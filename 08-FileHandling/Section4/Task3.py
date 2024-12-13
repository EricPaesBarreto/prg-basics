import re
def stuff():
    with open('email.txt', 'r') as file:
        file_as_string = file.read()
    frEmails = "by\s(.+\.+com)"
    foEmails = "for\s<(.+)>"

    from_emails = re.findall(frEmails, file_as_string)
    for_emails = re.findall(foEmails, file_as_string)
    
    print(for_emails)
    print(from_emails)

if __name__ == "__main__":
    stuff()