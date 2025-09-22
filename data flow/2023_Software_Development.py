import csv 

# opens attractions.csv, adds parallel arrays and returns them.
def read_file():
    with open("data flow/attractions.csv", "r") as file:
        attractions = []
        categories = []
        visitors = []
        daysOpen = []
        height = []
        reader = csv.reader(file)
        for row in reader:
            attractions.append(row[0])
            categories.append(row[1])
            visitors.append(int(row[2]))
            daysOpen.append(int(row[3]))
            height.append(row[4])
    return attractions, categories, visitors, daysOpen, height

# Finds and displays least and most visited attractions.
def mostleast_attract(attractions, visitors):
    minimum_index = 0
    maximum_index = 0
    
    for x in range(len(visitors)):
        if visitors[x] < visitors[minimum_index]:
            minimum_index = x
        if visitors[x] > visitors[maximum_index]: 
            maximum_index = x
    
    print("Most visited attraction is " + attractions[maximum_index]) 
    print("Least visited attraction is " + attractions[minimum_index]) 
    

# Writes the names of roller coasters that need a service within 7 days.
def service(attractions, categories, daysOpen):
    # 3.1 Create ‘service.csv’ file
    with open("data flow/service.csv", "w") as file:
    # 3.2 Loop for each attraction
        for x in range(len(categories)):
            if categories[x] == "Roller Coaster":
                days = daysOpen[x]%90
                if (90 - days) <= 7:
                    file.write(attractions[x])
    

# main program
globalattractions, globalcategories, globalvisitors, globaldays, globalheight = read_file()
mostleast_attract(globalattractions, globalvisitors)
service(globalattractions, globalcategories, globaldays)