###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[len(arr)-1] )
print('Penultimate value', arr[len(arr)-2])
print('Sum of first and last value', arr[0] + arr[len(arr)-1])
print('Middle value', arr[int(len(arr)/2)])

str1 = ''
for element in range(len(arr)-1):
    str1 += str(element)
    str1 += ' '
str1 += str(arr[len(arr)-1])
print(str1)