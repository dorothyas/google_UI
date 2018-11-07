
class Pet:
    dog=[]
    def __init__(self, dog):
        self.dog=dog

    def walk(self):
        for dog in self.dog:
            print(dog.walk())

class Dog:
    species ='mammal'
    is_hungry=True

    def __init__(self,name,age):
        self.name=name
        self.age =age
    def walk(self):
        return "{} is walking!".format(self.name)
          
my_dogs = [
    Dog("Tom", 6), 
    Dog("Fletcher", 7), 
    Dog("Larry", 9)
]

my_pets = Pet(my_dogs)

my_pets.walk()