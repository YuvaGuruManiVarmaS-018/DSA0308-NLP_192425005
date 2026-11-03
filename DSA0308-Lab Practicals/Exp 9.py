
import re

def pos_tag(word):
    if re.match(r".*ing$", word):
        return "VBG"
    elif re.match(r".*ed$", word):
        return "VBD"
    elif re.match(r".*ly$", word):
        return "RB"
    elif word in ["he", "she", "I", "we", "they"]:
        return "PRP"
    else:
        return "NN"

words = ["playing", "walked", "slowly", "he", "book"]

for word in words:
    print(word, "->", pos_tag(word))
