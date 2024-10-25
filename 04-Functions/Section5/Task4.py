###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import Task3

# Reads employee's data from keyboard
first_name = Task3.input_string('Enter name: ')
last_name = Task3.input_string('Enter surname: ')
age = Task3.input_integer('Enter age: ')
salary = Task3.input_integer('Enter salary: ')
is_salary_hidden = Task3.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Surname: ', last_name)
print('Age: ', age)
if is_salary_hidden:
    print('Salary: ', salary)