
def parse(sentence):
    grammar = {
        "S": [["NP", "VP"]],
        "NP": [["John"], ["Mary"]],
        "VP": [["runs"], ["eats"]]
    }

    def check(symbols, words):
        if not symbols:
            return not words

        first = symbols[0]

        if first in grammar:
            for rule in grammar[first]:
                if check(rule + symbols[1:], words):
                    return True
            return False

        if words and first == words[0]:
            return check(symbols[1:], words[1:])

        return False

    return check(["S"], sentence.split())

sentence = "John runs"

if parse(sentence):
    print("Sentence is accepted")
else:
    print("Sentence is rejected")
