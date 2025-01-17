import re
test_string = 'hello world, how are you today?'

regular_expression = '[aeiou]'

# gets all sections of the string between vowels (consonants)
result = re.split(regular_expression, test_string)
print(result)

consonants_other = "".join(result)
print(consonants_other)

regular_expression = '[a-zA-Z]+'
result = re.findall(regular_expression, consonants_other)
print(result)

consonants = "".join(result)
print(consonants)