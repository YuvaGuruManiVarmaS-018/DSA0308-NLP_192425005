
import nltk
from nltk.wsd import lesk

nltk.download("wordnet")
nltk.download("omw-1.4")

sentence = "I went to the bank to deposit money"

meaning = lesk(sentence.split(), "bank")

print("Word: bank")
print("Meaning:", meaning.definition())
