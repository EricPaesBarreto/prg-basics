attempts = 3
correct_pin = '0805'
while attempts > 0:
    attempt = input('Enter PIN: ')
    if(attempt == correct_pin):
        attempts = -1
    else:
        attempts -=1
        print('Incorrect...')
if(attempts == 0):
    print('Sorry, your payment card has been blocked.')