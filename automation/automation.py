from faker import Faker


fake = Faker('en_US')

# print(fake)
# print(fake.name())
print(fake.email())
print(fake.phone_number())



