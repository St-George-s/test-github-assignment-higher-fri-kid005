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
        pass


# main program
globalsightings = readDataFromFile()