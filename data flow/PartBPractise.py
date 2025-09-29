import csv

class Order:
     def __init__(self, name, product, amount_spent):
          self.name = name
          self.product = product
          self.amount_spent = amount_spent

def readOrders():
    orders = []
    with open("data flow/orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
             newOrder = Order(row[0], row[1], float(row[2]))
             orders.append(newOrder)
   
    return orders

def findMaxOrder(orders):
     maxOrder = orders[0]
     for order in orders:
          if "TV" in order.name and order.price > maxOrder:
               maxOrder = order
     print(maxOrder)

orders = readOrders()
findMaxOrder(orders)