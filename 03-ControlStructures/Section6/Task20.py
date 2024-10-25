decimal = int(input('Enter decimal: '))
base = 2
result = ''

while decimal >= 1:
    remainder = decimal/base - int(decimal/base)
    decimal /= base
    result += str(int(remainder*base))
print(result[::-1])