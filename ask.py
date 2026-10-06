from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

question = input("Ask Claude anything: ")

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=500,
    messages=[
        {"role": "user", "content": question}
    ],
)

print(message.content[0].text)
