import csv


class Sighting():
    def __init__(self, town, mammal, date, age):
        self.town = town
        self.mammal = mammal
        self.date = date
        self.age = age


# reads data from file
def readDataFromFile():
    sightings = []
    with open("Software/Records/mammals.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            newSight = Sighting(row[0], row[1], row[2], int(row[3]))
            sightings.append(newSight)
    return sightings


# finds and displays the age of the oldest walker
def findOldest(sightings):
    highest_age = sightings[0].age 
    for index in range(len(sightings)):
        if highest_age<sightings[index].age:
            highest_age = sightings[index].age
    print(highest_age)



# main program
globalsightings = readDataFromFile()
findOldest(globalsightings)