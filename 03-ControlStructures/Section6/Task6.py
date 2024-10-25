hours = 0
while hours < 1:
    hours = int(input('No. hours: '))

if hours < 3:
    cost = 5
elif hours < 7:
    cost = 15
else:
    cost = 20

print(f'The ticket will cost {cost} PLN')