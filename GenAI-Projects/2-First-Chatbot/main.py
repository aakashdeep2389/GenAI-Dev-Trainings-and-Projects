import os
import json
from urllib import response
from dotenv import load_dotenv
from llm_provider import LLMProvider

def load_config(config_path: str = "config.json") -> dict:
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at path: {config_path}")
    except json.JSONDecodeError:
        raise ValueError(f"invalid JSON in the config file: {config_path}")
    
def run_chat():
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    try:
        config = load_config()
        print(f"Loaded configuration: {config['provider']} with model {config['models'][config['provider']]}")
        bot = LLMProvider(config)
        
    except (Exception, ValueError) as e:
        print(f"Initialization Error: {e}")
        return
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not user_input.strip():
            print("Please enter a valid message.")
            continue
        try:
            reply = bot.chat(user_input)
            print(f"Bot: {reply}\n")
        except Exception as e:
            print(f"Error during chat: {e}")
            

if __name__ == "__main__":
    load_dotenv()
    run_chat()
           