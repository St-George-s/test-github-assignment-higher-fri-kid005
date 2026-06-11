import csv


def main():
    GetDetails()
    print("..Option 1 ..Linear search....")
    print("..Option 2 ..Print average....")
    print("..Option 3 .. ....Exit..... ..")
    ask = input("What option?: ")
    if ask == "1":
        linearSearch()
    elif ask == "2":
        Average()
    elif ask == "3":
        print("Exited.")

def linearSearch():
    counter = 0
    found = False
    ArrayName = ["Highland spring", "Geoffrey", "Ochil hills", "Organic land", "Hartziotis trading"]
    ArrayAge = ["15", "38", "13", "23", "42"]

    GetName = input("enter name for search pls: ")
    while found == False and counter <5:
        if GetName == ArrayName[counter]:
            found = True
            print(ArrayAge[counter])
        elif GetName != ArrayName[counter]:
            counter = counter + 1

def CreateFile():
    with open('users.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['name', 'age'])

def AppendFile(name, age):
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([name, age])

def GetDetails():
    usersAndAges = {}
    sumOfAge = 0
    users = int(input("How many users?"))

    for x in range(users):
        name = input("What name?")
        age = int(input("What age?"))

        while name == "":
            name = input("Name can't be blank. Enter again!!")

        while age <= 0 or age >= 120:
            age = int(input("Age unrealistic. Enter again!!"))
        
        if age <18:
            print("You are a minor!!!")
        else:
            print("You are an adult!!!")

        AppendFile(name, age)
        print("Hello " + name + ", You are " + str(age) + " years old.")


    userCount = 0
    newName = name

    while newName in usersAndAges:
            userCount = userCount + 1
            newName = name + str(userCount)


    usersAndAges[newName] = age
    print(usersAndAges)

def Average():
    sumOfAge = (age + sumOfAge)/users

    print("Total number of users are " + str(users) +
            " with an average age of " + str(sumOfAge))
main()