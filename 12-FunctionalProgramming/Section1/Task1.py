def add(x,y):
    return x + y
def divide(x,y):
    return x / y
def mean(x,y):
    return divide(add(x,y),2)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

result = mean(n1,n2)
print(f'The mean of the numbers {n1}, and {n2}, is {result}.')