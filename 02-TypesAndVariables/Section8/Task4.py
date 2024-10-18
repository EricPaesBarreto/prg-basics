###
# A program that prints your height both in cm and in feet and inches.
#
import math
cm = int(input("enter height (cm): "))
feet = cm * 0.0328084
inches = (feet - int(feet)) * (12)

# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {math.floor(feet)} feet and {math.floor(inches)} inches')