import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()


for model in models:
    if "generateContent" in getattr(model, "supported_generations_methods", []):
        print("Model Name:", model.name)

    else:
        print("Skip:", model.name, "sopprts:", getattr(model, "supported_generations_methods", []))