import csv
import statistics

def load_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader   = csv.DictReader(file)
            data_list = [row for row in reader]
          
        print("CSV file loaded successfully!")
        return data_list
      
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# -----------------------------------------------------------
def sort_data(data):
    if not data:
        print("No data available.")
        return

    print("\nAvailable columns:", *data[0].keys())
    inp = input("Enter column(s) to sort by (comma-separated, prefix with '-' for descending):\n> ")
    keys = []
  
    for token in inp.split(','):
        token = token.strip()
        if not token:
            continue
          
        if token.startswith('-'):
            col, rev = token[1:], True
          
        else:
            col, rev = token, False
          
        if col not in data[0]:
            print(f"  ❌ Unknown column '{col}' — skipping")
            continue
          
        # detect numeric column
        is_num = True
        for row in data:
            v = row[col].strip()
            if v == '':
                continue
              
            try:
                float(v)
              
            except:
                is_num = False
                break
              
        keys.append((col, rev, is_num))

    if not keys:
        print("No valid sort keys provided.")
        return

    def sort_key(row):
        out = []
        for col, rev, is_num in keys:
            v = row[col].strip()
            if is_num and v != '':
                out.append(float(v))
              
            else:
                out.append(v)
        return tuple(out)

    sorted_data = sorted(data, key=sort_key, reverse=False)
    for col, rev, _ in reversed(keys):
        sorted_data.sort(
            key=lambda r: (float(r[col]) if _ and r[col].strip()!='' else r[col].strip()),
            reverse=rev
        )

    print("\nSorted Data:")
    display_info(sorted_data)

# -----------------------------------------------------------
def display_info(data):
    if not data:
        print("No data available.")
        return

    headers = list(data[0].keys())
    print("\nInformation:")
    print(f"  Total Rows: {len(data)}")
    print("  Columns:", *headers)
    print("\nData:")
    print("  " + "  ".join(headers))
  
    for row in data:
        print("  " + "  ".join(row[h] for h in headers))

# -----------------------------------------------------------
def basic_statistics(data):
    if not data:
        print("No data available.")
        return

    print("\nBasic & Advanced Statistics:")
    columns = list(data[0].keys())
    for col in columns:
        # collect numeric values
        vals = []
        for row in data:
            v = row[col].strip()
          
            if v == '':
                continue
              
            try:
                vals.append(float(v))
              
            except:
                break
              
        if not vals:
            continue

        vals_sorted = sorted(vals)
        print(f"\n▶ Column: {col}")
        print(f"    Count: {len(vals)}")
        print(f"    Mean: {statistics.mean(vals):.2f}")
        print(f"    Min: {min(vals)}")
        print(f"    Max: {max(vals)}")
      
        # quartiles
        try:
            q1, q2, q3 = statistics.quantiles(vals, n=4)
            print(f"    Q1 (25th %ile): {q1}")
            print(f"    Median (50th %ile): {q2}")
            print(f"    Q3 (75th %ile): {q3}")
          
        except Exception:
            pass
          
        # variance & mode
        try:
            print(f"    Variance: {statistics.variance(vals):.2f}")
          
        except statistics.StatisticsError:
            pass
          
        try:
            modes = statistics.multimode(vals)
            print(f"    Mode(s): {', '.join(str(m) for m in modes)}")
          
        except Exception:
            pass

# -----------------------------------------------------------
def filter_data(data):
    if not data:
        print("No data available.")
        return

    print("\nAvailable columns:", *data[0].keys())
    col = input("Enter column name to filter by:\n> ").strip()
  
    if col not in data[0]:
        print("Invalid column name!")
        return

    # detect numeric
    numeric = True
    sample = None
  
    for row in data:
        v = row[col].strip()
        if v:
            sample = v
          
            try:
                float(v)
                break
              
            except:
                numeric = False
                break

    print("\nFilter types:")
    if numeric:
        print("  1) =    2) >    3) <    4) >=    5) <=    6) contains (text)")
      
    else:
        print("  1) =    6) contains    7) startswith    8) endswith")

    choice = input("Select filter type by number:\n> ").strip()
    val = input(f"Enter comparison value for '{col}':\n> ").strip()

    def keep(row):
        cell = row[col]
        if numeric:
            try:
                num = float(cell)
                cmp = float(val)
              
            except:
                return False
              
            if choice == '1':
                return num == cmp
              
            if choice == '2':
                return num > cmp
              
            if choice == '3':
                return num < cmp
              
            if choice == '4':
                return num >= cmp
              
            if choice == '5':
                return num <= cmp
              
        # fallthrough to text
        txt = cell
      
        if choice == '6':
            return val in txt
          
        if choice == '7':
            return txt.startswith(val)
          
        if choice == '8':
            return txt.endswith(val)
          
        return False

    filtered = [r for r in data if keep(r)]
    if not filtered:
        print("No matching records.")
      
    else:
        print("\nFiltered Data:")
        display_info(filtered)

# -----------------------------------------------------------
if __name__ == "__main__":
    print("Welcome to CSV Data Analyzer!")
    path = input("Enter CSV file path: ").strip()
    data = load_csv(path)
  
    if data is None:
        exit(1)

    while True:
        print("\nMenu:")
        print(" 1. Display Data Info")
        print(" 2. Show Basic & Advanced Statistics")
        print(" 3. Filter Data")
        print(" 4. Sort Data")
        print(" 5. Exit")
        cmd = input("> ").strip()
      
        if cmd == '1':
            display_info(data)
          
        elif cmd == '2':
            basic_statistics(data)
          
        elif cmd == '3':
            filter_data(data)
          
        elif cmd == '4':
            sort_data(data)
          
        elif cmd == '5':
            print("Exiting...")
            break
          
        else:
            print("Invalid choice. Try again!")
