from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("C:\Users\vedke\Desktop\healthify-me\app\OCR\img.jpg")
text = tess.image_to_string(img)

print(text)
