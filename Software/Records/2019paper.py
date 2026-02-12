import csv

class Member():
    def __init__(self, forename, surname, distance):
        self.forename = forename
        self.surname = surname
        self.distance = distance

# reads data from file
def readData():
    members = []
    with open("Software/Records/members.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            newMember = Member(row[0], row[1], float(row[2]))
            members.append(newMember)
        return members


# function to find the furthest distance walked by a member
def furthestDistance(members):
    furthest = members[0].distance
    for x in range(len(members)):
        if members[x].distance > furthest:
            furthest = members[x].distance
    return furthest


# procedure to display the furthest distance walked
def displayFurthest(furthest):
    print("The furthest distance walked is " + str(furthest))


# procedure to write club prize winners to file called results.txt
def writeWinnerToFile(members, furthest):
    with open("results.txt", "w") as file:
        for x in range(len(members)):
            if members[x].distance > (0.7 * furthest):
                file.write(members[x].forename)
                file.write(members[x].surname)


# main program
members = readData()
furthest = furthestDistance(members) 
displayFurthest(furthest)
writeWinnerToFile(members, furthest)