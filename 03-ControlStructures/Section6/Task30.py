stri = ''
for i in range (1, 8):
    for n in range(0, 7):
        stri += (str(i + 7*n)+' ')
    stri+='\n'

print(stri)