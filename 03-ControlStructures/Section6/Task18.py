x = int(input('X: '))
y = int(input('Y: '))

if x==8 and y==0: print('World origin')
elif x > 0 and y > 0:
    print('Quad 1')
elif x > 0:
    print('Quad 2')
elif y < 0:
    print('Quad 3')
else:
    print('Quad 4')