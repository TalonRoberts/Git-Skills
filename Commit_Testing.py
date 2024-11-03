# This is a basic file I will be utilizing to train and test my git skills
# Python File
def WordCount(s):
    words_and_count = {}  # Initializes an empty dictionary
    delims = [ ' ', ',', '!', '.', '?', '\n', '\r' ]      # All possible delimiters necessary to split words
    s = s.lower()    # Makes entire string lowercase so things like "word" and "Word" will be considered the same
    for delim in delims:
        s = s.replace(delim, ' ')    # Split string into words based on delimiter
    
    wordsInString = s.split()   # Split by whitespace

    for word in wordsInString:  # iterates through each word in inputted string
        if word in words_and_count:  # Checks if words_and_count contains current word
            words_and_count[word] += 1    # Adds word to wordCounts dictionary and increments its count by 1
        else:
            words_and_count[word] = 1  # First instance of word so adds word to wordCounts dictionary and sets count to 1
    
    return words_and_count

def Top10ContentWords(s):
    word_counts = WordCount(s)
    top_10_words = {}   # Dictionary to hold top 10 words
    total_words = len(word_counts)

    for _ in range(10):
        max_count = 0       # Hold highest count
        word_max = None     # Holds word with max count

        # Iterates over the words and counts in the dictionary
        for word, count in word_counts.items():
            if count > max_count:  # Check if the current count is greater than max_count
                max_count = count  # Update max_count
                word_max = word  # Update word_max with the current word

        if word_max is not None:  # If a word was found
            top_10_words[word_max] = max_count  # Add the max word to top_10_words
            del word_counts[word_max]  # Remove it from the original dictionary

    # Create a string to display the top 10 words and their counts
    top_10_string = f"Of {total_words} unique words, the top 10 words and their counts are:\n"
    
    rank = 1    # Variable to keep track of words rank
    for word, count in top_10_words.items():
        top_10_string += f"{rank}: \"{word}\": {count},\n"  # Append each word, its count, and rank to the string
        rank += 1   # Increments rank

    return top_10_string.strip(',\n')  # Remove trailing comma and newline


# Usage
s = "Hi my name is Talon Roberts, how are we doing on this fine evening. What is your favorite flavor of Starburst?"
word_counts = WordCount(s)
print("WordCount Function:", word_counts)
top_10 = Top10ContentWords(s)
print("Top10ContentWords Function:", top_10)