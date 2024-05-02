from PIL import Image
import requests
import pytesseract as tess






def query(payload):
    
    API_URL = (
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    )
    headers = {"Authorization": "Bearer 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"}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()




# print(output)


def OCRStuff(file=r'C:/Users/vedke/Desktop/AI-project/backend/img.jpg' ,q="how healthy is the product?"):
    tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 
    img = Image.open(file)
    text = tess.image_to_string(img)
    # q="what can you infer from the following data about a food item and give me asummary of its effect on health by giving relevant comparision for better understanding, keep it short"
    output = query(
    {
        "inputs": q
        # + text,
    }
    )

    return output[0]['generated_text'].replace(q,'')


if __name__ =="__main__":
    pass