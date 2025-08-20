shopping_cart = []

while True:
    print("\n=== Shopping Cart Menu ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Number of items in cart")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
        item = input("Enter item to add: ")
        shopping_cart.append(item)
        print(f"\nSuccess! '{item}' has been added to your cart.")
    
    elif choice == "2":
        if not shopping_cart:
            print("\nYour cart is empty!")
        else:
            item = input("Enter item to remove: ")
            if item in shopping_cart:
                shopping_cart.remove(item)
                print(f"\nSuccess! '{item}' has been removed from your cart.")
            else:
                print(f"\nError: '{item}' not found in cart.")
    
    elif choice == "3":
        if shopping_cart:
            print("\nItems in your cart:")
            for i, item in enumerate(shopping_cart, 1):
                print(f"{i}. {item}")
        else:
            print("\nYour cart is empty.")
    
    elif choice == "4":
        print(f"\nNumber of items in cart: {len(shopping_cart)}")
    
    elif choice == "5":
        print("\nThank you for shopping! Goodbye!")
        break
    
    else:
        print("\nError: Invalid choice! Please enter a number between 1 and 5.")