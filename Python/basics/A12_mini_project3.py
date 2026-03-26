#HOST INVENTORY TOOL
#Skills: Lists, loops, Conditionals, input, f-strings

hosts = []

while True:
    print("\n--- Host Inventory ---")
    print("1. Add host")
    print("2. View inventory")
    print("3. Remove host")
    print("4. Quit")

    choice = input("Select option: ")

    if choice == "1":
        print("Add host selected")
    elif choice == "2":
        print("View inventory selected")
    elif choice == "3":
        print("Remove host selected")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.Try again.")
