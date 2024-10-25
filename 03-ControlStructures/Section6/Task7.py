age = -1
while age < 0:
    age = int(input('Enter age of child: '))

if age < 13:
    print('Child')
elif age <= 19:
    print('Teen')
elif age <= 64:
    print('Adult')
else: print('Senior')