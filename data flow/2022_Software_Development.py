import csv

def new_member():
    first_names = input("GIVE ME UR FIRST NAME: ")
    surnames = input("GIVE ME UR LAST NAME: ")
    categories = input("JUNIOR, ADULT, OR SENIOR: ") 
    passwords = input("GIVE ME UR PASSWORD: ")
    return first_names, surnames, categories, passwords 
     
def read_file (first_names, surnames, categories, passwords):
    with open("data flow/members.csv", "r") as file:   
        first_names = []
        surnames = []
        categories = []
        passwords = []
        reader = csv.reader(file)
        next(reader)
        for row in reader: 
            first_names.append(row[0])
            surnames.append(row[1])
            categories.append(row[2])
            passwords.append(row[3])
    return categories

def total_members (categories):
    search = input("What membership to count? ")
    counter = 0
    for x in range(len(categories)):
        if categories[x].lower() == search.lower():
            counter = counter + 1
    print(counter)


def valid_password():
    

globalnames, globalsurnames, globalcategories, globalpasswords = new_member()
globalcategories = read_file(globalnames, globalsurnames, globalcategories, globalpasswords)
total_members(globalcategories)