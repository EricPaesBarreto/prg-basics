###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
min = 1
max = 20
total = 0
index = 0
while(index < 3):
    total += random.randint(min, max)
    index += 1
print(f"sum: {total}")