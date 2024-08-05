import os
from dotenv import load_dotenv
import requests
import io
from PIL import Image

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Request failed with status code {response.status_code}")

try:
    image_bytes = query({
        "inputs": "a white horse with a black background",
    })

    # Debugging: Check response size and type
    print(f"Response size: {len(image_bytes)} bytes")
    print(f"Response type: {type(image_bytes)}")

    # Load and save the image
    image = Image.open(io.BytesIO(image_bytes))
    image.save("white horse.jpg")
    print("Image saved as smiling_cat.jpg")

except Exception as e:
    print(f"An error occurred: {e}")
