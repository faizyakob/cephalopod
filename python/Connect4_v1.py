# Project #1: A Simple Game
'''
Once you've got the rules down, your assignment should be fairly straightforward. 
You'll want to draw the board, and allow two players to take turns placing their pieces on the board 
(but as you learned above, they can only do so by choosing a column, not a row). 
The first player to get 4 across or diagonal should win!

Normally the pieces would be red and black, but you can use X and O instead.
'''

import sys
from termcolor import colored, cprint


# Initialize a list that represents board game, set all elements to X.
# Board is 6x7 in size.
board = [["X" for i in range(7)] for i in range(6)]

# text = colored(u'\u2B24', 'green')
# print(text)

# Initialize first player to Player 1.
playerTurn = 1

# Function to draw the playing board.
def drawBoard():
    rows = 6
    columns = 15
    for r in range(rows):    
        startCounter = 1   
        for c in range(columns):
            if c != columns-1:
                if c%2 == 0:
                    print("|",end="")     
                elif c%2 != 0:
                    print(" "+str(board[r][c-startCounter])+" ",end="")
                    startCounter = startCounter + 1
            else:
                print("|")
                break             
    return True

# Function to insert player's choice. 
# Main function of the program.
def checkRow(input,row): 
    global playerTurn
    green = colored(u'\u2B24', 'green')
    red = colored(u'\u2B24', 'red')
    try:
        if row == -1:
            print("Colum full. Choose another column...")
            playerChoice()
        elif board[row][input-1] == "X":
            if playerTurn == 1:
                board[row][input-1] = green
                drawBoard()
                # Check for win conditions
                checkWinHorizontal(row,input-1,board[row][input-1],playerTurn)
                checkWinVertical(row,input-1,board[row][input-1],playerTurn)
                checkWinDiagonal(row,input-1,board[row][input-1],playerTurn)                
                playerTurn = 2
                print("Player 2 turn...")
                return playerChoice()
            elif playerTurn == 2:
                board[row][input-1] = red
                drawBoard()
                # Check for win conditions
                checkWinHorizontal(row,input-1,board[row][input-1],playerTurn)
                checkWinVertical(row,input-1,board[row][input-1],playerTurn)
                checkWinDiagonal(row,input-1,board[row][input-1],playerTurn)
                playerTurn = 1
                print("Player 1 turn...")
                return playerChoice()
        else:
            return checkRow(input,row-1)
    except SystemExit:
        print("Game ended")
    except:
        print("No such column...")
        playerChoice()

# Function to call player to input choice. Initialize row to last row. 
def playerChoice():
    choice = int(input("Enter column number... "))
    checkRow(choice,5)

# Function to check win condition horizontally.
def checkWinHorizontal(row,column,xxx,player):
    if column == 0 or column == 1 or column == 2:
        if board[row][column] == xxx and board[row][column+1] == xxx and board[row][column+2] == xxx and board[row][column+3] == xxx:
            cprint('We have a winner!', 'green', 'on_red')
            sys.exit()
    elif column == 3: 
        if board[row][column] == xxx and board[row][column+1] == xxx and board[row][column+2] == xxx and board[row][column+3] == xxx:
            cprint('We have a winner!', 'green', 'on_red')
            sys.exit()
        elif board[row][column] == xxx and board[row][column-1] == xxx and board[row][column-2] == xxx and board[row][column-3] == xxx:
            cprint('We have a winner!', 'green', 'on_red')
            sys.exit()
    elif column == 4 or column == 5 or column == 6:
        if board[row][column] == xxx and board[row][column-1] == xxx and board[row][column-2] == xxx and board[row][column-3] == xxx:
            cprint('We have a winner!', 'green', 'on_red')
            sys.exit()

# Function to check win condition vertically.
def checkWinVertical(row,column,xxx,player):
    if row == 5 or row == 4 or row == 3:
        if board[row][column] == xxx and board[row-1][column] == xxx and board[row-2][column] == xxx and board[row-3][column] == xxx:
            cprint('We have a winner!', 'yellow', 'on_red')
            sys.exit()
    elif row == 2 or row == 1 or row == 0:
        if board[row][column] == xxx and board[row+1][column] == xxx and board[row+2][column] == xxx and board[row+3][column] == xxx:
            cprint('We have a winner!', 'yellow', 'on_red')
            sys.exit()    

# Function to check win condition diagonally.    
def checkWinDiagonal(row,column,xxx,player):
    if column == 0 or column == 1 or column == 2:
        if row == 5 or row == 4 or row == 3:
            if board[row][column] == xxx and board[row-1][column+1] == xxx and board[row-2][column+2] == xxx and board[row-3][column+3] == xxx:
                cprint('We have a winner!', 'cyan', 'on_red')
                sys.exit() 
        elif row == 0 or row == 1 or row == 2:
            if board[row][column] == xxx and board[row+1][column+1] == xxx and board[row+2][column+2] == xxx and board[row+3][column+3] == xxx:
                cprint('We have a winner!', 'cyan', 'on_red')
                sys.exit() 
    elif column == 4 or column == 5 or column == 6:
        if row == 5 or row == 4 or row == 3:
            if board[row][column] == xxx and board[row-1][column-1] == xxx and board[row-2][column-2] == xxx and board[row-3][column-3] == xxx:
                cprint('We have a winner!', 'cyan', 'on_red')
                sys.exit() 
        elif row == 0 or row == 1 or row == 2:
            if board[row][column] == xxx and board[row+1][column-1] == xxx and board[row+2][column-2] == xxx and board[row+3][column-3] == xxx:
                cprint('We have a winner!', 'cyan', 'on_red')
                sys.exit() 
    elif column == 3:
        if row == 0 or row == 1 or row == 2:
            if board[row][column] == xxx and board[row+1][column+1] == xxx and board[row+2][column+2] == xxx and board[row+3][column+3] == xxx:
                cprint('We have a winner!', 'cyan', 'on_red')
                sys.exit() 
            elif board[row][column] == xxx and board[row+1][column-1] == xxx and board[row+2][column-2] == xxx and board[row+3][column-3] == xxx:
                cprint('We have a winner!', 'cyan', 'on_red')
                sys.exit() 
        elif row == 5 or row == 4 or row == 3:
            if board[row][column] == xxx and board[row-1][column+1] == xxx and board[row-2][column+2] == xxx and board[row-3][column+3] == xxx:
                cprint('We have a winner!', 'cyan', 'on_red')
                sys.exit() 
            elif board[row][column] == xxx and board[row-1][column-1] == xxx and board[row-2][column-2] == xxx and board[row-3][column-3] == xxx:
                cprint('We have a winner!', 'cyan', 'on_red')
                sys.exit() 

# Call function drawBoard to start the game.
drawBoard()
print("Player 1 turn...")
playerChoice()