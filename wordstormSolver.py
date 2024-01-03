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


def canMakeWord(word, letters, requiredLetter):
    """Checks if a word can be made from the letters."""
    if requiredLetter not in word:
        return False

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
        if len(word) > MIN_WORD_LENGTH and len(word) <= MAX_WORD_LENGTH + 1:
            # add the word to the filtered words list
            filteredWords.append(word)
    return filteredWords


def filterWordsByLetters(words, letters, requiredLetter):
    """Filters words based on whether they can be made from the letters. (also checks that there is not more duplicates than available.)"""
    
    # create a list to store the filtered words
    filteredWords = []

    # loop through all words in the dictionary
    for word in words:
        # remove the newline character from the word
        word = word.strip()

        # check if the word can be made from the letters
        if canMakeWord(word, letters, requiredLetter):
            # add the word to the filtered words list
            filteredWords.append(word)
    return filteredWords


def getSolution(letters, requiredLetter):
    """Returns all possible words that can be made from the puzzle."""
        
    possibleWords = loadWords()
    possibleWords = filterWordsByLength(possibleWords)
    # filter words based on whether they can be made from the letters
    possibleWords = filterWordsByLetters(possibleWords, letters, requiredLetter)
    return possibleWords


def main():
    """Main function of the program."""

    print("Wordstorm Solver")
    letters = input("Enter the letters: ")
    requiredLetter = input("Enter the required letter: ")

    # Get all possible words from the letters
    possibleWords = getSolution(letters, requiredLetter)

    # Print all possible words
    print(f"9 Letter Word: {[word for word in possibleWords if len(word) == 9]}")
    for i in range (8, 3, -1):
        print(f"{i} Letter Words: {[word for word in possibleWords if len(word) == i]}")


if __name__ == "__main__":
    main()
