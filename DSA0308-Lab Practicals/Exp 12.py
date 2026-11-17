
def earley_parser(words):
    grammar = {
        "S": [["NP", "VP"]],
        "NP": [["John"]],
        "VP": [["runs"]]
    }

    n = len(words)
    chart = [set() for _ in range(n + 1)]
    chart[0].add(("S", ("S",), 0, 0))

    for i in range(n + 1):
        changed = True
        while changed:
            changed = False

            for item in list(chart[i]):
                lhs, rhs, dot, start = item

                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol in grammar:
                        for rule in grammar[symbol]:
                            new = (symbol, tuple(rule), 0, i)
                            if new not in chart[i]:
                                chart[i].add(new)
                                changed = True

                    elif i < n and symbol == words[i]:
                        chart[i + 1].add(
                            (lhs, rhs, dot + 1, start)
                        )

                else:
                    for prev in list(chart[start]):
                        pl, pr, pd, ps = prev
                        if pd < len(pr) and pr[pd] == lhs:
                            new = (pl, pr, pd + 1, ps)
                            if new not in chart[i]:
                                chart[i].add(new)
                                changed = True

    return ("S", ("S",), 1, 0) in chart[n]

sentence = "John runs".split()

if earley_parser(sentence):
    print("Sentence accepted")
else:
    print("Sentence rejected")
