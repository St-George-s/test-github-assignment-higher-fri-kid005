import csv

# Record
class Order:
     def __init__(self, customerID, name, product, amount_spent, category):
          self.customerID = customerID
          self.name = name
          self.product = product
          self.amount_spent = amount_spent
          self.category = category


# Function that reads data from the CSV file into an array of records.
def readOrders():
    orders = []
    with open("Software/ordersExtended.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
             newOrder = Order(int(row[0]), row[1], row[2], float(row[3]), row[4])
             orders.append(newOrder)   
    return orders


# Procedure that finds the maximum price spent on a TV purchase.
def findMaxOrder(orders):
     maxOrder = orders[0]
     for order in orders:
          if "TV" in order.product and order.amount_spent > maxOrder.amount_spent:
               maxOrder = order
     print(maxOrder.amount_spent)


# Procedure that gives every 5th customer a discount code and writes it to a text file. 
def discount(orders):
     with open("Software/Records/discounts.txt", "w") as file:
          for order in orders:
               productName = order.product[0:3]
               if order.customerID % 5 == 0: # cif it's divisible by 5. 
                    file.write(str(order.customerID) + " - " + productName + " - DISCOUNT CODE ASSIGNED")
               else:
                    file.write(str(order.customerID) + " - " + productName + " - NO DISCOUNT")
               file.write("\n") # puts on new line

# main program
orders = readOrders()
findMaxOrder(orders) 
discount(orders)