
from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = "Hello, how are you?"

tokens = tokenizer(text, return_tensors="pt", padding=True)

translated = model.generate(**tokens)

result = tokenizer.decode(
    translated[0],
    skip_special_tokens=True
)

print("English:", text)
print("French:", result)
