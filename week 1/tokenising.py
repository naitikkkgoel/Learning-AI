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
prompt1 = "What is an API call?"
prompt2 = "Hi!"
prompt3 = "write an essay on freedom in 500 words"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt,
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=200)
    usage = response.usage
    print(f"Prompt: {prompt} --> Your prompt: {usage.prompt_tokens} --> completion_tokens: {usage.completion_tokens}  Total usage: {usage.total_tokens}  Finish reason: {response.choices[0].finish_reason}")




# answer = response.choices[0].message.content
# print(answer)
