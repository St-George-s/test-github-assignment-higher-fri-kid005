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


# function that changes lower case first letters to upper case
def upperString(word):
    firstChar = word[0]
    if ord(firstChar) >= 97 and ord(firstChar) <= 122:
        firstChar = firstChar.upper
    print(firstChar, word[1:])
    return firstChar, word[1:]


# finds and displays dates of sightings of a mammal in a specific town
def displayDates(sightings):
    town = input("Enter town: ")
    upperString("")
    mammal = input("Enter mammal: ")
    upperString("")
    print("The dates of the sightings were: ") 
    for x in range(len(sightings)):
        if sightings[x].town == upperString and sightings[x].mammal == upperString:
            print(sightings[x].date)
    

# # counts and displays number of sightings for each date in the text file
def countSightDates(sightings):
    dayToCount = sightings[0].date
    counter = 1
    for index in range(len(sightings[counter:])):
        if sightings[index].date == dayToCount:
            counter += 1
        else: 
            print(dayToCount, counter)
            dayToCount = sightings[index].date
            counter += 1
    print(dayToCount, counter)



# main program
globalsightings = readDataFromFile()
findOldest(globalsightings)
globalWord = input("Enter a town or mammal: ")
upperString(globalWord)
countSightDates(globalsightings)