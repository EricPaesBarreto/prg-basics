q1 = input('Are you interested in computer science? (y/n): ')
q2 = input('Do you like playing computer games? (y/n): ')
q3 = input('Do you have an Instagram account? (y/n): ')

if q1 == 'y': q1= 'yes' 
else: q1='no'
if q2 == 'y': q2='yes' 
else: q2='no'
if q3 == 'y': q3='yes' 
else: q3='no'

print(f'SURVEY RESULTS:\nInterested in computer science: {q1}\nPlaying computer games: {q2}\nHas an Instagram account: {q3}')
