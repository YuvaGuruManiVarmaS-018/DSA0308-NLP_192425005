
# Finite State Machine for Plural Nouns

def plural_fsm(noun):
    state = "START"

    # State 1: Check irregular nouns
    irregular = {
        "goose": "geese",
        "mouse": "mice",
        "child": "children",
        "man": "men"
    }

    if noun in irregular:
        state = "IRREGULAR"
        return irregular[noun]

    # State 2: Check special endings
    elif noun.endswith(("s", "x", "ch", "sh")):
        state = "ADD_ES"
        return noun + "es"

    # State 3: Regular plural
    else:
        state = "ADD_S"
        return noun + "s"


# Main program
word = input("Enter a singular noun: ")

plural = plural_fsm(word)

print("Singular Noun:", word)
print("Plural Noun:", plural)
