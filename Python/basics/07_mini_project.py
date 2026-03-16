#Personal Profile card
Name = input("Enter your name: ")
Age = input("Enter your age: ")
City = input("Enter your city: ")
Career_Goal = input("Enter your career goal: ")
Current_year = 2026
print()

#Display a clean formatted profile card using f-strings
print("=" * 22)
print("   PROFILE CARD   ")
print("=" * 22)
print(f"""
Name: {Name.title()}
City: {City.upper()}
Goal: {Career_Goal}
Name length: {len(Name)} characters
Experience length: {int(Current_year) + 10}
    """)
print("=" * 22)
print()
