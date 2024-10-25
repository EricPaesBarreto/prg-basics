import random
stri = ''

for i in range(1,21):
    stri += (str(i)+': '+str(random.randint(5,10))+'\n')

print(stri)