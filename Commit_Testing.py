# This is a basic file I will be utilizing to train and test my git skills
# Python File
def Top10ContentWords(s):
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

# Usage
s = "Hi my name is Talon Roberts, how are we doing on this fine evening. What is your favorite flavor of Starburst?"
word_counts = Top10ContentWords(s)
print(word_counts)