class Pet:
    def __init__(self, name, animal_type, age, hunger):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.hunger = hunger

    
    def showPet(self):
        print("Name: " + self.name + " Type: " + self.animal_type + " Age: " + self.age + " Hunger " + self.hunger)
    

    def feed(self):
        if self.hunger != 0:
            self.hunger -= 1
            print(self.name + " has been fed.")
    

    def is_hungry(self):
        hungry = False
        if self.hunger > 5:
            hungry = True
        else:
            hungry = False
        print(hungry)
