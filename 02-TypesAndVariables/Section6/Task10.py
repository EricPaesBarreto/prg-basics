###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Capitalized: ', movie.capitalize)

# print title in small letters
print('Lower-case: ', movie.casefold)

# print how many times the vowel "e" appears in the title
print('Number of times [e] appears: ', movie.count("e"))

# print where in the text is the word "Lord"
print('The position at which the word [lord] appears: ', movie.find("Lord"))

# print where in the text is the word "dragon"
print('The position at which the word [dragon] appears: ', movie.find("dragon"))
#dragon does not exist in the string so the value [-1] is returned