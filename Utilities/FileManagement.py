import os

def create_file(filename):
    try:
        open(filename, 'w')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)

def create_folder(foldername):
        try:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), foldername)
            os.mkdir(foldername)
            print("File " + foldername + " created successfully.")
        except IOError:
            print("Error: could not create file " + foldername)
