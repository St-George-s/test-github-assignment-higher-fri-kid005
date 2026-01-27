import csv

def getData():
    with open("Software/Parallel arrays/athletes.csv", "r") as file:
        entryID = []
        location = []
        forename = []
        surname = []
        jumps = []
        reader = csv.reader(file)
        for row in reader:
            entryID.append(row[0])
            location.append(row[1])
            forename.append(row[2])
            surname.append(row[3])
            jumps.append(int(row[4]))
    return entryID, location, forename, surname, jumps



def generateBib(entryID, location, forename, surname):
    with open("bibValues.csv", "w") as file:
        for x in range(30):
            bibValue = forename[x][0] + surname[x] + str(ord(location[x][0]))
            file.write(entryID[x] + " " + bibValue + '\n')



def highestJump(jumps):
    maxJumps = jumps[0]
    for x in range(1, len(jumps)):
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]
    return maxJumps



def athleteJump(maxJumps, forename, surname, jumps):
    pass




# main program
globalEntryID, globalLocation, globalForename, globalSurname, globalJumps = getData()
generateBib(globalEntryID, globalLocation, globalForename, globalSurname)
highestJump(globalJumps)