two_three = lambda num : num%3==0 and num%2==0

nums = [i+1 for i in range(20)]

print(list(filter(two_three, nums)))