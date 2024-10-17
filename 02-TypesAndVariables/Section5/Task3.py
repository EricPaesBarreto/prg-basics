###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input("b="))
c = int(input("c="))
volume = a*b*c
surface_area = (a*b + b*c + c*a)*2
print(f"a = {a}, b = {b}, c = {c} --> volume = {volume}, surface area = {surface_area}")