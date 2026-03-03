import csv


# opens tools.csv, adds parallel arrays and returns them
def readFromFile():
    with open("Courseworks Databases/Coursework 2026/Coursework 2026/Software/tools.csv", "r") as file:
        tools = []
        manufacturers = []
        dateRented = []
        returned = []
        fees = []
        reader = csv.reader(file)
        for row in reader:
            tools.append(row[0])
            manufacturers.append(row[1])
            dateRented.append(row[2])
            returned.append(row[3])
            fees.append(int(row[4]))
    return tools, manufacturers, dateRented, returned, fees


# finds and displays name of each tool and total number of tools by a chosen manufacturer
def findChosenTools(tools, manufacturers):
    found = False
    counter = 0
    chosenManufacturer = input("Enter a manufacturer: ")
    arraySize = len(manufacturers)
    while counter < arraySize and not found:
        if manufacturers[counter] == chosenManufacturer:
            found = True
            print(tools[counter])
        else:
            counter += 1
    if found:
        print("Total: " + str(counter))
                

# calculates late fees 
def calculateLateFee(dateRented, returned, fees):
    for x in range(len(dateRented)):
        if dateRented[x][6:10] == "2025" and returned[x] == "No": # if characters from index 6 to 10 in dateRented are equal to 2025
            if 1 < int(dateRented[x][3:5]) < 6: # if characters from index 3 to 5 in dateRented is bigger than 1 and smaller than 6
                fees[x] += 10
            else:
                fees[x] += 5
    return fees


# writes tool name, date rented and fee of any tool with a late fee to lateTools.csv
def writeLateTools(tools, dateRented, fees):
    with open("lateTools.csv", "w") as file:
        for x in range(len(tools)):
            if fees[x] != 0:
                file.write(tools[x] + ", " + dateRented[x] + ", " + str(fees[x]) + '\n')


# main program
tools, manufacturers, dateRented, returned, fees = readFromFile()
findChosenTools(tools, manufacturers)
calculateLateFee(dateRented, returned, fees)
writeLateTools(tools, dateRented, fees)