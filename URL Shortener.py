import hashlib

data = {}  # Global in-memory dictionary

# Generate a short URL from a long URL using MD5 hashing
def generate_short_url(long_url):
  
    # Step 1: Convert the URL text to bytes (MD5 requires bytes, not text)  
    encoded_url = long_url.encode()  

    # Step 2: Create an MD5 hash object  
    hash_object = hashlib.md5(encoded_url)  
    
    # Step 3: Get the 32-character hexadecimal string  
    full_hash = hash_object.hexdigest() 
  
    # Step 4: Extract the first 6 characters of the hash to serve as the short code.
    short_code = hash_object.hexdigest()[:6]  
        
    # Step 5: Return full shortened URL
    return f"http://short.ly/{short_code}"

# Function to generate a short URL and store it in a dictionary
def shorten_url():

    # Prompt the user to enter a long URL
    long_url = input("Enter the long URL: ").strip()

    # Handling empty URL case
    if not long_url:
        print("Error: URL cannot be empty")
        return

    # Check the dictionary
    for short, url in data.items():
        if url == long_url:  # the URL is already shortened
            print(f"Short URL already exists: {short}")  # return the existing short URL
            return

    # Generate the short URL
    short_url = generate_short_url(long_url)
  
    # Store the short URL as the key and the original URL as the value in the dictionary
    data[short_url] = long_url
  
    print(f"Short URL created: {short_url}")

# Function to fetch the original URL from the stored data
def retrieve_url():

    # Prompt the user to enter the short URL
    short_url = input("Enter the short URL: ").strip()

    # Direct lookup from the dictionary
    long_url = data.get(short_url)

    # if the short URL exists, display the original URL
    if long_url:
        print(f"Original URL: {long_url}")

    # if not found, display an error message
    else:
        print("Short URL not found!")

# Accept the user input
def user_choice(choice):
  
    if choice == "1":
        shorten_url()
      
    elif choice == "2":
        retrieve_url()
      
    elif choice == "3":
        print("Exiting... Goodbye!")
        return
      
    else:
        print("Invalid choice! Try again.")

# Driver code
if __name__ == "__main__":
  
    while True:
        print("\nURL Shortener")
        print("1. Shorten a URL")
        print("2. Retrieve Original URL")
        print("3. Exit")
      
        choice = input("Choose an option (1-3): ").strip()
        user_choice(choice)
      
        if choice == "3":
            break
