###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum = 0
    str_num = str(number)
    for char in str_num:
        sum += int(char)
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print('The sum of the digits in the number  is: ', result)