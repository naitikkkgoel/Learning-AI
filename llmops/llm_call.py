import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("API key is invalid")

client = Groq(api_key=API_KEY)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "What is an API call?"

message = {
    "role": role,
    "content": prompt,
}

messages = [message]

response = client.chat.completions.create(model=model, messages=messages)
answer = response.choices[0].message.content
print(answer)
