import random
import datetime
import time
import csv
import json
import os

LOG_FILE = "logs.txt"
LOG_LEVELS = ["INFO", "WARNING", "ERROR"]
MESSAGES = [
    "Application started",
    "Low memory warning",
    "Database connection failed",
    "User logged in",
    "File not found",
    "Network timeout",
    "Disk space running low",
    "Unauthorized access attempt"
]


# Function to generate a log entry
def generate_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(LOG_LEVELS)
    message = random.choice(MESSAGES)
    log_entry = f"{timestamp} [{level}] {message}"

    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

    print("New log entry added!")


# View all logs
def view_logs():
    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    if logs:
        print("\n--- Log Entries ---")
        for log in logs:
            print(log.strip())
          
    else:
        print("No logs found.")


# Filter logs by level
def filter_logs_by_level():
    level = input("Enter log level (INFO, WARNING, ERROR): ").strip().upper()
    if level not in LOG_LEVELS:
        print("Invalid log level!")
        return

    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return

    with open(LOG_FILE, "r") as file:
        filtered_logs = [line.strip() for line in file if f"[{level}]" in line]

    if filtered_logs:
        print(f"\n--- {level} Logs ---")
        for log in filtered_logs:
            print(log)
          
    else:
        print(f"No {level} logs found.")


# Advanced filtering by level and date
def advanced_filter():
    levels_input = input("Enter levels (comma-separated, e.g., INFO,ERROR): ").upper().split(",")
    start_date = input("Start date (YYYY-MM-DD) or leave blank: ")
    end_date = input("End date (YYYY-MM-DD) or leave blank: ")

    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    filtered = []
    for log in logs:
        for level in levels_input:
            if f"[{level.strip()}]" in log:
                timestamp_str = log.split()[0]  # Get date part
                if (not start_date or timestamp_str >= start_date) and (not end_date or timestamp_str <= end_date):
                    filtered.append(log.strip())

    if filtered:
        print("\n--- Filtered Logs ---")
        for log in filtered:
            print(log)
          
    else:
        print("No matching logs found.")


# Real-time log monitor
def real_time_monitoring():
    print("\n--- Real-Time Log Monitor --- (Ctrl+C to stop)")
    try:
        with open(LOG_FILE, "r") as f:
            f.seek(0, 2)
            while True:
                line = f.readline()
                if line:
                    print(line.strip())
                  
                else:
                    time.sleep(1)
                  
    except KeyboardInterrupt:
        print("\nStopped real-time monitoring.")


# Search logs by keyword
def search_logs():
    keyword = input("Enter keyword to search in logs: ").strip().lower()

    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return

    with open(LOG_FILE, "r") as f:
        logs = [line.strip() for line in f if keyword in line.lower()]

    if logs:
        print(f"\n--- Logs containing '{keyword}' ---")
        for log in logs:
            print(log)
          
    else:
        print(f"No logs found containing '{keyword}'.")


# Log statistics
def log_statistics():
    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    if not logs:
        print("No logs found to analyze.")
        return

    total_logs = len(logs)
    level_counts = {level: 0 for level in LOG_LEVELS}

    for log in logs:
        for level in LOG_LEVELS:
            if f"[{level}]" in log:
                level_counts[level] += 1

    most_recent_log = logs[-1].strip()

    print("\n--- Log Statistics ---")
    print(f"Total logs: {total_logs}")
    for level, count in level_counts.items():
        print(f"{level} logs: {count}")
    print(f"Most recent log: {most_recent_log}")


# Export logs to CSV or JSON
def export_logs():
    format = input("Export format (csv/json): ").strip().lower()
    if format not in ["csv", "json"]:
        print("Invalid format!")
        return

    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return

    with open(LOG_FILE, "r") as f:
        logs = [line.strip() for line in f]

    if format == "csv":
        with open("logs_export.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Timestamp", "Level", "Message"])
          
            for log in logs:
                timestamp, level_msg = log.split(" [", 1)
                level, message = level_msg.split("] ", 1)
                writer.writerow([timestamp, level, message])
              
        print("Logs exported to logs_export.csv")

    elif format == "json":
        log_data = []
        for log in logs:
            timestamp, level_msg = log.split(" [", 1)
            level, message = level_msg.split("] ", 1)
            log_data.append({"timestamp": timestamp, "level": level, "message": message})
          
        with open("logs_export.json", "w") as jsonfile:
            json.dump(log_data, jsonfile, indent=4)
        print("Logs exported to logs_export.json")


# User choices
def user_choice(choice):
    if choice == "1":
        generate_log()
      
    elif choice == "2":
        view_logs()
      
    elif choice == "3":
        filter_logs_by_level()
      
    elif choice == "4":
        search_logs()
      
    elif choice == "5":
        log_statistics()
      
    elif choice == "6":
        advanced_filter()
      
    elif choice == "7":
        real_time_monitoring()
      
    elif choice == "8":
        export_logs()
      
    elif choice == "9":
        print("Exiting... Goodbye!")
        return True
      
    else:
        print("Invalid choice! Try again.")
      
    return False


# Main menu
if __name__ == "__main__":
    while True:
        print("\nLog File Parser")
        print("1. Generate a new log entry")
        print("2. View all logs")
        print("3. Filter logs by level")
        print("4. Search logs by keyword")
        print("5. View log statistics")
        print("6. Advanced filter (level + date)")
        print("7. Real-time log monitor")
        print("8. Export logs (CSV/JSON)")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()
        if user_choice(choice):
            break
