###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Eric'   # replace Anna with your name
surname = 'Barreto' # replace May with your surname
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(name+surname)} characters') # with a space between name and surname