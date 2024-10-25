EAN_13 = input('Enter EAN-13: ')
if(len(EAN_13) == 13):
    print('Article number is correct')
    if(EAN_13[0:3] == '590'):
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')