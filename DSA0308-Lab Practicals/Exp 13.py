
import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> 'runs'
""")

parser = nltk.ChartParser(grammar)

sentence = "John runs".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
