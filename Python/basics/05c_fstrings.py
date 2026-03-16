# f strings with math
a = 10
b = 3
print(f"10 + 3 = {a + b}")
print(f"10 * 3 = {a * b}")
print(f"10 to the power of 3 = {a ** b}")

#F-strings can call string methods inside {}
name = "ted anubi"
print(f"Uppercase: {name.upper()}")
print(f"Length: {len(name)}")
print(f"First 3 letters: {name[ :3]}")

#F-strings can control decimal places
result = 10/3
print(f"Full result: {result}")
print(f"2 decimal places: {result:.2f}")
print(f"4 decimal places: {result:.4f}")
print()
print()

#Q2 Problem
name = "Ted"
years = 5
goal = 2026

print(f"{name} has {years} years to reach his goal of {2026}")