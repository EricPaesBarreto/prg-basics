###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

import math
radius = float(input("Enter radius: "))
area = round((math.pi * (radius**2)), 2)
circumference = round((2 * math.pi * radius), 2)
print(f"Area: {area}, circumference: {circumference}")