from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from gpt import OCRStuff


@app.route('/api/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    q=request.form.get('q')
    file = request.files['file']
    print(file)
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    res=OCRStuff(file,q)
    print(res)
    # You can now process the file, such as performing OCR
    # For demonstration, let's just return the file name
    return jsonify({'text': res})


if __name__ == '__main__':
    app.run(debug=True)
