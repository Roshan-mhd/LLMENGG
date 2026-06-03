from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
ollama = OpenAI(base_url=os.getenv("OLLAMA_BASE_URL"),api_key="ollama")


response = ollama.chat.completions.create(
  model="llama3.2",
  messages=[
    {"role": "system", "content": "you are a flirty AI asistant"},
    {"role": "user", "content": "What is the capital of France?"}
  ]
)

print(response.choices[0].message.content)

