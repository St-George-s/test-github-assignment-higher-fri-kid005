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
def chosenTool(tools, manufacturers):
    chosenManufacturer = input("What manufacturer would you like to search for?: ")
    found = False
    counter = 0
    for x in range(len(manufacturers)):
        while found == False:
            if manufacturers[x] == chosenManufacturer:
                




# calculates late fees
def lateFee(datesRented, returned, fees):
    for x in range(len(datesRented)):
        if datesRented[x][6:10] == "2025" and returned[x] == "No":
            if 1 < int(datesRented[x][3:5]) < 6:
                fees[x] += 10
            else:
                fees[x] += 5
    return fees


# writes tool name, date rented and fee of any tool with a late fee to lateTools.csv
def lateTools(tools, datesRented, fees):
    pass