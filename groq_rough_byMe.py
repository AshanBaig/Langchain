from groq import Groq

client = Groq( api_key="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")
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "user",
        "content": "HI"
      },
      {
        "role": "assistant",
        "content": "Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?"
      },
      {
        "role": "user",
        "content": "Tell me what is 10*2 in detail"
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
