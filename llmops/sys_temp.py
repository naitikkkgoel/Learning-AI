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
prompt = "Suggest a name for my new hair salon for both men and women"


message_system={
    "role":"system",
    "content":"You are a brand manager who suggests trendy names for upcoming businesses, name should be in one word, suggest only one",
}

message = {
    "role": role,
    "content": prompt,
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, temperature=1)
answer = response.choices[0].message.content
print(answer)
