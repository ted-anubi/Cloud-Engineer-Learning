# PROBLEM 1
number = int(input("Enter a number: "))
if number > 100 :
    print("High")
elif 50 <= number <= 100:
    print("Medium")
else:
    print("Low")
    print()

#PROBLEM 2
for number in range(2, 21, 2):
    print(number)
    print()

#PROBLEM 3
while True:              #means loop forever
    password = input("Enter password: ")
    if password == "python123":
        print("Access granted.")
        break
    else:
        print("Wrong password. Try again.")