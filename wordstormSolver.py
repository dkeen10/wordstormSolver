"""Evaluates a wordstorm puzzle and returns all possible words that can be made from the puzzle."""
"""Note: it may be better to load a dictionary file into a list and search that list instead of using pyDictionary.
https://github.com/AaronFlanagan20/Countdown-letters-game-solver
"""


# define max length of word as 9
# define min length of word as 4
MAX_WORD_LENGTH = 9
MIN_WORD_LENGTH = 4


def loadWords():
    """Loads a dictionary file into a list."""
    
    # open the dictionary file
    file = open("dictionary.txt", "r")

    # load the dictionary file into a list
    dictionary = file.readlines()

    # close the dictionary file
    file.close()

    return dictionary


def canMakeWord(word, letters):
    """Checks if a word can be made from the letters."""
    
    # loop through all letters in the word
    for letter in word:
        # check if the letter is in the letters
        if letter in letters:
            # remove the letter from the letters
            letters = letters.replace(letter, "", 1)
        else:
            # return false if the letter is not in the letters
            return False
    return True


def filterWordsByLength(words):
    """Filters words based on their length."""
    
    # create a list to store the filtered words
    filteredWords = []

    # loop through all words in the dictionary
    for word in words:
        # check if the word is between the min and max word length
        if len(word) > MIN_WORD_LENGTH and len(word) <= MAX_WORD_LENGTH:
            # add the word to the filtered words list
            filteredWords.append(word)
    return filteredWords


def filterWordsByLetters(words, letters):
    """Filters words based on whether they can be made from the letters."""
    
    # create a list to store the filtered words
    filteredWords = []

    # loop through all words in the dictionary
    for word in words:
        # remove the newline character from the word
        word = word.strip()

        # check if the word can be made from the letters
        if canMakeWord(word, letters):
            # add the word to the filtered words list
            filteredWords.append(word)
    return filteredWords


def getSolution(letters):
    """Returns all possible words that can be made from the puzzle."""
        
    possibleWords = loadWords()
    possibleWords = filterWordsByLength(possibleWords)
    # filter words based on whether they can be made from the letters
    possibleWords = filterWordsByLetters(possibleWords, letters)
    return possibleWords


def main():
    """Main function of the program."""

    print("Wordstorm Solver")
    letters = input("Enter the letters: ")

    # Get all possible words from the letters
    possibleWords = getSolution(letters)

    # Print all possible words
    print(f"Possible words: {possibleWords}")
    

if __name__ == "__main__":
    main()
