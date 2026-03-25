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


