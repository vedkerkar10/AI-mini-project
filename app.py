from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # You can now process the file, such as performing OCR
    # For demonstration, let's just return the file name
    return jsonify({'text': file.filename})


if __name__ == '__main__':
    app.run(debug=True)
