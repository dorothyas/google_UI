class Pets:
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs
class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def eat(self):
        self.is_hungry = False

my_dogs = [
    Dog("Tom", 6), 
    Dog("Fletcher", 7), 
    Dog("Larry", 9)
]
my_pets = Pets(my_dogs)
print("I have {} dogs.".format(len(my_pets.dogs)))

for dog in my_pets.dogs:
    dog.eat()

print("{} is {}.".format(dog.name, dog.age))
print("And they're all {}s, of course.".format(dog.species))

are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")