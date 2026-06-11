class Clubmember:
    def __init__(self, name, year_group, club, parents_permission):
        self.name = name
        self.year_group = year_group
        self.club = club
        self.parents_permission = parents_permission

c1 = Clubmember("Lara", 12, "coding", False)
c2 = Clubmember("Sahana", 13, "maths", True)
c3 = Clubmember("Mr Walker", 9, "gaming", False)
c4 = Clubmember("Steph", 12, "coding", True)

members = [c1, c2, c3, c4]
for index in range(len(members)):
    print(members[index].name + " is in year " + str(members[index].year_group) + " and goes to " + members[index].club + " club, with" + (" parental permission." if members[index].parents_permission else "out parental permission."))
