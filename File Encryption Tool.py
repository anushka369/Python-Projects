from cryptography.fernet import Fernet
import hashlib
from tkinter import Tk, filedialog
import os

# Suppress the Tkinter root window
Tk().withdraw()

KEY_PATH = "/home/chef/workspace/secret.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved in 'secret.key'. Keep it safe!\n")


def load_key():
    with open(KEY_PATH, "rb") as key_file:
        return key_file.read()


def compute_hash(filepath):
    """Compute SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def encrypt_file():
    try:
        key = load_key()
        cipher = Fernet(key)

        input_file = filedialog.askopenfilename(title="Select a File to Encrypt")
        if not input_file:
            print("No file selected.")
            return

        output_file = input_file + ".enc"

        with open(input_file, "rb") as file:
            file_data = file.read()

        encrypted_data = cipher.encrypt(file_data)

        with open(output_file, "wb") as file:
            file.write(encrypted_data)

        print(f"File encrypted successfully!\nEncrypted File: {output_file}\n")
      
    except FileNotFoundError:
        print("SECRET KEY NOT FOUND! Generate key first.\n")


def decrypt_file():
    try:
        key = load_key()
        cipher = Fernet(key)

        input_file = filedialog.askopenfilename(title="Select a File to Decrypt")
        if not input_file:
            print("No file selected.")
            return

        output_file = filedialog.asksaveasfilename(title="Save Decrypted File As")
        if not output_file:
            print("No output file name provided.")
            return

        with open(input_file, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print(f"File decrypted successfully!\nDecrypted File: {output_file}")

        # Ask for original file for comparison
        compare = input("Do you want to compare with the original file? (y/n): ").strip().lower()
        if compare == 'y':
            original_file = filedialog.askopenfilename(title="Select Original File to Compare")
          
            if original_file and compute_hash(original_file) == compute_hash(output_file):
                print("✅ Decrypted file matches the original file.")
              
            else:
                print("❌ Decrypted file does NOT match the original.")
        print()
      
    except Exception as e:
        print(f"Error: {e}\n")


def user_choice():
    while True:
        print("🔐 File Encryption Tool")
        print("1. Generate Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
          
        except ValueError:
            print("Invalid input! Enter a number between 1 and 4.\n")
            continue

        if choice == 1:
            generate_key()
          
        elif choice == 2:
            encrypt_file()
          
        elif choice == 3:
            decrypt_file()
          
        elif choice == 4:
            print("Exiting... Goodbye!")
            break
          
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    print("Welcome to File Encryption Tool!\n")
    user_choice()
