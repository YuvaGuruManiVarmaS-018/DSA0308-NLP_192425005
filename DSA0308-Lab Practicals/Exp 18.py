
import re

def fopc_parser(expression):
    tokens = re.findall(
        r'forall|exists|and|or|not|implies|[A-Za-z_]\w*|[(),]',
        expression
    )

    print("Tokens:", tokens)

    if tokens.count("(") == tokens.count(")"):
        print("Logical expression is valid")
    else:
        print("Invalid logical expression")

expression = "forall(x, Human(x))"

fopc_parser(expression)
