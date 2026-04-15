import os
import google.generativeai as genai
from openai import OpenAI

class LLMProvider:
    def __init__(self, config: dict):
        self.provider_name = config["provider"]
        self.model_name = config["models"][self.provider_name]
        if self.provider_name == "openai":
            key = os.getenv("OPENAI_API_KEY")
            if not key:                
                raise ValueError("OPENAI_API_KEY environment variable not set")
            self.client = OpenAI(api_key=key)  # OpenAI client will read the API key from environment variable
        elif self.provider_name == "gemini":
            key = os.getenv("GEMINI_API_KEY")
            if not key:                
                raise ValueError("GEMINI_API_KEY environment variable not set")
            genai.configure(api_key=key)
            self.client = genai.GenerativeModel(self.model_name)
        else:
            raise ValueError(f"Unsupported provider: {self.provider_name}")
        
        print(f"Initialized LLMProvider with {self.provider_name.title()} and model {self.model_name}")
    
    def chat(self, user_message: str) -> str:
        try: 
            if self.provider_name == "openai":
                    response = self.client.chat.completions.create(
                        model=self.model_name,
                        messages=[{"role": "user", "content": user_message}]
                    )
                    return response.choices[0].message.content
            # except Exception as e:
            #     print(f"Error occurred while generating response: {e}")
            elif self.provider_name == "gemini":
                response = self.client.generate_content(
                    model=self.model_name,
                    contents=user_message
                )
                return response.text
        except Exception as e: 
            raise Exception(f"Error in {self.provider_name} chat: {str(e)}")