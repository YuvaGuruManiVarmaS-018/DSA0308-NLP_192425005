import spacy

nlp = spacy.load("en_core_web_sm")

text = "Google was founded by Larry Page in California."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ":", ent.label_)
