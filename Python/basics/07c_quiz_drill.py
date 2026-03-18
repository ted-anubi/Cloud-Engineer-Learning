#10 QUESTIONS TO BUILD MUSCLE MEMORY
#TIER 1
#QUESTION 1
full_name = "Teddy Anubi"
city = "Nairobi"
year = 2026

#Print
print(full_name)
print(city)
print(year)
print()
print()

#QUESTION 2
name = "Teddy"
age = 35
language = 3.12

#print variable types
print(type(name))
print(type(age))
print(type(language))
print()
print()

#QUESTION 3
full_name = input("Enter your full name: ")
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(len(full_name))
print()
print()

#TIER 2
#QUESTION 4
num1 = input("Give me a number: ")
num2 = input("Give me a second number: ")
print()
print(f"{num1} + {num2} = {int(num1) + int(num2)}")
print(f"{num1} - {num2} = {int(num1) - int(num2)}")
print(f"{num1} * {num2} = {int(num1) * int(num2)}")
print(f"{num1} % {num2} = {int(num1) % int(num2)}")
print()

#QUESTION 5
Goal = "Cloud security architect"
print(f"Result: {Goal.strip().title()} | Length: {len(Goal.strip())}")
print()

#QUESTION 6
sentence = "Python is the language of the cloud"
print(f"First 6: {sentence[0:6].upper()} | last 5: {sentence[30:36].title()}")
print()

#QUESTION 7
Name = input("Enter your name: ")
Birth_Year = input("Enter your birth year: ")
Age = int(2026) - int(Birth_Year)
print()
print(f"Name: {Name}")
print(f"Birth Year: {Birth_Year}")
print(f"Age: {Age}")
print()

#QUESTION 8
Statement = input("Enter a statement: ")
print(Statement.upper())
print(Statement[::-1])
print(len(Statement))
print(Statement.upper().replace("CLOUD", "CLASSIFIED"))
print()

#QUESTION 9
Item = "Laptop"
Price = 85000
Discount = 10
Final = Price - (Price * Discount/100)

print("=" * 22)
print(f"  RECEIPT ")
print("=" * 22)
print(f"Item: {Item}")
print(f"Price: KES {Price}")
print(f"Discount: {Discount}%")
print(f"Final: KES {Final:.2f}")
print("=" * 22)
print()
print()

#QUESTION 10
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
average = (num1 + num2 + num3)/3
print()
print(f"Sum: {num1 + num2 + num3}")
print(f"Max: {max(num1, num2, num3)}")
print(f"Min: {min(num1, num2, num3)}")
print(f"average: {average:.2f}")
