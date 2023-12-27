import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Define a prompt
prompt_text = "Once upon a time, in a land far, far away, there was a"

# Generate text using ChatGPT
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt_text,
  max_tokens=100
)

# Get the generated text
generated_text = response.choices[0].text.strip()
print(generated_text)
