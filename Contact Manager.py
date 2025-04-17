import json
import os

# File path for storing contacts
CONTACTS_FILE = "contacts.json"

# Dictionary to store contacts
contacts = {}


def load_contacts():
    """Loads contacts from a JSON file if it exists."""
    global contacts
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)


def save_contacts():
    """Saves the current contacts to a JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    """Adds a new contact to the dictionary."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number (10 digits): ").strip()

    if not name or not phone.isdigit() or len(phone) != 10:
        print("❌ Invalid input! Please enter a valid name and 10-digit phone number.")
        return

    if name in contacts:
        print("⚠️ Contact already exists!")
      
    else:
        contacts[name] = phone
        save_contacts()
        print(f"✅ Contact '{name}' added successfully!")


def view_contacts():
    """Displays all saved contacts."""
    if not contacts:
        print("📭 No contacts available!")
        return

    print("\n📇 Contact List:")
    for name, phone in contacts.items():
        print(f"- {name}: {phone}")


def search_contact():
    """Searches for a contact using partial name or phone number."""
    keyword = input("🔍 Enter name or number to search: ").strip().lower()
    results = {name: phone for name, phone in contacts.items()
               if keyword in name.lower() or keyword in phone}

    if results:
        print("\n🔎 Search Results:")
        for name, phone in results.items():
            print(f"- {name}: {phone}")
          
    else:
        print("❌ No matching contacts found!")


def update_contact():
    """Updates an existing contact (name or phone number)."""
    old_name = input("Enter the contact name to update: ").strip()

    if old_name in contacts:
        new_name = input("Enter the new name (press Enter to keep the same): ").strip()
        new_phone = input("Enter new phone number (10 digits, press Enter to keep the same): ").strip()

        if new_phone and (not new_phone.isdigit() or len(new_phone) != 10):
            print("❌ Invalid phone number! Must be 10 digits.")
            return

        if new_name and new_name != old_name:
            contacts[new_name] = contacts.pop(old_name)
            old_name = new_name

        if new_phone:
            contacts[old_name] = new_phone

        save_contacts()
        print(f"✅ Contact '{old_name}' updated successfully!")
      
    else:
        print("❌ Contact not found!")


def delete_contact():
    """Deletes a contact by name."""
    if not contacts:
        print("⚠️ No contacts available to delete!")
        return

    name_to_delete = input("Enter name of contact to delete: ").strip()
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        save_contacts()
        print(f"🗑️ Contact '{name_to_delete}' deleted successfully!")
      
    else:
        print("❌ No contact found with that name!")


def userChoice(choice):
    """Handles user input and calls the appropriate function."""
    if choice == '1':
        add_contact()
      
    elif choice == '2':
        view_contacts()
      
    elif choice == '3':
        search_contact()
      
    elif choice == '4':
        update_contact()
      
    elif choice == '5':
        delete_contact()
      
    elif choice == '6':
        print("👋 Goodbye! See you again.")
        exit()
      
    else:
        print("❗ Invalid choice! Please enter a number between 1 and 6.")


if __name__ == '__main__':
    load_contacts()

    while True:
        print("\n📞 Contact Manager Menu:")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")

        choice = input("👉 Choose an option (1-6): ").strip()
        userChoice(choice)
