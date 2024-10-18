###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if(char == ' '):
        continue
    encrypted_text += chr((ord(char) + 1))

print(f'Plain text: {plain_text}' )
print(f'Encrypted text: {encrypted_text}')