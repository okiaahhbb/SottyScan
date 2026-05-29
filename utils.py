import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        return text[:3000] if text else None
    except:
        return None
    
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r'E:\software all\tesseract.exe'

def extract_text_from_image(image_file):
    try:
        image = Image.open(image_file)
        text = pytesseract.image_to_string(image, lang='ben+eng')
        return text.strip() if text.strip() else None
    except:
        return None