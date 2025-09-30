import csv

# Record
class Order:
     def __init__(self, name, product, amount_spent):
          self.name = name
          self.product = product
          self.amount_spent = amount_spent


# Function that reads data from the CSV file into an array of records
def readOrders():
    orders = []
    with open("data flow/orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
             newOrder = Order(row[0], row[1], float(row[2]))
             orders.append(newOrder)   
    return orders


# Procedure that finds the maximum price spent on a TV purchase
def findMaxOrder(orders):
     maxOrder = orders[0]
     for order in orders:
          if "TV" in order.product and order.amount_spent > maxOrder.amount_spent:
               maxOrder = order
     print(maxOrder.amount_spent)


# main program
orders = readOrders()
findMaxOrder(orders) 