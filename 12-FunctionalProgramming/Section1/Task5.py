def avg_speed(d, h, m):
    return d/(h + (m / 60))

distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

result = avg_speed(distance, hours, minutes)
print(f'Avergage speed: {round(result,2)}')