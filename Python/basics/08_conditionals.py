#Conditionals
#age = 15

# if age >= 18:
    #print("You are an adult.")
#else:
    #print("You are a minor.")
#print()

#TASK 2 - elif
#age = 65
#if age < 13:
    #print("You are a child.")
#elif age < 18:
    #print("You are a teenager.")
#elif age < 60:
    #print("You are an adult.")
#else:
    #print("You are a senior.")
#print()

#TASK 3 - Conditionals with input()
#age = int(input("Enter your age: "))
#if age < 13:
    #print("You are a child.")
#elif age < 18:
    #print("You are a teenager.")
#elif age < 60:
    #print("You are an adult.") 
#else:
    #print("You are a senior.")
    
#AFTER REVISION: TASK 1
#CONDITIONAL PRACTICE
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")
    print()

    #example
name = input("Enter your name: ")
if name == "":
    print("You didn't enter a name!")

    print("Program continues here...")
    print()
print()

#and / or
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")
if age >= 18 and has_id == "yes":
    print("Access granted.")
elif age >= 18 and has_id == "no":
    print("You need an ID.")
else:
    print("Access denied. You are underage.")
    print()

#Example (using or)
age = 16
has_id = "yes"

if age >= 18 or has_id == "yes":
    print("Access granted.")
else:
    print("Access denied.")

