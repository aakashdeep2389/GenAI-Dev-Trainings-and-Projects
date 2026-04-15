import os
import requests
from dotenv import load_dotenv

load_dotenv()

prompt = "can you personal trade to buy or sell in FnO?"


model_id = "gpt3.5"
api_url = f"https://api-inference.huggingface.co/models/{model_id}"

header = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

payload = {
    "inputs": prompt, "parameters": {"max_new_tokens": 200}}

response = requests.post(api_url, headers=header, json=payload)
response.raise_for_status()  # Check for HTTP errors
data = response.json()

print(data[0]["generated_text"].strip())