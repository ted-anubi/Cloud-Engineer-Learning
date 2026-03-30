#Lists and Conditionals
numbers = [5, 12, 3, 8, 19, 7]
for number in numbers:
    if number > 7:
        print(number)
        print()

#.sort() & sorted()
hosts = ["campus01", "campus03", "campus02", "campus04"]
hosts.sort()
print(hosts)
print()

hosts = ["campus01", "campus03", "campus02", "campus04"]
new_list =sorted(hosts)
print(new_list)
print(hosts)
print()

#. index()
hosts = ["web01", "web02", "web03", "web04"]
hosts.index("web02")
print(hosts.index("web02"))
print()

try:
    print(hosts.index("web05"))
except ValueError:
    print("Host not found")
