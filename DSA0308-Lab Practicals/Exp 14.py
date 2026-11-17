
grammar = {
    "singular": ["he", "she", "john"],
    "plural": ["they", "we", "students"],
    "singular_verb": ["runs", "eats"],
    "plural_verb": ["run", "eat"]
}

def check_agreement(sentence):
    words = sentence.lower().split()

    if len(words) != 2:
        return False

    subject, verb = words

    if (subject in grammar["singular"] and
        verb in grammar["singular_verb"]):
        return True

    if (subject in grammar["plural"] and
        verb in grammar["plural_verb"]):
        return True

    return False

sentence = "he runs"

if check_agreement(sentence):
    print("Correct agreement")
else:
    print("Incorrect agreement")
