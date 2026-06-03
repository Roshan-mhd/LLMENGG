from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

ollama = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key="ollama"
)

history = [
    {"role": "system", "content": "You are a flirty AI assistant"}
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        break
    history.append({
        "role": "user",
        "content": user_input
    })
    response = ollama.chat.completions.create(
        model="llama3.2",
        messages=history
    )
    ai_reply = response.choices[0].message.content
    print("AI:", ai_reply)
    history.append({
        "role": "assistant",
        "content": ai_reply
    })