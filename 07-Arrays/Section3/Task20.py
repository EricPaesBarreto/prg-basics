def second_largest(nums):
    snums = sorted(nums)
    count = len(snums)
    if count == 1:
        return nums[0]
    else:
        return snums[count-2]

def largest(nums):
    largest = float('-inf')
    for num in nums:
        if num > largest:
            largest = num
    return largest

def smallest(nums):
    smallest = float('inf')
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest

def difference(nums):
    return largest(nums) - smallest(nums)

def is_even(num):
    return (num%2==0)

import math

def median(nums):
    snums = sorted(nums)
    half = len(snums)//2
    if is_even(len(snums)):
        return snums[half-1] + (snums[half] - snums[half-1]) / 2
    else:
        return snums[half]

def extrema(nums):
    return [smallest(nums), largest(nums)]

def stringify(nums):
    result = str(nums[0])
    for index in range(1,len(nums)):
        result += '-'
        result += str(nums[index])
    return result

test_array = [7,3,8,5,2]

print('Numbers:',test_array)
print('Second largest:',second_largest(test_array))
print('Smallest:',smallest(test_array))
print('Largest:',largest(test_array))
print('Difference:',difference(test_array))
print('Median:',median(test_array))
print('Extrema:',extrema(test_array))
print('String:',stringify(test_array))