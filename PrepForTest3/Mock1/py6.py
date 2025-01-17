def f(password):
    # check if the first letter is uppercase or '_'
    if not (password[0] == "_" or password[0].isalpha()):
        return False
    # check if every letter is in the alphabet or contains a _
    for cha in password:
        if not (cha.isalpha() or cha == "_" or cha.isdigit()):
            return False
    return True
    
if __name__ == "__main__":
    print(f("abc"))
    print(f("Abc"))
    print(f("aBC"))
    print(f("_ab_c"))
    print(f("abcdef")) # example provided is wrong, should be True
    print(f("8abc"))
    print(f("_aB8_"))
    print(f("_4x"))