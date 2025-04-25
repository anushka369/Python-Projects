import random

# List of words
word_list = ["python", "developer", "programming", "algorithm", "function", "variable", "debugging", "compiler", "codechef", "machine", "bitcoin", "operation"]

def scramble_word(word):
    """Scramble the letters of a word randomly"""
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_game():
    word_list = ["python", "developer", "programming", "algorithm", "function"]
    
    while True:  # Keep playing until user decides to exit
        original_word = random.choice(word_list)
        scrambled = scramble_word(original_word)

        print("\n Welcome to the Word Scramble Game!")
        print(f"Scrambled word: {scrambled}")

        attempts = 3

        while attempts > 0:
            guess = input("Guess the word (or type 'exit' to quit): ").lower()

            if guess == "exit":
                print("Thanks for playing! Goodbye!")
                return  # Exit the game completely

            if guess == original_word:
                print("Correct! You guessed it!\n")
                break  # Move to the next word
              
            else:
                attempts -= 1
                print(f"Wrong guess. Attempts left: {attempts}")

        print(f"The correct word was: {original_word}\n")

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break  # Exit the outer loop and end the game

# Run the game
if __name__ == "__main__":
    play_game()
