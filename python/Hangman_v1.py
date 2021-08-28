
# Project #2 - Hangman
'''
Details:
 
Have you ever played hangman? It's a children's game, normally played by kids when they're supposed to be doing homework 
instead. If you've never played here are the rules:

https://www.youtube.com/watch?v=cGOeiQfjYPk
https://www.wikihow.com/Play-Hangman

For this assignment, we want to play hangman in 2-player mode. 
The game should start by prompting player 1 to pick a word. 
Then the screen should clear itself so that player 2 can't see the word

hint: print(chr(27) + "[2J") 

After the screen is clear, the "gallows" and the empty letter spaces should be drawn, 
and player 2 should be allowed to guess letters until they either win, or lose. 
As they choose correct letters, the letters should appear on the screen in place of the blank space 
(clear and redraw the whole screen). 
As they choose wrong letters, the "man" himself should come end up being drawn, piece by piece. 
How many guesses they get before losing is up to you (depending on how complicated of a man you want to draw).

Important: If you'd rather not do "hangman" because of the violence aspect, that's fine! Please make "snowman" instead. 
You can see an example in the wikihow link above.

Extra Credit:

Try finding a large list of dictionary words and embedding them in your application. 
When the game starts, instead of player 1 choosing the word to play with, the computer should pick a random word 
from the dictionary. This will allow you to play against the computer instead of only 2-player mode. 
When the game starts, the user should be prompted to choose between 1-player or 2-player mode.
'''
# Import built-in function and input file
import random
from Hangman_Words import listofwords
import sys

# List by the named GALLOWS, to represent each stage of the hanging process based on index...
GALLOWS = ['''
            O
           ''',
           '''
            O
            |
           ''',
           '''
            O
           /| 
           ''',
           '''
            O
           /|\\
           ''',
           '''
            O
           /|\\
           /
           ''',
           '''
            O
           /|\\
           / \\
           ''',
           '''
            +
            O
           /|\\
           / \\
           ''']
# Function to get a random word from input file
def chooseWords(input):
    word = random.choice(input) 
    return word.upper()

# Function to find duplicate elements in a list
def find_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

mode = int(input("Enter mode : 1) for 2-player-mode, 2) for againt computer...\n"))

Guess_Word = '' 

if mode == 1:

    NewUpperWord = str(input("Enter your secret word (alphabets only) : \n"))
    Guess_Word = NewUpperWord.upper()
    print(chr(27) + "[2J") 

elif mode == 2:
  
    Guess_Word = str(chooseWords(listofwords))
    NewUpperWord = Guess_Word.upper

else: 
    print("Invalid choice. Quiting game...")
    sys.exit

# Initialize turn to represent hangman stages
turn = 0 
# Create a set from chosen word.
SecretWord = set(Guess_Word)
# Create another similar set to check length.
SecretWord2 = set(Guess_Word)
# Create a list from chosen word.
ListGuessWord = list(Guess_Word)
# Create a set to store used letters.
Used_Letters = set()
# Create a list to display answer.
blanks = ['_']*len(ListGuessWord)

# End loop when turn equal to 7 and answer correctly guessed.
while turn != 7 and len(SecretWord2) > 0:
    for i in blanks:
        print(i,end=" ")
    element = input("\nInput a char : ").upper()
    if element not in SecretWord:
        print("Sorry, word does not contain letter : ",element)
        print(GALLOWS[turn])
        turn = turn + 1
        Used_Letters.add(element)
        print('You already used these letters: ', ' '.join(Used_Letters))
    elif element in SecretWord:    
        # Check if letter already exist in list of used letters.
        if element in Used_Letters:
            print("\nCharacter already used, choose again...")
            print('You already used these letters: ', ' '.join(Used_Letters))
        else: 
            Used_Letters.add(element)
            # Call function to return indexes of duplicate letters
            for i in find_duplicates_of(ListGuessWord, element):
                blanks[i] = element
            SecretWord2.remove(element)
            print('You already used these letters: ', ' '.join(Used_Letters))

if turn == 7:
    print('You lose...:( The word was ', Guess_Word)
else:
    print('You WIN! You guessed the word ', Guess_Word, ' correctly!!!')



