ms_to_kmh = lambda ms : ms * 60 * 60 / 1000

ms = int(input("Please enter speed in seconds: "))

result = ms_to_kmh(ms)

print(f'{ms}m/s in kmph is: {result}')