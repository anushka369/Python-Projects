from datetime import datetime

# Handle user choices
def userChoice(choice, tasks, completed_tasks):
    if choice == 1:
        task_name = input("Enter task name: ")
        deadline = input("Enter deadline (DD-MM-YYYY): ")
        add_task(tasks, task_name, deadline)

    elif choice == 2:
        if not tasks:
            print("No tasks available.\n")
            return
        display_tasks(tasks)
      
        try:
            task_number = int(input("Enter task number to delete: "))
            delete_task(tasks, task_number)
          
        except ValueError:
            print("Please enter a valid number!\n")

    elif choice == 3:
        display_tasks(tasks)

    elif choice == 4:
        if not tasks:
            print("No tasks available to update.\n")
            return
        display_tasks(tasks)
      
        try:
            task_number = int(input("Enter task number to update: "))
            update_task(tasks, task_number)
          
        except ValueError:
            print("Please enter a valid number!\n")

    elif choice == 5:
        if not tasks:
            print("No tasks available to mark as completed.\n")
            return
        display_tasks(tasks)
      
        try:
            task_number = int(input("Enter task number to mark as done: "))
            mark_task_completed(tasks, completed_tasks, task_number)
          
        except ValueError:
            print("Please enter a valid number!\n")

    elif choice == 6:
        display_completed_tasks(completed_tasks)

    elif choice == 7:
        return "Exiting application. Goodbye!"
    
    else:
        print("Invalid choice!\n")


# Add a new task
def add_task(tasks, task_name, deadline):
    deadline_date = validate_date(deadline)
    if deadline_date:
        tasks.append({"task": task_name, "deadline": deadline_date})
        print("Task added successfully!\n")


# Validate the date format
def validate_date(deadline):
    try:
        deadline_date = datetime.strptime(deadline, "%d-%m-%Y").date()
        return deadline_date
      
    except ValueError:
        print("Invalid date format! Try again\n")
        return None


# Display current tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return
      
    print("\nYour Tasks:")
    for index, task in enumerate(tasks):
        formatted_deadline = task['deadline'].strftime("%d-%m-%Y")
        print(f"{index+1}. {task['task']} - Deadline: {formatted_deadline}")
    print()


# Display completed tasks
def display_completed_tasks(completed_tasks):
    if not completed_tasks:
        print("No completed tasks yet.\n")
        return
      
    print("\nCompleted Tasks:")
    for index, task in enumerate(completed_tasks):
        formatted_deadline = task['deadline'].strftime("%d-%m-%Y")
        print(f"{index+1}. {task['task']} - Completed (Original Deadline: {formatted_deadline})")
    print()


# Delete a task
def delete_task(tasks, task_number):
    task_index = task_number - 1
  
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' deleted successfully!\n")
      
    else:
        print("Invalid task number!\n")


# Update a task's name or deadline
def update_task(tasks, task_number):
    task_index = task_number - 1
    if 0 <= task_index < len(tasks):
        new_name = input("Enter new task name (leave blank to keep unchanged): ")
        new_deadline = input("Enter new deadline (DD-MM-YYYY) (leave blank to keep unchanged): ")

        if new_name:
            tasks[task_index]['task'] = new_name

        if new_deadline:
            deadline_date = validate_date(new_deadline)
          
            if deadline_date:
                tasks[task_index]['deadline'] = deadline_date

        print("Task updated successfully!\n")
      
    else:
        print("Invalid task number!\n")


# Mark a task as completed
def mark_task_completed(tasks, completed_tasks, task_number):
    task_index = task_number - 1
  
    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        completed_tasks.append(completed_task)
        print(f"Task '{completed_task['task']}' marked as completed!\n")
      
    else:
        print("Invalid task number!\n")


# Main driver
if __name__ == "__main__":
    tasks = []
    completed_tasks = []

    print("Welcome to the To-Do List Application!")

    while True:
        print("Choose one operation:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Update Task")
        print("5. Mark Task as Completed")
        print("6. View Completed Tasks")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
            result = userChoice(choice, tasks, completed_tasks)
          
            if result == "Exiting application. Goodbye!":
                print(result)
                break
              
        except ValueError:
            print("Please enter a valid number!\n")
