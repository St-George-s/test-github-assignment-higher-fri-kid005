class Competitor:
    def __init__(self, name, year_group, event, seed_time):
        self.name = name
        self.year_group = year_group
        self.event = event
        self.seed_time = seed_time

c1 = Competitor("Amira", 1, "100m", 14.8)
c2 = Competitor("Beth", 3, "200m", 30.6)
c3 = Competitor("Chloe", 2, "100m", 15.2)
c4 = Competitor("Dina", 4, "200m", 28.9)

c1.seed_time = 14.5

# print(c1.name + " runs " + c1.event + " in " + str(c1.seed_time) + " seconds.")
# print(c4.name + " runs " + c4.event + " in " + str(c4.seed_time) + " seconds.")

competitors = [c1, c2, c3]
competitors.append(c4)


# print(competitors[0].event)

for index in range(len(competitors)):
    print(competitors[index].name + " is in year " + str(competitors[index].year_group) + " and runs " + competitors[index].event + " in " + str(competitors[index].seed_time) + " seconds.")

count_100 = 0
for x in range(len(competitors)):
    if competitors[x].event == "100m":
        count_100 += 1
print("100m entries: " + str(count_100))

fastest_100 = None
for x in range(len(competitors)):
    if competitors[x].event == "100m":
        if fastest_100 == None or competitors[x].seed_time < fastest_100:
            fastest_100 = competitors[x].seed_time
print("fastest 100m seed: " + str(fastest_100) + " seconds.")