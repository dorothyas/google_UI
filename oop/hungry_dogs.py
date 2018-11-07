class Pets:
    def __init__(self, dogs):
        self.dogs = dogs
class Dog:
    species = 'mammals'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry= True
    def eat(self):
        self.is_hungry= False

Tom =  Dog("Tom", 6)
Fletcher=  Dog("Fletcher", 7)    
Larry = Dog("Larry", 9)
all_dogs = [Tom, Fletcher,Larry]
all_pets = Pets(all_dogs)

print ("I have %d dogs." % (len(all_pets.dogs)))

for dog in all_pets.dogs:
    print("%s is %s" % (dog.name, dog.age))
print("And they're all %s of course." %dog.species)
hungry_dogs = False
for dog in all_pets.dogs:
    if dog.is_hungry:
        hungry_dogs = True

if hungry_dogs:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")