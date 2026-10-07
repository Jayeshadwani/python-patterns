class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"Person(name='{self.name}')"


person = Person("Jayesh")

print(person)
print(repr(person))