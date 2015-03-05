from random import randint

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

def print_board(board):
    for r in board:
        print(" ".join(r))

def row(board):
    return randint(0, len(board) - 1)

def col(board):
    return randint(0, len(board[0]) - 1)

def PlayEasy():

    length=int(input("Size(m):"))

    for x in range(length):
        board.append(["O"] * length)

    print("Let's play Battleship!")
    print_board(board)

    ship_row = row(board)
    ship_col = col(board)

    option=str(input("Do you want Hint[y/n]:"))
    if option=='y':
          print("Hint: the ship is somewhere in row {0:1} and row {1:2}\n\n".format(ship_row,randint(0,len(board)-1)))

    for turn in range(1,4):
             
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
           
            print("\n\nCongratulations! You sunk my battleship!\n\n")
            board[guess_row][guess_col]="H"
            print_board(board)
            exit()
        
        else:
           
            if (guess_row < 0 or guess_row > length-1) or  (guess_col < 0 or guess_col > length-1):
                print("Oops, that's not even in the ocean.\n\n")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.\n\n")
            else:
                print("You missed my battleship!\n\n")
                board[guess_row][guess_col] = "X"
    
            print("turn={0:1}\n".format(turn))
            print_board(board)
            
            if turn==3:
                board[ship_row][ship_col]="S"
                print("\n\nGame Over\n\n")
                print_board(board)
                print("\n\nthe battleship is at ({0:1},{1:2})".format(ship_row,ship_col))               
                exit()

def Guess(ship_row,ship_col,length):
    option=str(input("Do you want Hint[y/n]:"))
    if option=='y':
          print("Hint: the ship is somewhere in row {0:1} and row {1:2}\n\n".format(ship_row,randint(0,len(board)-1)))
    for turn in range(1,4):
             
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
           
            print("\n\nCongratulations! You sunk my battleship!\n\n")
            board[guess_row][guess_col]="H"
            print_board(board)
            return
        
        else:
           
            if (guess_row < 0 or guess_row > length-1) or  (guess_col < 0 or guess_col > length-1):
                print("Oops, that's not even in the ocean.\n\n")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.\n\n")
            else:
                print("You missed my battleship!\n\n")
                board[guess_row][guess_col] = "X"
    
            print("turn={0:1}\n".format(turn))
            print_board(board)
            
            if turn==3:
                board[ship_row][ship_col]="S"
                print("\n\nGame Over\n\n")
                print_board(board)
                print("\n\nthe battleship is at ({0:1},{1:2})".format(ship_row,ship_col))
                return


def PlayCool():
    length=int(input("Size(m>5):"))

    if(length<5):
        print("size must be greater than or equal 5X5\n")
        exit()

    for x in range(length):
        board.append(["O"] * length)

    print("Let's play Battleship!")
    print_board(board)

    No=int(input("enter the number of Battleships you want(should be less than m-3):"))
    
    for x in range(No):
        rows.append(["O"] * No)
    for x in range(No):
        cols.append(["O"] * No)

    if No<=length-3:
        for i in range(No):
            rows[i]=row(board)
            cols[i]=col(board)
    else:
        print("No of Battleships exceeds the limit!")
        exit()

    for i in range(0,No):
        print("Guess battleship {0:1}\n".format(No))
        Guess(rows[i],cols[i],length)
    exit()

def play(option):

    while switch(option):
        if case('1'):
            PlayEasy()
        if case('2'):
            PlayCool()
        print("Invalid option")
        exit()

    
if __name__=="__main__":

    board = []
    rows = []
    cols = []


    Choice=str(input("Enter 1: to play\n      2: to exit\n"))

    if Choice=='1':
        option=str(input("Enter 1: Easy (Single Battleship)\n      2: Difficult (Multiple Battleships)\n"))
        play(option)
    else:
        exit()
       
        
        
        

