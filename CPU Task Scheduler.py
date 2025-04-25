from collections import deque

class Task:
    """ Represents a Process/Task for CPU Scheduling """
    def __init__(self, name, burst_time, priority=0):
        self.name = name
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time  # Used for Round Robin
        self.start_time = None
        self.finish_time = None

    def __repr__(self):
        return f"{self.name}(burst={self.burst_time}, priority={self.priority})"


class Scheduler:
    def __init__(self):
        self.tasks = []  # List of tasks as objects

  
    def get_user_tasks(self):
        """ Takes user input to create Task objects """
        num_tasks = int(input("Enter the number of tasks: "))
      
        for i in range(num_tasks):
            name = input(f"Enter name for Task {i+1}: ")
            burst_time = int(input(f"Enter burst time for {name}: "))
            priority = int(input(f"Enter priority for {name} (lower number = higher priority): "))
            self.tasks.append(Task(name, burst_time, priority))

  
    def reset_tasks(self):
        """ Resets time variables before re-running scheduling """
        for task in self.tasks:
            task.remaining_time = task.burst_time
            task.start_time = None
            task.finish_time = None

  
    def fcfs(self):
        """ Implements First-Come, First-Serve (FCFS) Scheduling """
        print("\nRunning First-Come, First-Serve (FCFS) Scheduling:")
        current_time = 0

        for task in self.tasks:
            task.start_time = current_time
            current_time += task.burst_time
            task.finish_time = current_time
            print(f"{task.name}: start at {task.start_time}, finish at {task.finish_time}")

  
    def round_robin(self, quantum):
        """ Implements Round Robin Scheduling """
        print("\nRunning Round Robin Scheduling:")
        task_queue = deque(self.tasks)
        current_time = 0

        while task_queue:
            task = task_queue.popleft()

            if task.start_time is None:
                task.start_time = current_time

            if task.remaining_time > quantum:
                current_time += quantum
                task.remaining_time -= quantum
                task_queue.append(task)  # Re-add to queue if unfinished
              
            else:
                current_time += task.remaining_time
                task.remaining_time = 0
                task.finish_time = current_time
                print(f"{task.name}: start at {task.start_time}, finish at {task.finish_time}")

  
    def priority_scheduling(self):
        """ Implements Non-Preemptive Priority Scheduling """
        print("\nRunning Priority Scheduling:")
        tasks_sorted = sorted(self.tasks, key=lambda x: x.priority)  # Sorting tasks by priority
        current_time = 0

        for task in tasks_sorted:
            task.start_time = current_time
            current_time += task.burst_time
            task.finish_time = current_time
            print(f"{task.name} (Priority {task.priority}): start at {task.start_time}, finish at {task.finish_time}")

  
    def main(self):
        """ Menu system to allow user to select scheduling algorithm """
        while True:
            print("\nChoose a Scheduling Algorithm:")
            print("1. First-Come, First-Serve (FCFS)")
            print("2. Round Robin (RR)")
            print("3. Priority Scheduling (Non-Preemptive)")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")
            self.reset_tasks()

            if choice == "1":
                self.fcfs()
              
            elif choice == "2":
                quantum = int(input("Enter time quantum for Round Robin: "))
                self.round_robin(quantum)
              
            elif choice == "3":
                self.priority_scheduling()
              
            elif choice == "4":
                print("Exiting CPU Task Scheduler. Goodbye!")
                break
              
            else:
                print("Invalid choice! Please enter a valid option.")


# Create an instance of Scheduler and run the program
if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.get_user_tasks()
    scheduler.main()
