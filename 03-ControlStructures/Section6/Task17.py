time = input('Enter time: ')
hour = int(time[0:2])
if hour >= 12: 
    pm = 'pm' 
    hour//=2
else: 
    pm = 'am'
minute = time[3:5]
print(f'The time in the 12-four format is: {hour}:{minute}{pm}')