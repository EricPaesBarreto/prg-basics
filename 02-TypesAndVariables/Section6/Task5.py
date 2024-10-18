###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
index = 1
phone_readable = ""
while(index <= len(phone)):
    phone_readable += phone[index-1]
    if(index % 3 == 0 and index != len(phone)):
        phone_readable += '-'
    index+=1
print(phone_readable)