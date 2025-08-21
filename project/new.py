groceries = []
while True:
    print("\n1.add \n2.remove \n3.view")
    choice =int (input("\nenter your choice:"))
    if choice == 1:
        item = input("enter item to add:")
        groceries.append(item)
        print(f"sucessfully added '{item} to the list")
    elif choice == 2:
        if not groceries:
            print("your list is empty")
        else:
            item = input("enter item to remove:")
            if item in groceries:
                groceries.remove(item)
                print(f"'{item}' removed sucessfully from the list")
            else:
                print("'{item}' item not found in your list")
    elif choice == 3:
        if groceries:
            print("Item in your list")
            for i, item in enumerate(groceries, 1):
                print(f"{i}. {item}")
            else:
                print("your list is empty")







