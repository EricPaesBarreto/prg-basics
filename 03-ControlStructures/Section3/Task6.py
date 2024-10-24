###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
days = int(input('Enter the day number of the month: '))
day_ok = False

if month == 2 and days == 28:
    day_ok = True
elif month < 8 :
    if month % 2 == 0 and days == 30:
        day_ok = True
    else:
        day_ok = False
else:
    if month % 2 == 0 and days == 31:
        day_ok = True
    else:
        day_ok = False

message = f'Day {days} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is not correct')