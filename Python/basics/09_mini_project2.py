#CLOUD ACCESS CONTROL SYSTEM
username = input("Enter your username: ")
age = int(input("Enter your age: "))
access_level = int(input("Enter your access level: "))


print("=" * 35)
print("  CLOUD ACCESS CONTROL SYSTEM  ")
print("=" * 35)
print(f"Username: {username}")
print(f"Age: {age}")
if age < 18:
    print("Status: Access denied: You must be 18 or older")
elif access_level == 1:
    print("Status: Access granted: Read only")
elif access_level == 2:
    print("Status: Access granted: Read and Write")
elif access_level == 3:
    print("Status: Access granted: Full Admin")
else:
    print("Status: Invalid access level")
print("=" * 35)