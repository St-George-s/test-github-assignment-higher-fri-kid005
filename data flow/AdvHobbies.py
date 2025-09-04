import csv

# Function to read CSV file into parallel arrays 
def readFile():
    # Opens CSV file into read mode
    with open("data flow/Fun_Users.csv", "r") as file:
        name = [] # 
        hobby = []
        pokemon = []
        fallout = []
        age = []
        job = []
        reader = csv.reader(file)
        next(reader) # Skips the header row
        for row in reader:  
            name.append(row[0])
            hobby.append(row[1])
            pokemon.append(row[2])
            fallout.append(row[3])
            age.append(row[4])
            job.append(row[5])
    return pokemon, age, name, hobby, fallout, job

# Procedure that asks the user to choose a pokemon and it will count how many of those pokemon are in the array
def pokeCount(pokemon): 
    search = input("What pokemon? ")
    counter = 0
    for x in range(len(pokemon)):
        if pokemon[x] == search:
            counter = counter + 1
    print(counter)

# Procedure that finds the largest value in the age array
def findMax(age): 
     maximum_value = age[0] 
     for x in range(1, len(age)): # Check over remaining values in age
         if age[x] > maximum_value: 
             maximum_value = age[x] 
     print(f"The largest value was {maximum_value}") 

# Procedure that finds the smallest value in the age array
def findMin(age): 
     minimum_value = age[0] 
     for x in range(1, len(age)): 
         if age[x] < minimum_value: 
             minimum_value = age[x] 
     print(f"The smallest value was {minimum_value}") 

# Procedure to do a linear search based on a name and print details for any matches
def details(name, age, pokemon, hobby, fallout, job):
    find_details = input("Who do you want? ")
    for x in range(len(name)):
        if find_details == name[x]:
            print(name[x] + " is " + age[x] + " years old. Their favourite pokemon is " + pokemon[x] + ". Their hobby is " + hobby[x] + ". Their fallout favourite is " + fallout[x] + ". They are a " + job[x] + ".")

# main program
globalPokemon, globalAge, globalName, globalHobby, globalFallout, globalJob = readFile()
details(globalName, globalAge, globalPokemon, globalHobby, globalFallout, globalJob)
pokeCount(globalPokemon)
findMax(globalAge)
findMin(globalAge)
