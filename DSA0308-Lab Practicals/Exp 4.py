
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays", "running",
         "happiness", "ponies", "studies"]

for word in words:
    print(word, "->", ps.stem(word))
