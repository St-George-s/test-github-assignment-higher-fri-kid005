from Pet import Pet

pets = []


def menu():
    print("1. Add pet")
    print("2. View all pets")
    print("3. Search pet")
    print("4. Feed pet")
    print("5. Exit")

    option = input("")

    if option == "1":
        getName = input("Enter name: ")
        getType = input("Enter animal type: ")
        getAge = int(input("Enter age: "))
        getHunger = int(input("Enter hunger: "))
        myPet = Pet(getName, getType, getAge, getHunger)
        pets.append(myPet)

    if option == 2:
        showPet()

menu() 