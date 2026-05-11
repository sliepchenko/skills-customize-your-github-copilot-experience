# Python Text Processing - Starter Code

def read_file(filename):
    """Read and display file contents."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                print(f"{i}: {line}", end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def analyze_text(filename):
    """Analyze text for word and character count."""
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Count characters (excluding whitespace)
        char_count = len(content.replace(" ", "").replace("\n", ""))

        # Count words
        words = content.split()
        word_count = len(words)

        # Count unique words (case-insensitive)
        unique_words = set(word.lower() for word in words)

        print(f"Total characters: {char_count}")
        print(f"Total words: {word_count}")
        print(f"Unique words: {len(unique_words)}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def find_and_replace(filename, search_word, replace_word):
    """Find and replace text in file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Perform case-insensitive replacement
        new_content = content.replace(search_word, replace_word)
        count = len(content.split(search_word)) - 1

        # Save to new file
        with open(f"{filename[:-4]}_modified.txt", 'w') as file:
            file.write(new_content)

        print(f"Replaced {count} occurrences. Saved to '{filename[:-4]}_modified.txt'")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage
if __name__ == "__main__":
    filename = "sample.txt"

    # Task 1
    print("=== Reading File ===")
    read_file(filename)

    # Task 2
    print("\n=== Analyzing Text ===")
    analyze_text(filename)

    # Task 3
    print("\n=== Find and Replace ===")
    find_and_replace(filename, "Python", "Python (programming language)")

