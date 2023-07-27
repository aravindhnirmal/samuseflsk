import os
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

def get_images(image_folder):
    images = []
    for filename in os.listdir(image_folder):
        if any(ext in filename.lower() for ext in ['.jpg', '.jpeg', '.png', '.gif']):
            images.append({'filename': filename})
    return images

def get_image_chunks(images, chunk_size):
    chunked_images = [images[i:i + chunk_size] for i in range(0, len(images), chunk_size)]
    return chunked_images

@app.route('/')
def index():
    image_folder = r'C:\Users\NIRMAL\Desktop\project4thyear\project_blog\static\images'
    images = get_images(image_folder)

    chunk_size = 30  # Number of images to display per page
    page = int(request.args.get('page', 1))
    image_chunks = get_image_chunks(images, chunk_size)
    current_chunk = image_chunks[page - 1] if 0 < page <= len(image_chunks) else []
    return render_template('home.html', images=current_chunk, page=page, num_pages=len(image_chunks))

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory('static/images', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
