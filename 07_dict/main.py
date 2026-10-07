class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Jayesh", 25)

print(person.__dict__)