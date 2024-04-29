from flask import Flask, request, jsonify
from PIL import Image
import pytesseract as tess
import requests

app = Flask(__name__)

tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

API_URL = (
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
)
HEADERS = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()


@app.route("/submit_form", methods=["POST"])
def submit_form():
    try:
        # Get the uploaded image file from the form data
        image_file = request.files["file"]
        # Perform OCR on the uploaded image
        text = tess.image_to_string(Image.open(image_file))
        # Combine OCR result with additional text if needed
        input_text = (
            "what can you infer from the following data about a food item and Elaborate on its effect on health by giving relevant comparison for better understanding"
            + text
        )
        # Query Hugging Face model
        output = query({"inputs": input_text})
        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
