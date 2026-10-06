from dotenv import load_dotenv
import anthropic
import json
import os

load_dotenv()

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are Aryan's personal AI assistant.
Be direct, honest and concise. No fluff or generic motivation.
Aryan is a UCL student learning to build AI tools."""

MEMORY_FILE = "memory.json"

# Load past conversations if the file exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE) as f:
        history = json.load(f)
    print("Memory loaded.")
else:
    history = []

print("Assistant ready. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=history,
    )

    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})

    # Save the conversation after every reply
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

    print(f"\nAssistant: {reply}\n")

