#truthy/falsy values
hostname = input("Enter a hostname: ")

if hostname:
    print("Valid hostname")

else:
    print("No hostname provided")

port_count = int(input("Enter port_count: "))
if port_count:
    print(f"Ports configured: {port_count}")

else:
    print("No ports configured.")