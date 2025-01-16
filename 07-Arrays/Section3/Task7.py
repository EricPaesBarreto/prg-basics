array1 = [15, 8, 31, 47, 2, 19]
total = len(array1)
mean = 0

for value in array1:
    mean += value
mean /= total

print(round(mean,1))