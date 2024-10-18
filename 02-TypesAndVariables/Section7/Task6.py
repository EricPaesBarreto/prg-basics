speed = float(input("Please enter your speed in km/h: "))
#assume speed limit is inclusive (140 is allowed but >140 is not)
valid_speed = speed >= 40 and speed <= 140
print(f"Speed is valid: {valid_speed}")