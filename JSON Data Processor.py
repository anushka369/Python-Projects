import json

FILE_NAME = "students.json"


def load_data():
    """Load student data from JSON file."""
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
          
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Unable to load data from students.json")
        return []


def view_students():
    """Display all student records in tabular format."""
    students = load_data()
    if not students:
        print("No student records found.")
        return
      
    print("\n--- Student Records ---")
    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'CGPA':<5}")
    for student in students:
        print(f"{student['id']:<5} {student['name']:<20} {student['age']:<5} {student['cgpa']:<5}")


def search_student():
    """Search student by ID or partial name."""
    students = load_data()
    query = input("Enter student ID or name to search: ").strip()

    matches = []
    if query.isdigit():
        sid = int(query)
        matches = [s for s in students if s["id"] == sid]
      
    else:
        matches = [s for s in students if query.lower() in s["name"].lower()]

    if matches:
        print("\n--- Student(s) Found ---")
        for student in matches:
            print(student)
          
    else:
        print("No student found matching your query.")


def filter_students():
    """Filter students based on CGPA or Age."""
    students = load_data()
    key = input("Enter key to filter by (cgpa/age): ").strip().lower()
    if key not in ["cgpa", "age"]:
        print("Invalid key! You can only filter by 'cgpa' or 'age'.")
        return

    operator = input("Enter condition operator (>, <, >=, <=, ==): ").strip()
    try:
        if key == "cgpa":
            value = float(input(f"Enter {key}: ").strip()) 
          
        else:
            int(input(f"Enter {key}: ").strip())
      
    except ValueError:
        print("Invalid value entered.")
        return

    filtered = [s for s in students if eval(f"s['{key}'] {operator} {value}")]

    if filtered:
        print(f"\n--- Students with {key} {operator} {value} ---")
        for student in filtered:
            print(student)
          
    else:
        print(f"No students found with {key} {operator} {value}.")

def delete_student():
    """Delete a student by ID."""
    students = load_data()
  
    try:
        student_id = int(input("Enter student ID to delete: ").strip())
      
    except ValueError:
        print("Invalid ID format.")
        return

    updated = [s for s in students if s["id"] != student_id]
    if len(updated) == len(students):
        print("No student found with this ID.")
        return

    # Backup
    with open("students_backup.json", "w") as backup:
        json.dump(students, backup, indent=4)

    with open(FILE_NAME, "w") as f:
        json.dump(updated, f, indent=4)
    print(f"Student with ID {student_id} deleted successfully (backup created).")


def sort_students():
    """Sort students by name, cgpa, or age."""
    students = load_data()
    if not students:
        print("No records to sort.")
        return

    field = input("Sort by (name/cgpa/age): ").strip().lower()
    if field not in ["name", "cgpa", "age"]:
        print("Invalid field!")
        return

    sorted_students = sorted(students, key=lambda x: x[field])
    print(f"\n--- Students Sorted by {field.title()} ---")
    for s in sorted_students:
        print(s)

def update_student():
    """Update details of a student."""
    students = load_data()
  
    try:
        sid = int(input("Enter ID of student to update: ").strip())
      
    except ValueError:
        print("Invalid ID format.")
        return

    for student in students:
        if student["id"] == sid:
            name = input(f"New name ({student['name']}): ").strip() or student['name']
            age = input(f"New age ({student['age']}): ").strip()
            cgpa = input(f"New CGPA ({student['cgpa']}): ").strip()

            student["name"] = name
            if age.isdigit():
                student["age"] = int(age)
              
            if cgpa.replace('.', '', 1).isdigit():
                student["cgpa"] = float(cgpa)

            with open(FILE_NAME, "w") as f:
                json.dump(students, f, indent=4)
            print("Student record updated successfully.")
            return

    print("Student not found.")

def user_choice(choice):
    if choice == "1":
        view_students()
      
    elif choice == "2":
        search_student()
      
    elif choice == "3":
        filter_students()
      
    elif choice == "4":
        delete_student()
      
    elif choice == "5":
        sort_students()
      
    elif choice == "6":
        update_student()
      
    elif choice == "7":
        print("Exiting... Goodbye!")
        return True
      
    else:
        print("Invalid choice! Try again.")
      
    return False

if __name__ == "__main__":
    while True:
        print("\nJSON Data Processor - Student Records")
        print("1. View all students")
        print("2. Search student by ID or name")
        print("3. Filter students by condition")
        print("4. Delete a student")
        print("5. Sort student records")
        print("6. Update student details")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()
        if user_choice(choice):
            break
