###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
counter = 0

# Count vowels in the text
while counter < len(text):
    if text[counter] in vowels:
        vowel_count += 1
    counter+=1

print(f"The number of vowels in the text is: {vowel_count}")
