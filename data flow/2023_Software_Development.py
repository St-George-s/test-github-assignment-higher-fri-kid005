import csv 

def read_file():
    with open("data flow/attractions.csv", "r") as file:
        attractions = []
        categories = []
        visitors = []
        daysOpen = []
        height = []
    return attractions, categories, visitors, daysOpen, height

def vistited_attract(attraction, visitors):
    