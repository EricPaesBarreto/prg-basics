###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()

# get countries in array
countries = []
for line in file_lines:
   countries.append(line.split(', ')[0])

# sorts alphabetcally
countries = sorted(countries)

# prints the array
for index in range(len(countries)):
   print(f'{index+1}: {countries[index]}')