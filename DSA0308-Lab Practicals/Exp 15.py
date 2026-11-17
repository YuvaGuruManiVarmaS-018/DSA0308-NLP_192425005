
import nltk
from nltk import PCFG

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [0.6] | 'Mary' [0.4]
VP -> 'runs' [0.7] | 'eats' [0.3]
""")

parser = nltk.ViterbiParser(grammar)

sentence = "John runs".split()

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
