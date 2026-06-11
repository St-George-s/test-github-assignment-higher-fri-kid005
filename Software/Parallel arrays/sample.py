import csv

# function to get data from file into parallel arrays
def getData():
    with open("Software/Parallel arrays/athletes.csv", "r") as file:
        entryID = []
        location = []
        forename = []
        surname = []
        jumps = [] # read data into parallel arrays
        reader = csv.reader(file)
        for row in reader:
            entryID.append(row[0])
            location.append(row[1])
            forename.append(row[2])
            surname.append(row[3])
            jumps.append(int(row[4]))
    return entryID, location, forename, surname, jumps

# procedure which generates bib values and writes it into a new csv file
def generateBib(entryID, location, forename, surname):
    with open("bibValues.csv", "w") as file:
        for x in range(30):
            bibValue = forename[x][0] + surname[x] + str(ord(location[x][0])) # makes bib value first letter of forename, surname and first number of ASCII value of location
            file.write(entryID[x] + " " + bibValue + '\n')

# function that finds the highest number of jumps
def highestJump(jumps):
    maxJumps = jumps[0]
    for x in range(1, len(jumps)):
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]
    return maxJumps

# procedure that finds and displays the full name of the athletes who completed the highest number of jumps
def athleteJump(maxJumps, forename, surname, jumps):
    for x in range(30):
        if jumps[x] == maxJumps:
            print(forename[x] + " " + surname[x])

def final(location):
    countC= 0
    countI = 0
    countK = 0
    countM = 0
    for x in range(len(location)):
        if location[x] == "Coatbridge":
            countC += 1
        elif location[x] == "Inverness":
            countI += 1
        elif location[x] == "Kirkcaldy":
            countK += 1
        else:
            countM += 1
    print("Coatbridge has " + str(countC) + " finalists")
    print("Inverness has " + str(countI) + " finalists")
    print("Kirkcaldy has " + str(countK) + " finalists")
    print("Motherwell has " + str(countM) + " finalists")

# main program
entryID, location, forename, surname, jumps = getData()
generateBib(entryID, location, forename, surname)
highestJump(jumps)
maxJumps = highestJump(jumps)
athleteJump(maxJumps, forename, surname, jumps)
final(location)