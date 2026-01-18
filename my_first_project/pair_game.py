
from random import choice

#Initialize
def InitializeGrid(board):
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q','R','S','T','U'])

def DrawBoard(board):
    #Display the board to the screen
    linetodraw = ""

    #Draw some blank lines
    print("\n\n\n")
    print(" -----------------------------------")

    #Now draw rows from 8 down to 1
    for i in range(7,-1,-1):

        #Draw each row
        linetodraw = ""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print(" -----------------------------------")

    print("   a   b   c   d   e   f   g   h ")
    global score
    print("Current score: ", score)


def IsValid(move):

    #Chack length of move
    if len(move) != 3:
        return False

    #Chack space and direction
    if not(move[0] in ['a','b','c','d','e','f','g','h']):
        return False
    if not(move[1] in ['1','2','3','4','5','6','7','8']):
        return False
    if not(move[2] in ['u','d','l','r']):
        return False

    #Chack direction is valid for the given row/column
    if(move[0]== 'a' and move[2] == 'l' ):
        return False
    if (move[0] == 'h' and move[2] == 'r'):
        return False
    if (move[1] == '1' and move[2] == 'd'):
        return False
    if (move[1] == '8' and move[2] == 'u'):
        return False

    return True

def GetMove():
    #Get the move from the user
    print("Enter a move by specifying the space and the direction(u,d,l,r) ")
    print("For example, e3u would change the letter on position e3 with the one above")

    move = input("Enter move: ")

    while not IsValid(move):
        move = input("That's not a valid move! Enter a new one: ")
    return move

def Update(board,move):
    print("Updating Board")

def Initialize(board):
    InitializeGrid(board)

    #Initialize score
    global score
    score = 0

    #Initialize turn number
    global turn
    turn = 1

#Loop while game not over
def ContinueGame(current_score,goal_score = 100):
    if current_score >= goal_score:
        return False
    else:
        return True

def DoRound(board):
    #Perform one round of the game
    #Display Current Board
    DrawBoard(board)

    #get move
    move = GetMove()

    #Update Board
    Update(board,move)

    #Update turn number
    global turn
    turn += 1



def ConvertLetterToCol(Col):
    if Col == 'a':
        return 0
    elif Col == 'b':
        return 1
    elif Col == 'c':
        return 2
    elif Col == 'd':
        return 3
    elif Col == 'e':
        return 4
    elif Col == 'f':
        return 5
    elif Col == 'g':
        return 6
    elif Col == 'h':
        return 7
    else:
        return -1


def SwapPieces(board, move):
    #Get original position

    origrow = int(move[1])-1
    origcol = ConvertLetterToCol(move[0])

    #Get adjacent position
    if move[2] =='u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1

    #Swap objects in two positions
    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp

def RemovePieces(board):
    #Create board to store removals

    remove = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
         ]

    #Rows check
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j+1] and board[i][j]==board[i][j+2]):
                remove[i][j] = 1
                remove[i][j+1] = 1
                remove[i][j+2] = 1

    #Columns check
    for j in range(8):
        for i in range(6):
            if (board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j]):
                remove[i][j] = 1
                remove[i+1][j] = 1
                remove[i+2][j] = 1

    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any


def DropPieces(board):
    for j in range(8):
        #make a list of pieces in the column
        listofpieces = []
        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
        #copy that list into the column
        for i in range(len(listofpieces)):
            board[i][j] = listofpieces[i]

        #fill remainder of columns with 0
        for i in range(len(listofpieces),8):
            board[i][j] = 0

def FillBlanks(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


def Update(board, move):
    SwapPieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = RemovePieces(board)
        DropPieces(board)
        FillBlanks(board)
#Initialize main variables
score = 100
turn = 100
goal_score = 100
board = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
         ]
Initialize(board)


while ContinueGame(score,goal_score):
    DoRound(board)
