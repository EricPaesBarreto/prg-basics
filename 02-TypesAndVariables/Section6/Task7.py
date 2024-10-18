###
# A program that prints a numerical representation of each letter of your name.
#
name = input("Please enter your name: ")
for i in name:
    if i != ' ':
        print(f'The letter {i} has a code {ord(i)}')