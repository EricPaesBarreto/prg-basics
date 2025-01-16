array1 = [15, 8, 31, 47, 2, 19]
count = len(array1)
index = 0
mean = 0

while index < count:
    mean += array1[index]
    index += 1

mean /= count
print(round(mean,1))