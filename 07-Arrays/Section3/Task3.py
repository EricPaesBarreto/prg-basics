array1 = 34,7,19,4,21,8
def is_even(input):
    return (input%2==0)

count = 0
for value in array1:
    if is_even(value):
        count += 1

print(count)