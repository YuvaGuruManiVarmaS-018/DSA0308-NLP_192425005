
def dialog_act(sentence):
    sentence = sentence.lower()

    if any(word in sentence for word in ["hello", "hi", "hey"]):
        return "Greeting"

    elif sentence.endswith("?"):
        return "Question"

    elif "please" in sentence:
        return "Request"

    elif "thank" in sentence:
        return "Thanking"

    else:
        return "Statement"


dialog = [
    "Hello",
    "How are you?",
    "Please help me",
    "Thank you"
]

for sentence in dialog:
    print(sentence, ":", dialog_act(sentence))
