def contains_negative(array):
    for value in array:
        if value < 0:
            return True
    return False


print(contains_negative([11, 6, -4]))
print(contains_negative([5, 4, 14]))