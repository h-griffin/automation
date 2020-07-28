
# with open('notes.txt', 'w+') as f:
#     f.write(content)

        # re_dash = r'\d\d\d-\d\d\d-\d\d\d\d'
        # re_paren = r'\(\d\d\d\)\d\d\d-\d\d\d\d'
        # re_dot = r'\d\d\d\.\d\d\d\.\d\d\d\d'
        # re_area_dash = r'\d\d\d-\d\d\d\d'
        # re_area_dot = r'\d\d\d\.\d\d\d\d'

import re

def pull_numbers(original, new):
    """takes in 2 files as arguments, one origional file to read from and a new file to print phone numbers from origional"""
    with open(original) as contents:
        contents = contents.read()

        ten_digits = re.findall(r'\d{3}.\d{3}.\d{4}', contents)
        erase_paren_dot = [num.replace(')', "-") for num in ten_digits]
        erase_dot = [num.replace('.', '-') for num in erase_paren_dot]
        erase_dot.sort()

    with open(new, 'w+') as f:
        for num in erase_dot:
            f.write(num + '\n')

def pull_emails(original, new):
    """takes in 2 files as arguments, one origional file to read from and a new file to print emails from origional"""
    with open(original) as contents:
        contents = contents.read()

        emails = re.findall(r'[\w-]+@[\w-]+\.(?:com|net|org|info)', contents)
        emails.sort()

    with open(new, 'w+') as f:
        for email in emails:
            f.write(email + '\n')

if __name__ == "__main__":
    pull_numbers('potential_contacts.txt', 'numbers.txt')
    pull_emails('potential_contacts.txt', 'emails.txt')


# with open('notes.txt', 'w+') as f:
#     f.write(content)
