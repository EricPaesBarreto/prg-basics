size = 9
str1 = ''
if size%2==0:
    add = 1
else:
    add = 2

for i in range(1, (size//2)+add):
    for n in range(1, i+1):
        str1 += '*'
    str1 += '\n'

for i in reversed(range(1, (size//2) + add-1)):
    for n in range(1, i+1):
        str1 += '*'
    str1 += '\n'
print(str1)