import csv 

# opens attractions.csv, adds parallel arrays and returns them.
def read_file():
    with open("data flow/attractions.csv", "r") as file:
        attractions = []
        categories = []
        visitors = []
        daysOpen = []
        height = []
    return attractions, categories, visitors, daysOpen, height

# Finds and displays least visited attractions.
def least_attract(attractions, visitors):
     minimum_value = visitors[0] 
     for x in range(1, len(visitors)):
         if visitors[x] < minimum_value: 
             minimum_value = visitors[x] 

# Finds and displays most visited attractions.
def most_attract(attractions, visitors):
     maximum_value = visitors[0] 
     for x in range(1, len(visitors)):
         if visitors[x] > maximum_value: 
             maximum_value = visitors[x] 


# main program
globalattractions, globalcategories, globalvisitors, globaldays, globalheight = read_file
least_attract(globalattractions, globalvisitors)
most_attract(globalattractions, globalvisitors)