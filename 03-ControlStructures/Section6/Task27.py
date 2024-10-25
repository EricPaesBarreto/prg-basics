for i in range(6,-1,-3):#start, stop, step
    for j in range(1,4):#start, stop
        print(f'{i+j}',end=' ')
    print()

print('\nWhile version: \n')

c1 = 6
while c1 > -1:#start, stop
    c2 = 1
    while(c2 < 4):#start, stop
        print(f'{c1+c2}', end=' ')
        c2+=1#step
    print()
    c1-=3#step