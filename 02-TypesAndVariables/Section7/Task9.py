import random
dice_rolled = 4
index = 0
special_number_rolled = False
while index < dice_rolled:
    random_num = random.randint(1, 6)
    print(random_num)
    if random_num == 1 or random_num == 6:
        special_number_rolled = True
    index += 1
print(f"Dice rolled: {dice_rolled}")
print(f"Special number (1 or 6): {special_number_rolled}")