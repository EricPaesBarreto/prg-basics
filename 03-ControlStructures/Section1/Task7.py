###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = input('Recieve bonus? (Y/N): ') == 'Y' # does the employee receive a bonus
bonus = float(input("Enter a bonus percentage (%): ")) // 100

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')