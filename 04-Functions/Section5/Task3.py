###
# Functions to read any data type from the keyboard
#
def input_string(message):
    result = input(message)
    return result

def input_integer(message):
    result = int(input(message))
    return result

def input_real(message):
    result = float(input(message))
    return result

def input_boolean(message):
    userin = input(message)
    if(userin == 'y'):
        result = False
    elif(userin == 'n'):
        result = True
    else: return
    return result