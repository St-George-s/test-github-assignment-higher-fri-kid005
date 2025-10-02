import csv


# reads data from games.csv into parallel arrays.
def readGameDatafromCSV():
    with open("class test - software/games.csv", "r") as file:
        gameTitles = []
        genres = []
        ageRatings = []
        reader = csv.reader(file)
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(int(row[2]))
    return gameTitles, genres, ageRatings


# counts how many games in a genre are suitable for players under 18 and prints the game title and the number of suitable games. 
def countSuitableGames(gameTitles, genres, ageRatings, genre_to_check):
    counter = 0
    for x in range(len(gameTitles)):
        if genres[x] == genre_to_check and ageRatings[x] < 18:
            print(gameTitles[x])
            counter += 1
    print("Total number of suitable games: " + str(counter)) 


# main program
globalgameTitles, globalgenres, globalageRatings = readGameDatafromCSV()
globalgenre_to_check = input("What genre would you like to check are suitable for players under 18? ")
countSuitableGames(globalgameTitles, globalgenres, globalageRatings, globalgenre_to_check)