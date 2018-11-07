class Pets:
    def __init__(self, dogs):
        self.dogs = dogs
    def walk(self):
        for dog in self.dogs:
            print(dog.walk())
class Dog:
    species = 'mammals'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry= True
    def eat(self):
        self.is_hungry= False
    def walk(self):
        return "%s is walking!" % (self.name)

Tom =  Dog("Tom", 6)
Fletcher=  Dog("Fletcher", 7)    
Larry = Dog("Larry", 9)
all_dogs = [Tom, Fletcher,Larry]
all_pets = Pets(all_dogs)
all_pets.walk()