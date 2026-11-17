
import spacy

nlp = spacy.load("en_core_web_sm")

text = "John bought a car. He drives it every day."

doc = nlp(text)

nouns = []

for token in doc:
    if token.pos_ in ["NOUN", "PROPN"]:
        nouns.append(token.text)

for token in doc:
    if token.pos_ == "PRON":
        if token.text.lower() == "he":
            print(token.text, "refers to John")
        elif token.text.lower() == "it":
            print(token.text, "refers to car")
