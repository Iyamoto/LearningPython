# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def get_letter(good_letters):
    letter = input('Please guess a letter: ')
    letter = str(letter)
    assert len(letter)==1
    index = good_letters.find(letter)
    assert index>=0
    return letter

# body
guesses = 8
sep = '-------------'
good_letters = string.ascii_lowercase
word = choose_word(wordlist).lower()
length = len(word)
guessed_word = '_'*length

print('Welcome to the game, Hangman!')
print('I am thinking of a word that is',length,'letters long.')
print(sep)
while guessed_word.count('_')>0 and guesses>0:
    print('You have',guesses,'guesses left.')
    print('Available letters:',good_letters)
    letter = get_letter(good_letters)
    good_letters = good_letters.replace(letter,'')
    count = word.count(letter)
    if count>0:
        #found letter
        #replace _ in guessed word
        index = 0
        for i in range(count):
            index = word.find(letter, index)
            if index>=0:
                guessed_word = guessed_word[:index] + letter + guessed_word[index+1:]
                index+=1
        print('Good guess:', guessed_word)
    else:    
        print('Oops! That letter is not in my word:', guessed_word)
        guesses-=1     
    print(sep)
if word==guessed_word:
    print('You win!')
else:
    print('You lose!')
