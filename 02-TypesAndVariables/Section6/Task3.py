###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
first = True
index = 0
initials = ""
while(index < len(university)):
    if(first):
        if(university[index].isupper()):
            initials += university[index]
            first=False
    if(university[index] == ' '):
        first = True
    index+=1
print(initials)