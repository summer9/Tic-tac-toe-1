#!/usr/bin/env python
# coding: utf-8

# In[ ]:


board =["1","2","3","4","5","6","7","8","9"]
player = "X"
isRunning = True

#Print the board to the console.
def initVisualBoard():
    # starting from
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8])
    
# Player will pick their move from function below:.
def playerMove(): 
    choice = int(input("Please pick your cell [1-9]: "))
    
    #Player choose the number that not between 1 - 9, will print the error.
    if choice >=1 and choice <= 9 and board[choice-1].isnumeric():
        board[choice-1] = player
    else:
        print("The cell has been marked!")
        
#Checking horizontal if either player have marked all their move.
def checkHorizontal(board):
    #Logical is each of horizontal have the same mark by player and not with default value
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        return True

#Checking vertical if either player have marked all their move.
def checkVertical(board):
     #Logical is each of vertical have the same mark by player and not with default value
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    elif board[3] == board[5] == board[8]:
        winner = board[3]
        return True

# X checking
def checkCrossing(board):
    if board[0] == board[4] == board[8]:
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6]:
        winner = board[2]
        return True

#Checking winner
def checkWinner():
    # in order for isRunning 
    global isRunning
    if checkHorizontal(board) or checkVertical(board) or checkCrossing(board):
        # Print the final mark.
        initVisualBoard();
        print("The winner is",player)
        choice = input("Play again? (y/n)")
        if choice == "y":
            reset()
        else:
            isRunning = False;
        
#Restart the game.
def reset():
    global board
    global player
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = "X"
    
#Checking tie
def checkTie():
    oriBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # Intersection help match 2 lists, if board list is completely filled with X and 0, then intersection will return an empty list.
    if not bool(set(board).intersection(oriBoard)):
        print("It's a tie")
        initVisualBoard();
        reset();
    
    
#Player taking turn.
def switchPlayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"
        
# Logical is while isRunning = true, the game keep running.
while isRunning:
    initVisualBoard()
    playerMove()
    checkWinner()
    checkTie()
    switchPlayer()


# In[ ]:




