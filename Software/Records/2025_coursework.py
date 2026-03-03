import csv 

class Order():
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost
        self.rating = rating


# read from file into array of records
def readFromFile():
    orders = []
    with open("Software/Records/orders.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            newOrder = Order(row[0], row[1], row[2], row[3], float(row[4]), int(row[5]))
            orders.append(newOrder)
        return orders


# find the position of the customer who gave the first 5-star rating
def ratingPosition(orders):
    position = -1
    index = 0
    month = input("Enter a month to search for: ")
    while position == -1 and index < len(orders):
        if orders[index].date[3:6] == month and orders[index].rating == 5:
            position = index
        index += 1
    return position


# write details of winning customer to a text file
def winningDetails(orders, position):
    with open("winningCustomer.txt", "w") as file:
        if position >= 0:
            file.write(orders[position].orderNum + " ")
            file.write(orders[position].email + " ")
            file.write(str(orders[position].cost))
        else:
            file.write("No winner")


def countOption(orders, status):
    counter = 0
    for item in orders:
        if item.option == status:
            counter += 1
    return counter



# display total number of orders delievered and collected
def totalOrders(orders):
    count = countOption(orders, "Delivered")
    count = countOption(orders, "Collected")


# main program
orders = readFromFile()
position = ratingPosition(orders)
winningDetails(orders, position)
totalOrders(orders)