###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    index = 1
    for line in file:
        print(f'{index}.', line, end="")
        index += 1