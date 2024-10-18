###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# determine tempereature in celsius
# multiply by the fraction (9/5)
# add 32 
celsius = int(input("Enter temperature (c): "))
farenheit = round(((celsius * (9/5)) + 32), 2)
print(f"Farenheit: {farenheit}")