first = lambda text : text[0]
initials = lambda input : map(first, input.split(' '))

print(list(initials("Eric Paes Barreto")))