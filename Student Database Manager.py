FILE_NAME = "students.txt"

# Load records into memory on startup
def load_records():
    records = []
  
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.strip():
                    records.append(line.strip().split(","))
                  
    except FileNotFoundError:
        open(FILE_NAME, "w").close()
    return records


# Save records from memory to file
def save_records(records):
    with open(FILE_NAME, "w") as file:
        for record in records:
            file.write(",".join(record) + "\n")


# Display table header
def display_header():
    print("\nRoll Number\tName\tAge\tCourse\tDepartment")


# Add a student
def add_student(records):
    student_id = input("Enter Roll Number (numeric): ").strip()
    if not student_id.isdigit():
        print("❌ Invalid Roll Number. Use digits only.")
        return

    for record in records:
        if record[0] == student_id:
            print("⚠️ Roll Number already exists.")
            return

    name = input("Enter Name: ").strip()
    if not name.isalpha():
        print("❌ Name must contain alphabets only.")
        return

    age = input("Enter Age (<=100): ").strip()
    if not age.isdigit() or int(age) > 100:
        print("❌ Invalid Age.")
        return

    course = input("Enter Course: ").strip()
    department = input("Enter Department: ").strip()

    records.append([student_id, name, age, course, department])
    print("✅ Student added successfully!")


# View all students
def view_students(records):
    if not records:
        print("📂 No records found.")
        return
    display_header()
  
    for record in records:
        print("\t\t".join(record))


# Search with partial name, roll number or department
def search_student(records):
    query = input("Enter Name / Roll Number / Department: ").strip().lower()
    matches = [
        r for r in records
        if query in r[0].lower() or query in r[1].lower() or query in r[4].lower()
    ]

    if matches:
        print("\n🔍 Matching Records:")
        display_header()
        for r in matches:
            print("\t\t".join(r))
          
    else:
        print("⚠️ No matching student found.")


# Update a student
def update_student(records):
    student_id = input("Enter Roll Number to update: ").strip()
    for i, record in enumerate(records):
      
        if record[0] == student_id:
            print("Leave blank to keep existing value.")
            new_name = input(f"New Name ({record[1]}): ").strip() or record[1]
            new_age = input(f"New Age ({record[2]}): ").strip() or record[2]
            new_course = input(f"New Course ({record[3]}): ").strip() or record[3]
            new_dept = input(f"New Department ({record[4]}): ").strip() or record[4]

            if not new_name.isalpha():
                print("❌ Invalid Name.")
                return
              
            if not new_age.isdigit() or int(new_age) > 100:
                print("❌ Invalid Age.")
                return

            records[i] = [student_id, new_name, new_age, new_course, new_dept]
            print("✅ Student updated successfully!")
            return
          
    print("❌ Student not found.")


# Delete a student
def delete_student(records):
    student_id = input("Enter Roll Number to delete: ").strip()
    for i, record in enumerate(records):
        if record[0] == student_id:
            confirm = input(f"Are you sure you want to delete {record[1]}? (y/n): ").strip().lower()
          
            if confirm == "y":
                records.pop(i)
                print("🗑️ Student deleted.")
              
            else:
                print("❎ Deletion cancelled.")
            return
          
    print("❌ Student not found.")


# Main interface
def main():
    records = load_records()

    while True:
        print("\n🎓 Student Database Manager")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            add_student(records)
          
        elif choice == "2":
            view_students(records)
          
        elif choice == "3":
            search_student(records)
          
        elif choice == "4":
            update_student(records)
          
        elif choice == "5":
            delete_student(records)
          
        elif choice == "6":
            save_records(records)
            print("💾 Records saved. Goodbye!")
            break
          
        else:
            print("⚠️ Invalid option. Try again.")


if __name__ == "__main__":
    main()
