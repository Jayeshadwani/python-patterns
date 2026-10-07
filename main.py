print("1. main.py started")

import animals

print("2. animals imported")

from animals.dog import Dog

print("3. Dog imported")

dog = Dog()

print("4. Dog object created")

dog.bark()