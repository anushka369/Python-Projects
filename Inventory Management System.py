import csv
import os

# Inventory format: product_name: [category, quantity, price]
inventory = {}
LOW_STOCK_LIMIT = 5
INVENTORY_FILE = "inventory.csv"


def load_inventory():
    """Load inventory from CSV file if exists"""
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                name, category, quantity, price = row
                inventory[name] = [category, int(quantity), float(price)]


def save_inventory():
    """Save inventory to CSV file"""
    with open(INVENTORY_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Category", "Quantity", "Price"])
        for name, details in inventory.items():
            writer.writerow([name, details[0], details[1], details[2]])
    print("📁 Inventory saved to inventory.csv\n")


def add_product():
    """Add a product to the inventory"""
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    
    if name in inventory:
        inventory[name][1] += quantity
      
    else:
        inventory[name] = [category, quantity, price]
    
    print(f"✅ Product '{name}' added successfully!\n")


def view_inventory(sorted_by=None):
    """View the items in the inventory"""
    if not inventory:
        print("📭 Inventory is empty.\n")
        return
    
    print("📦 Current Inventory:")
    print("Name\t\tCategory\tQuantity\tPrice")

    items = list(inventory.items())

    if sorted_by == "price":
        items.sort(key=lambda x: x[1][2])
      
    elif sorted_by == "quantity":
        items.sort(key=lambda x: x[1][1])
      
    elif sorted_by == "name":
        items.sort()
      
    elif sorted_by == "category":
        items.sort(key=lambda x: x[1][0])

    for name, details in items:
        print(f"{name}\t\t{details[0]}\t\t{details[1]}\t\t${details[2]:.2f}")
    print()

    # Low stock alert
    low_stock_items = [name for name, details in inventory.items() if details[1] < LOW_STOCK_LIMIT]
    if low_stock_items:
        print("🚨 Low Stock Alert for:", ", ".join(low_stock_items), "\n")


def update_product():
    """Update a product in the inventory"""
    name = input("Enter product name to update: ")
    if name not in inventory:
        print("❌ Product not found!\n")
        return

    print("\nWhich detail do you want to update?")
    print("1. Product Name")
    print("2. Category")
    print("3. Quantity")
    print("4. Price")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        new_name = input("Enter new product name: ")
        inventory[new_name] = inventory.pop(name)
        print("✅ Product name updated.\n")
      
    elif choice == "2":
        new_category = input("Enter new category: ")
        inventory[name][0] = new_category
        print("✅ Category updated.\n")
      
    elif choice == "3":
        new_quantity = int(input("Enter new quantity: "))
        inventory[name][1] = new_quantity
        print("✅ Quantity updated.\n")
      
    elif choice == "4":
        new_price = float(input("Enter new price: "))
        inventory[name][2] = new_price
        print("✅ Price updated.\n")
      
    else:
        print("❗ Invalid choice!\n")


def delete_product():
    """Delete a product from the inventory"""
    name = input("Enter product name to delete: ")
    if name in inventory:
        del inventory[name]
        print(f"🗑️ Deleted '{name}' from inventory\n")
      
    else:
        print("❌ Product not found!\n")


def search_product():
    """Search for a product in the inventory"""
    name = input("Enter product name to search: ")
    if name in inventory:
        details = inventory[name]
        print(f"🔍 {name}: Category={details[0]}, Quantity={details[1]}, Price=${details[2]:.2f}\n")
      
    else:
        print("❌ Product not found!\n")


def sort_menu():
    """Sort the items in the inventory"""
    print("Sort inventory by:")
    print("1. Name")
    print("2. Category")
    print("3. Price")
    print("4. Quantity")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        view_inventory("name")
      
    elif choice == "2":
        view_inventory("category")
      
    elif choice == "3":
        view_inventory("price")
      
    elif choice == "4":
        view_inventory("quantity")
      
    else:
        print("❗ Invalid choice!\n")


def main_menu():
    """Main inventory menu"""
    while True:
        print("\n🛠️  Inventory Management Menu")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Sort Inventory")
        print("7. Save & Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_product()
          
        elif choice == "2":
            view_inventory()
          
        elif choice == "3":
            update_product()
          
        elif choice == "4":
            delete_product()
          
        elif choice == "5":
            search_product()
          
        elif choice == "6":
            sort_menu()
          
        elif choice == "7":
            save_inventory()
            print("👋 Exiting program...")
            break
          
        else:
            print("❗ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    load_inventory()
    main_menu()
