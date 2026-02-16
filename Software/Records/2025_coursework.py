import csv 

class Order():
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost
        self.rating = rating

def readFromFile():
    with open("Software/Records/orders.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            newOrder = Order(row[0])