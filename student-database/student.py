student = {}
while True:
    print("Student Database Menu")
    print("1. Add student")
    print("2. Remove student")
    print("3. View students")
    print("4. Number of students")
    print("5. search student")
    print("7. Update student")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        student[name] = age
        print(f"\nSuccess! '{name}' has been added to the database.")
    
    elif choice == "2":
        if not student:
            print("\nThe database is empty!")
        else:
            name = input("Enter student's name to remove: ")
            if name in student:
                del student[name]
                print(f"\nSuccess! '{name}' has been removed from the database.")
            else:
                print(f"\nError: '{name}' not found in the database.")
    
    elif choice == "3":
        if student:
            print("\nStudents in the database:")
            for name, age in student.items():
                print(f"Name: {name}, Age: {age}")
        else:
            print("\nThe database is empty.")
    
    elif choice == "4":
        print(f"\nNumber of students in the database: {len(student)}")
    elif choice == "5":
        if not student:
            print("\nThe database is empty!")
        else:
            name = input("Enter student's name to search: ")
            if name in student:
                print(f"\nFound: Name: {name}, Age: {student[name]}")
            else:
                print(f"\nError: '{name}' not found in the database.")
    
    elif choice == "6":
        print("\nThank you for using the Student Database! Goodbye!")
        break
    
    else:
        print("\nError: Invalid choice! Please enter a number between 1 and 5.")