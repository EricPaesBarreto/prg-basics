numbers = [(17,15,16,17,15),
            (16,18,19,17,19),
            (19,15,15,19,18),
            (18,17,19,15,16)]

min_max = lambda scores : sum(sorted(scores)[1:len(scores)-1])

print(list(map(min_max, numbers)))