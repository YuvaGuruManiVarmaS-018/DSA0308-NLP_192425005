
import nltk
from nltk.corpus import wordnet

nltk.download("wordnet")

word = "book"

synsets = wordnet.synsets(word)

for syn in synsets:
    print("Meaning:", syn.definition())
    print("Synonyms:", syn.lemma_names())
    print()
