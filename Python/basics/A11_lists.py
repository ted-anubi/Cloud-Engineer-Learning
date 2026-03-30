#Lists
cities = ["Mombasa", "Nairobi", "Kisumu"]
print(cities[0])
print(cities[1])
print(cities[2])
print()

#List Methods
cities.append("Eldoret")      #adds to the end
print(cities)
print()

cities.remove("Kisumu")       #removes by value
print(cities)
print()

print(len(cities))            #counts items
print()

#loop through list
for city in cities:
    print(city)
    print()

#Index and returns(pop)
hosts = ["kca", "zetech", "jkuat"]
removed = hosts.pop(2)
print(removed)
print(hosts)
print()

#.sort() - sorts a list in place
hosts = ["web03", "web01", "web02"]
hosts.sort()
print(hosts)
print()