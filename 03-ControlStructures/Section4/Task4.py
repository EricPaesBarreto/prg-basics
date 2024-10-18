###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character)
#
university = 'Krakow University of Economics'
university_expanded = ''

for i in range(0, len(university)):
    university_expanded += university[i]
    if(i != len(university) - 1 ):
        university_expanded += ' '

print(f'University name: {university}')
print(f'University name expanded: {university_expanded}')