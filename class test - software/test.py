import csv


# reads data from games.csv into parallel arrays.
def readGameDatafromCSV():
    with open("class test - software/gamesExtended.csv", "r") as file:
        gameTitles = []
        genres = []
        ageRatings = []
        platforms = []
        reader = csv.reader(file)
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(int(row[2]))
            platforms.append(row[3])
    return gameTitles, genres, ageRatings, platforms


# counts how many games in a genre are suitable for players under 18 and prints the game title and the number of suitable games. 
def countSuitableGames(gameTitles, genres, ageRatings, genre_to_check):
    counter = 0
    for x in range(len(gameTitles)):
        if genres[x] == genre_to_check and ageRatings[x] < 18:
            print(gameTitles[x])
            counter += 1
    print("Total number of suitable games: " + str(counter)) 


# counts how many games that are suitable for players under 18 are available on a platform.
def countGamesAvailableOnPlatform(gameTitles, genres, ageRatings, genre_to_check, platforms, platform_to_check):
    with open("class test - software/platform_suitable_games.txt", "w") as file:
        counter = 0
        for x in range(len(gameTitles)):
            if genres[x] == genre_to_check and ageRatings[x] < 18 and platform_to_check == platforms[x]:
                file.write(gameTitles[x] + " - " + platforms[x])
                file.write("\n")
                counter += 1
            


# main program
globalgameTitles, globalgenres, globalageRatings, globalplatforms = readGameDatafromCSV()
globalgenre_to_check = input("What genre would you like to check are suitable for players under 18? ")
globalplatform_to_check = input("What platform do you want? ")
countSuitableGames(globalgameTitles, globalgenres, globalageRatings, globalgenre_to_check)
countGamesAvailableOnPlatform(globalgameTitles, globalgenres, globalageRatings, globalgenre_to_check, globalplatforms, globalplatform_to_check)
countGamesAvailableOnPlatform(["Pokemon Go", "GTA 6"], ["Action", "Action"], [6, 18], "Action", ["Mobile", "PC"], "Mobile")