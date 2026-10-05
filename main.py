from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=300,
    messages=[
        {"role": "user", "content": "Explain what an API is in one sentence."}
    ],
)

print(message.content[0].text)



