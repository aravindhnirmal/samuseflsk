import os
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    image_folder = 'static/images'
    images = []
    for root, dirs, files in os.walk(image_folder):
        for filename in files:
            if any(ext in filename.lower() for ext in ['.jpg', '.jpeg', '.png', '.gif']):
                image_path = os.path.join(root, filename)
                images.append({'path': image_path})
    return render_template('home.html', images=images)

if __name__ == '__main__':
    freezer.freeze()
