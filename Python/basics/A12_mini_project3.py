#HOST INVENTORY TOOL - STEP 1

hosts = []
while True:
    print("\n=== Host Inventory Tool ===")
    print("1. Add host")
    print("2. View hosts")
    print("3. Quit")
    print("4. Remove host")

    choice = input("Enter a selection: ")

    if choice == "1":
        hostname = input("Enter hostname: ")
        hosts.append(hostname)
        print("Host added.")

    elif choice == "2":
        if len(hosts) == 0:
            print("No hosts yet")
        else:
            for host in hosts:
                print(host)

    elif choice == "4":
        hostname = input("Enter hostname to remove: ")
        try:
            hosts.remove(hostname)
            print("Host removed.")
        except ValueError:
            print("Host not found.")

    elif choice == "3":
        print("Goodbye.")
        break
else:
    print("Invalid option")