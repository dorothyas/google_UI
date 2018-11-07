class Pets:
    def __init__(self, dogs):
        self.dogs = dogs
class Dog:
    species = 'mammals'
    def __init__(self, name, age):
        self.name = name
        self.age = age
Tom =  Dog("Tom", 6)
Fletcher=  Dog("Fletcher", 7)    
Larry = Dog("Larry", 9)
all_dogs = [Tom, Fletcher,Larry]
all_pets = Pets(all_dogs)

print ("I have %d dogs." % (len(all_pets.dogs)))

for dog in all_pets.dogs:
    print("%s is %s" % (dog.name, dog.age))
print("And they're all %s of course." %dog.species)