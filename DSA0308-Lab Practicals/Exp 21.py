
import spacy

nlp = spacy.load("en_core_web_sm")

sentence = "The student reads a book."

doc = nlp(sentence)

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
    print("Root Meaning:", chunk.root.text)
    print("Part of Speech:", chunk.root.pos_)
    print()
