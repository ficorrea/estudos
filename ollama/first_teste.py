import os
from dotenv import load_dotenv
load_dotenv()

from ollama import chat

response = chat(
    model='llama3.2:1b',
    messages=[{'role': 'user', 'content': 'crie um código em python para soma recursiva'}],
)
print(response.message.content)