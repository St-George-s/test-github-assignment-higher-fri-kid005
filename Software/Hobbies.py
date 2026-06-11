def getusername():
    username = input("What is your username? ")
    return username

def getage(uname):
    age = input(uname + " how old are you? ")
    return age
    
def gethobby(uname):
    Hobbies = []
    for x in range(10):
        hobby = input("Hobby???")
        Hobbies.append(hobby)
    return Hobbies

def counthobbies(hobbies):
    return len(hobbies)

def hobbysearch(hobbies):
    searchHobby = input("What are you looking for? ")
    for x in range(len(hobbies)):
        if searchHobby == hobbies[x]:
            return x


globalusername = getusername()
globalage = getage(globalusername)
globalhobbies = gethobby(globalusername)
globalcount = counthobbies(globalhobbies)
globgalsearch = hobbysearch(globalhobbies)
print(globalusername)
print(globalage)
print(globalhobbies)
print(globalcount)
print(globgalsearch)