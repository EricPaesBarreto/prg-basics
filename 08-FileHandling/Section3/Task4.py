###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r') as file:
    email = file.read()

# regular expression pattern
# for amounts
pattern = 'â‚¬(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

total = 0
# calculate the total purchases
for amount in amounts:
   total += int(amount)

# print result
print(total)