###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12)'))

if month < 1 or month > 12:
    days = 'N/A'
elif month == 2:
    days = 28
elif month < 8 :
    if month % 2 == 0:
        days = 30
    else:
        days = 31
else:
    if month % 2 == 0:
        days = 31
    else:
        days = 30


print(f'Month {month} has {days} days')