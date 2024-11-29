def read_from_file(file_name):
   with open(file_name, 'r') as file:
      content = file.read()
   return content

def count_words_in_file(file_name):
    content = read_from_file(file_name)
    content_lines = content.splitlines()
    total_words = 0
    for line in content_lines:
        total_words += len(line.split(' '))
    return total_words
   
if __name__ == '__main__':
   print(count_words_in_file('pets.txt'))