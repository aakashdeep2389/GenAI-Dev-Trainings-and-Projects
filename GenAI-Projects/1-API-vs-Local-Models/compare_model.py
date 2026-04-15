import os
import logging
from dotenv import load_dotenv
from typing import Dict, Any
import google.generativeai as genai 


load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

prompt = "can you personal trade to buy or sell in FnO?"

def run_gemini_model(prompt: str) -> str:
    try:
       
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content("What is the capital of France?")
        return response.text.strip() 
        
    except Exception as e:
        logging.error(f"Error occurred while running OpenAI model: {e}")
        return "An error occurred while processing your request."
    
def run_huggingface_model(prompt: str) -> str:
        try:
            api_url = f"https://api-inference.huggingface.co/models/gpt3.5"
            headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
            payload = {"inputs": prompt, "parameters": {"max_new_tokens": 200}}
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data[0]["generated_text"].strip()
        except Exception as e:
            logging.error(f"Error occurred while running Hugging Face model: {e}")
            return "An error occurred while processing your request."
        
def run_ollama_model(prompt: str) -> str:
    try:
        # Implement the logic to call your local Ollama model here
        # For example, you might use subprocess to run a local server or command-line tool
        return "Ollama model response (placeholder)"
    except Exception as e:
        logging.error(f"Error occurred while running Ollama model: {e}")
        return "An error occurred while processing your request."
    
    
    
def run_all_models(prompt: str) -> Dict[str, Any]:
    logging.info("Running all models with the given prompt...")
    results = {
        "google_gemini": run_gemini_model(prompt),
        "hugging_face": run_huggingface_model(prompt),
        "ollama": run_ollama_model(prompt)
    }
    return results

if __name__ == "__main__":
    results = run_all_models(prompt)
    for model_name, response in results.items():
        print(f"{model_name} response: {response}\n")