from Pet import Pet

pets = []
pets.append(Pet("princess", "cat", 2, 7))

def menu():
    print("🐛🐛🐛🐛🐛🐛🐛🐛")
    print("1. Add pet")
    print("2. View all pets 🐶")
    print("3. Search pet")
    print("4. Feed pet 🍓")
    print("5. Exit")
    print("🐛🐛🐛🐛🐛🐛🐛🐛")
    option = ""


    while option != "5":
        option = input("")
        if option == "1":
            getName = input("Enter name: ")
            getType = input("Enter animal type: ")
            getAge = int(input("Enter age: "))
            getHunger = int(input("Enter hunger: "))
            myPet = Pet(getName, getType, getAge, getHunger)
            pets.append(myPet)


        if option == "2":
            for x in range (len(pets)):
                pets[x].showPet()
        

        if option == "3":
            searchPet = input("What pet? ")
            for x in range (len(pets)):
                if searchPet == pets[x].name:
                    pets[x].showPet()
        

        if option == "4":
            searchPet = input("What pet do you want to feed? ")
            for x in range (len(pets)):
                if searchPet == pets[x].name:
                    pets[x].feed()
                    pets[x].showPet()


menu() 