import os
from pathlib import Path
import json
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel





load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("API key not provided")

client = Groq(api_key=API_KEY)

model = "openai/gpt-oss-120b"
role = "user"
text = "Hello my name is Naitik. I purchased a Bluetooth speaker and it has stopped working. I reside in Delhi. My email is naitikgoel4456@gmail.com and my phone number is 9870513287 please resolve this issue"
class Info(BaseModel):
    name: str
    email: str
    phone: int
    issue: str

schema = Info.model_json_schema()

response_format = {
    "type" : "json_object"
}

system_prompt = f"""
Extract personal information from the ticket in json format strictly based on this schema
{schema}
"""

message_system = {
    "role": "system",
    "content": system_prompt,
}
prompt = f"""
This is a customer ticket. Extract information from this {text}
"""
message = {
    "role": role,
    "content": prompt,
}

messages = [message_system,message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)
answer = response.choices[0].message.content


raw_json = answer
data = json.loads(raw_json)
ticket = Info(**data)

with open("answer.json", "w") as file:
    json.dump(data, file, indent=4)