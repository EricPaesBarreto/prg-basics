cube = lambda num : num ** 3

nums =  [i+1 for i in range(20)]

print(list(map(cube, nums)))