from functools import reduce

add = lambda a,b : a+b

pi_nums = [3,1,4,1,5]

sum_5_pi_digits = reduce(add, pi_nums)

print(sum_5_pi_digits)

def average(count):
    return lambda a,b : a + (b/count)

def find_average(nums):
    nums[0] /= len(nums)
    return reduce(average(len(nums)), nums)

average_pi = find_average(pi_nums)
print(average_pi)
print(pi_nums) # sadly this changes our original first number into a new one :(