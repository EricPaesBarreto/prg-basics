amount = int(input('Enter amount: '))

five = 0
two = 0
one = 0

while amount > 0:
    if amount > 4: 
        amount -= 5
        five +=1
    elif amount > 1:
        amount -=2
        two +=1
    else:
        amount -=1
        one +=1

print(f'5 pln coins: {five}\n2 pln coins: {two}\n1 pln coins: {one}')