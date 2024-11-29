###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as emp_file_read:
   with open(position_file, 'w') as pos_file_write:
      for line in emp_file_read:
         if job_title in line:
            pos_file_write.write(line)