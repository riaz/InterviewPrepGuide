import os
import anthropic

api_key = os.getenv("CLAUDE_KEY")

if not api_key:
    print("Set CLAUDE_KEY ENV VARIABLE in bashrc")
    exit(0)

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=api_key
)
message = client.messages.create(
    model="claude-2.1",
    max_tokens=1000,
    temperature=0,
    system="You are a helpful coding assistant for Rust Programming Language. And believe in providing code as concrete examples to queries",
    messages=[
        {"role": "user", "content": "How to I create a rust project for production with git action CI/CD"}
    ]
)

print(message.content)