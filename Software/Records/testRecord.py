import csv

class Game():
    def __init__(self, gameTitle, genre, ageRating, platform):
        self.gameTitle = gameTitle
        self.genre = genre
        self.ageRating = ageRating
        self.platform = platform


def readGameDatafromCSV():
    games = []
    with open("class test - software/gamesExtended.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
             newGame = Game(row[0], row[1], int(row[2]), row[3])
             games.append(newGame)   
    return games


# counts how many games in a genre are suitable for players under 18 and prints the game title and the number of suitable games. 
def countSuitableGames(games, genre_to_check):
    counter = 0
    for x in range(len(games)):
        if games[x].genre == genre_to_check and games[x].ageRating < 18:
            print(games[x].gameTitle)
            counter += 1
    print("Total number of suitable games: " + str(counter)) 


# counts how many games that are suitable for players under 18 are available on a platform.
def countGamesAvailableOnPlatform(games, genre_to_check, platform_to_check):
    with open("class test - software/platform_suitable_games.txt", "w") as file:
        platform = input("What platform do you need your game for? ")
        counter = 0
        for x in range(len(games)):
            if games[x].genre == genre_to_check and games[x].ageRating < 18 and platform_to_check == games[x].platform:
                file.write(games[x].gameTitle + " - " + games[x].platform)
                file.write("\n")
                counter += 1
            


# main program
globalGames = readGameDatafromCSV()
globalgenre_to_check = input("What genre would you like to check are suitable for players under 18? ")
countSuitableGames(globalGames, globalgenre_to_check)
countGamesAvailableOnPlatform(globalGames, globalgenre_to_check, "PC")