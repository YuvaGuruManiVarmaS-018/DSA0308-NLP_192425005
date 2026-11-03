
words = ["I", "play", "cricket"]

emission = {
    "I": {"PRP": 0.9, "NN": 0.1},
    "play": {"VB": 0.8, "NN": 0.2},
    "cricket": {"NN": 0.9, "VB": 0.1}
}

for word in words:
    tag = max(emission[word], key=emission[word].get)
    print(word, "->", tag)
