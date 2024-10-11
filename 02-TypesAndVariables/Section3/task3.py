###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
x+=y
y=x-y
x=(y-x)*(-1)

print("After swapping: x=", x, "y=", y)