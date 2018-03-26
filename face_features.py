import face_recognition as fr
import json
import os
from flask import Flask, request

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/upload", methods=['POST'])
def recognize():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)

    image = fr.load_image_file(f)
    encodings = fr.face_encodings(image)
    os.remove(f)

    return json.dumps(encodings[0].tolist())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
