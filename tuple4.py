from collections import namedtuple

Person = namedtuple("Person", ["first_name", "last_name", "license_plate"])

person_data = Person(input(), input(), input())

print("First name: " + person_data.first_name)
print("Last name: " + person_data.last_name)
print("License plate: " + person_data.license_plate)