import csv


# read from file into parallel arrays
def readFromFile():
    with open("Software/Parallel arrays/companies.csv", "r") as file:
        company = []
        numEmployees = []
        ceoSalary = []
        reader = csv.reader(file)
        for row in reader:
            company.append(row[0])
            numEmployees.append(int(row[1]))
            ceoSalary.append(int(row[2]))
    return company, numEmployees, ceoSalary


# returns position of the highest value in the array
def findMaxPos(ceoSalary):
    position = 0
    maxValue = ceoSalary[0]
    for x in range(len(ceoSalary)):
        if ceoSalary[x] > maxValue:
            maxValue = ceoSalary[x]
            position += 1
    return position


# find + display difference between chosen company's CEO salary and highest CEO salary
def differenceInSalary(company, ceoSalary):
    chosenCompany = input("Enter the name of the chosen company: ")
    found = False
    findMaxPos(ceoSalary)
    for x in range (len(company)):
        if company[x] == chosenCompany:
            found = True
            position = x
    if chosenCompany == company:
        

# find and display highest number of employees employed by a single company + number of companies who employ within 10% of that figure
def highestNumEmployees(numEmployees):
    pass


# main program
company, numEmployees, ceoSalary = readFromFile()
findMaxPos(ceoSalary)
differenceInSalary(company, ceoSalary)
highestNumEmployees(numEmployees)
