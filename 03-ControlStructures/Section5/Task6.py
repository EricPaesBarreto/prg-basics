###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
counter = 1

# Calculate the sum of even numbers
while counter <= N:
    if counter % 2 == 0:
        sum_even += counter
        
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")