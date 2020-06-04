# from faker import Faker


# fake = Faker('en_US')

# print(fake)
# print(fake.name())
# print(fake.email())
# print(fake.phone_number())


# content = ''
# for _ in range(10): #one argument = stop at
#     content += fake.paragraph()
#     content += fake.email()
#     content += fake.paragraph()
#     content += fake.phone_number()
#     content += fake.paragraph()
# content+= '\n'
# print(content)


# with open('notes.txt', 'w+') as f:
#     f.write(content)

import re

def pull_numbers(original, new):
    """takes in 2 files as arguments, one origional file to read from and a new file to print to then pulls phone numbers from origional"""
    with open(original) as contents:
        contents = contents.read()

        # re_dash = r'\d\d\d-\d\d\d-\d\d\d\d'
        # re_paren = r'\(\d\d\d\)\d\d\d-\d\d\d\d'
        # re_dot = r'\d\d\d\.\d\d\d\.\d\d\d\d'
        # re_area_dash = r'\d\d\d-\d\d\d\d'
        # re_area_dot = r'\d\d\d\.\d\d\d\d'

        ten_digits = re.findall(r'\d{3}.\d{3}.\d{4}', contents)
        erase_paren_dot = [num.replace(')', "-") for num in ten_digits]
        erase_dot = [num.replace('.', '-') for num in erase_paren_dot]

    with open(new, 'w+') as f:
        for num in erase_dot:
            f.write(num + '\n')


if __name__ == "__main__":
    pull_numbers('potential_contacts.txt', 'notes.txt')

# with open('notes.txt', 'w+') as f:
#     f.write(content)
