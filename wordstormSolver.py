"""Evaluates a wordstorm puzzle and returns all possible words that can be made from the puzzle."""
"""Note: it may be better to load a dictionary file into a list and search that list instead of using pyDictionary."""

import pyDictionary
import enchant

def getSolution(letters):
    """Returns all possible words that can be made from the puzzle."""
    
    minLength = 4
    maxLength = 9
    possibleWords = []

    # Get all possible words from the letters
    for i in range(minLength, maxLength + 1):
        possibleWords += pyDictionary.getWords(letters, i)

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
