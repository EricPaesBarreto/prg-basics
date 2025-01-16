array1 = [-15, 8, -31, 47, -2, 19]
min = float('inf')
max = float('-inf')

for value in array1:
    if value > max:
        max = value
    if value < min:
        min = value

print('min:',min,'max:',max)