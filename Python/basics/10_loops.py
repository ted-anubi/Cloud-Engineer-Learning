# FOR LOOPS
#for i in range(5):
    #print(i)

#range with start and stop
#for i in range(1,6):
    #print(i)

#Looping over a list
certs = ["CLF-CO2", "Linux+", "SAA-CO3", "Terraform", "CKA"]

for cert in certs:
    print(f"Studying: {cert}")
print()

#While loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
print()

#break and continue
for i in range(1, 11):
    if i == 6:
        break
    print(i)

#Continue
for i in range(1, 11):
    if i == 6:
        continue
    print(i)
print()

#Example
for i in range(2, 10, 2):
    print(i)
    