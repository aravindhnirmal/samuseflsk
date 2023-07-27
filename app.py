import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    image_folder = r'C:\Users\NIRMAL\Desktop\project4thyear\project_blog\static\images'
    images = []
    for filename in os.listdir(image_folder):
        if any(ext in filename.lower() for ext in ['.jpg', '.jpeg', '.png', '.gif']):
            images.append({'filename': filename})
    return render_template('home.html', images=images)

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory('static/images', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
