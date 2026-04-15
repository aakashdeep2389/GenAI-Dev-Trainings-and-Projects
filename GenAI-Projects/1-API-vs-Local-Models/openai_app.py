import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "can you personal trade to buy or sell in FnO?"

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "user", "content": prompt}
    ],
    max_tokens = 200
)

print(response)