import csv

def readfile():
    with open("data flow/Fun_Users.csv", "r") as file:
        name = []
        hobby = []
        pokemon = []
        fallout = []
        age = []
        job = []
        reader = csv.reader(file) 
        for row in reader: 
            
            name.append(row[0])
            hobby.append(row[1])
            pokemon.append(row[2])
            fallout.append(row[3])
            age.append(row[4])
            job.append(row[5])

        print(name)
        print(hobby)
        print(pokemon)
        print(fallout)
        print(age)
        print(job)
    return pokemon


def pokecount(pokemon):
    if 


globalpokemon = readfile()
