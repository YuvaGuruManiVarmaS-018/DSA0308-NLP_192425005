
import nltk

text = "The boy plays cricket"

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print("POS Tags:")
for word, tag in tags:
    print(word, ":", tag)
