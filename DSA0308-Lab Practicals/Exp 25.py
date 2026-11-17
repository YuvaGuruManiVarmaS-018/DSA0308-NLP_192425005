
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

prompt = "Artificial Intelligence is"

result = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1
)

print("Generated Text:")
print(result[0]["generated_text"])
