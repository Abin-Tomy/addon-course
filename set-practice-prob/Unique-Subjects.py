subjects = set()

def add_subject(subject):
    subjects.add(subject)
    print(f"\n{subject} has been added to the subjects list.")

def remove_subject(subject):
    if subject in subjects:
        subjects.remove(subject)
        print(f"\n{subject} has been removed from the subjects list.")
    else:
        print(f"\n{subject} was not found in the subjects list.")

def display_subjects():
    if subjects:
        print("\nList of all subjects:")
        for subject in subjects:
            print(subject)
    else:
        print("\nNo subjects in the list.")

def total_subjects():
    print(f"\nTotal number of unique subjects: {len(subjects)}")


while True:
    print("Subject Management System")
    print("1. Add a subject")
    print("2. Remove a subject")
    print("3. Display all subjects")
    print("4. Show total number of subjects")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        subject = input("Enter subject name to add: ")
        add_subject(subject)
    
    elif choice == '2':
        subject = input("Enter subject name to remove: ")
        remove_subject(subject)
    
    elif choice == '3':
        display_subjects()
    
    elif choice == '4':
        total_subjects()
    
    elif choice == '5':
        print("\nExiting program. Goodbye!")
        break
    
    else:
        print("\nInvalid choice. Please try again.")
