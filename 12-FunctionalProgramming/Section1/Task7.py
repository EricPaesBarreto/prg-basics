is_even = lambda n : n%2==0

nat_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(is_even,nat_nums)))
# expected result --> [False, True, False, True, False, 
#                       True, False, True, False, True]