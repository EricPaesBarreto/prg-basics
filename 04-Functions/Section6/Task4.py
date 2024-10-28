def char_in_string(text, letter):
    count = 0
    for char in text:
        if letter == char:
            count+=1
    return count

test_string = 'You never get a second chance to make a first impression'
print('The number of letter e: ', char_in_string(test_string, 'e'))