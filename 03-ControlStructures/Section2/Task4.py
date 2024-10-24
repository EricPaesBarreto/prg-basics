###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input('First number: '))
number2 = float(input('Second number: '))
operator = input('Operator: ')

if operator == '+':
    result = number1+number2
elif operator == '-':
    result = number1-number2
elif operator == '*':
    result = number1*number2
elif operator == '/':
    result = number1/number2
else:
    print('Unrecognized operator.')
    result = 'N/A'

# print result
print(f'{number1} {operator} {number2} = {result}')