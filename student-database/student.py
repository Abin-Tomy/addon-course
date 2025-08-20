student_db = {}
while True:
        print("\nStudent Database Menu:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. View All Students")
        print("5. Search Student")
        print("6. Show Total Students")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
                roll = input("Enter roll number: ")
                name = input("Enter student name: ")
                student_db[roll] = name
                print("Student added successfully.")

        elif choice == "2":
                roll = input("enter roll number to update")
                if roll in student_db:
                        name = input("enter new name")
                        student_db[roll] = name
                        print("Student details updated.")
                else:
                        print("Student not found.")
        elif choice == "3":
                roll = input("Enter roll number to remove: ")
                if roll in student_db:
                        del student_db[roll]
                        print("Student removed successfully.")
                else:
                        print("Student not found.")
        elif choice == "4":
                if student_db:
                        print("Student Database:")
                        for roll, name in student_db.items():
                                print(f"Roll No: {roll}, Name: {name}")
                else:
                        print("No students found.")
                        print("Total Students: 0")
                        print("Average Marks: N/A")
                        print("Highest Marks: N/A")
                        print("Lowest Marks: N/A")
        elif choice == "5":
                roll = input("Enter roll number to search: ")
                if roll in student_db:
                        print(f"Student found - Roll No: {roll}, Name: {student_db[roll]}")
                else:
                        print("Student not found.")
        elif choice == "6":
                print(f"Total Students: {len(student_db)}")
        elif choice == "7":
                print("Exiting...")
  
