import re
from collections import Counter

# Read content from the file
def read_input_file(filename):
    try:
        file = open(filename, 'r')
        return file.read().strip()
      
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""


# Display the results
def display_results(total_words, search_word, word_frequency, sentence_count, paragraph_count, most_frequent):
    print(f"Total Words: {total_words}")
    print(f"Frequency of '{search_word}': {word_frequency}")
    print(f"Number of Sentences: {sentence_count}")
    print(f"Number of Paragraphs: {paragraph_count}")
    print(f"Most Frequent Word: '{most_frequent[0]}' occurred {most_frequent[1]} times")


# Count words using advanced regex to include contractions and hyphenated words
def count_words_advanced(text):
    # This pattern handles words with apostrophes and hyphens
    words = re.findall(r"\b[\w'-]+\b", text)
    return words


# Count sentences using punctuation as delimiters
def count_sentences(text):
    # Count occurrences of ., !, ? followed by space or end of string
    sentences = re.findall(r'[.!?](?:\s|$)', text)
    return len(sentences)


# Count paragraphs based on double line breaks
def count_paragraphs(text):
    paragraphs = text.split('\n\n')
    return len([p for p in paragraphs if p.strip()])  # Ignore empty paragraphs


# Prompt user for a word and calculate its frequency
def word_frequency(words):
    search_word = input("Enter the word to search: ").strip().lower()
    word_freq = sum(1 for word in words if word.lower() == search_word)
    return word_freq, search_word


# Find the most frequently occurring word
def most_frequent_word(words):
    # Normalize to lowercase for accurate frequency count
    freq = Counter(word.lower() for word in words)
    most_common = freq.most_common(1)[0]  # Returns tuple (word, frequency)
    return most_common


# Main execution
if __name__ == "__main__":
    filename = "/home/chef/workspace/input.txt"
    text = read_input_file(filename)

    if text:

        # Extract words using improved regex
        words = count_words_advanced(text)
        total_words = len(words)

        # Sentence and paragraph counting
        sentence_count = count_sentences(text)
        paragraph_count = count_paragraphs(text)

        # Word frequency search
        word_freq, search_word = word_frequency(words)

        # Most frequent word
        most_common = most_frequent_word(words)

        # Display all results
        display_results(total_words, search_word, word_freq, sentence_count, paragraph_count, most_common)
