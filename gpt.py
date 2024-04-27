from PIL import Image
import requests
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


img = Image.open(r'C:\Users\vedke\Desktop\AI-project\backend\img.jpg')
text = tess.image_to_string(img)

API_URL = (
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
)
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query(
    {
        "inputs": "what can you infer from the following data about a food item and Elaborate on its effect on health by giving relevant comparision for better understanding"
        + text,
    }
)

print(output)
