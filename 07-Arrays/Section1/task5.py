array1 = [1, 2, 3, 4, 5]
print(array1)

array1[0] -= 1
print(array1)

array1[len(array1)-1] += 4
print(array1)

for index in range(1, len(array1)-1):
    array1[index] *=2

print(array1)