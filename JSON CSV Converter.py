import csv
import json
import os

# ---------------------------- Utility Functions -----------------------------

def read_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
          
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


def read_json(file_path):
    try:
        with open(file_path, mode='r') as file:
            return json.load(file)
          
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


def write_csv(file_path, data):
    try:
        if not data:
            print("Error: No data to write to CSV.")
            return False

        fieldnames = data[0].keys()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
      
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        return False


def write_json(file_path, data):
    try:
        with open(file_path, mode='w') as file:
            json.dump(data, file, indent=4)
        return True
      
    except Exception as e:
        print(f"Error writing JSON file: {e}")
        return False


# ------------------------ Advanced Conversion Logic -------------------------

def flatten_json(y):
    out = {}
  
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
              
        elif type(x) is list:
            for i, a in enumerate(x):
                flatten(a, name + str(i) + '_')
              
        else:
            out[name[:-1]] = x
          
    flatten(y)
    return out


def json_to_csv():
    json_file = input("Enter input JSON file path: ").strip()
    csv_file = input("Enter output CSV file path: ").strip()

    data = read_json(json_file)
    if not isinstance(data, list):
        data = [data]  # Ensure the data is a list of records

    try:
        flat_data = [flatten_json(d) for d in data if isinstance(d, dict)]
      
    except Exception as e:
        print(f"Error flattening JSON data: {e}")
        return

    if flat_data and write_csv(csv_file, flat_data):
        print(f"Successfully converted '{json_file}' to '{csv_file}'")


def csv_to_json():
    csv_file = input("Enter input CSV file path: ").strip()
    json_file = input("Enter output JSON file path: ").strip()

    data = read_csv(csv_file)
    if data:
        try:
            if write_json(json_file, data):
                print(f"Successfully converted '{csv_file}' to '{json_file}'")
              
        except Exception as e:
            print(f"Error writing JSON file: {e}")


# ----------------------------- Main Program ----------------------------------

if __name__ == "__main__":
    print("Welcome to JSON CSV Converter!\n")
  
    while True:
        print("JSON CSV Converter")
        print("1. Convert CSV to JSON")
        print("2. Convert JSON to CSV")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1-3): "))
          
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        if choice == 1:
            csv_to_json()
          
        elif choice == 2:
            json_to_csv()
          
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
          
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
