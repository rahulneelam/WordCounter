# Word Counter Program

def count_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The input text.
    
    Returns:
        int: The number of words in the text.
    """
    # Remove leading/trailing whitespaces and split text into words
    words = text.strip().split()
    
    # Return the word count
    return len(words)


def main():
    # Prompt user for input
    text = input("Enter a sentence or paragraph: ")
    
    # Check for empty input
    if not text:
        print("Error: Input cannot be empty.")
        return
    
    # Count words and display result
    word_count = count_words(text)
    print(f"Word Count: {word_count}")


if __name__ == "__main__":
    main()
