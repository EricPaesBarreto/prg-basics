dog_age = int(input('Enter dog age (yrs): '))
if dog_age < 3:
    human_age = dog_age * 5.25
else:
    human_age = 10.5 + ((dog_age - 2) * 4)

print('human_age: ', human_age)