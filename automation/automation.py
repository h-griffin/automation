from faker import Faker


fake = Faker('en_US')

# print(fake)
# print(fake.name())
print(fake.email())
print(fake.phone_number())


content = ''
for _ in range(10): #one argument = stop at
    content += fake.paragraph()
    content += fake.email()
    content += fake.paragraph()
    content += fake.phone_number()
    content += fake.paragraph()
content+= '\n'
print(content)


with open('notes.txt', 'w+') as f:
    f.write(content)
