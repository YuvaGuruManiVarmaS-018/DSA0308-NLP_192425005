
import random
from nltk import word_tokenize, bigrams
from collections import defaultdict

text = "I like tea. I like coffee. I like tea."

words = word_tokenize(text.lower())
model = defaultdict(list)

for w1, w2 in bigrams(words):
    model[w1].append(w2)

word = "i"
result = [word]

for i in range(5):
    next_words = model.get(word)
    if not next_words:
        break
    word = random.choice(next_words)
    result.append(word)

print("Generated Text:", " ".join(result))
