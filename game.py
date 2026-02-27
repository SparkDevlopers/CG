import alg
import chess_board
from piece import Piece

gameStart = True
turn = 1

# WHITE PIECES

wRook1   = Piece("Rook",   (1, 1), True)
wKnight1 = Piece("Knight", (1, 2), True)
wBishop1 = Piece("Bishop", (1, 3), True)
wQueen   = Piece("Queen",  (1, 4), True)
wKing    = Piece("King",   (1, 5), True)
wBishop2 = Piece("Bishop", (1, 6), True)
wKnight2 = Piece("Knight", (1, 7), True)
wRook2   = Piece("Rook",   (1, 8), True)

wPawn1 = Piece("Pawn", (2, 1), True)
wPawn2 = Piece("Pawn", (2, 2), True)
wPawn3 = Piece("Pawn", (2, 3), True)
wPawn4 = Piece("Pawn", (2, 4), True) 
wPawn5 = Piece("Pawn", (2, 5), True)
wPawn6 = Piece("Pawn", (2, 6), True)
wPawn7 = Piece("Pawn", (2, 7), True)
wPawn8 = Piece("Pawn", (2, 8), True)


# BLACK PIECES (row 8 and 7)

bRook1   = Piece("Rook",   (8, 1), False)
bKnight1 = Piece("Knight", (8, 2), False)
bBishop1 = Piece("Bishop", (8, 3), False)
bQueen   = Piece("Queen",  (8, 4), False)
bKing    = Piece("King",   (8, 5), False)
bBishop2 = Piece("Bishop", (8, 6), False)
bKnight2 = Piece("Knight", (8, 7), False)
bRook2   = Piece("Rook",   (8, 8), False)

bPawn1 = Piece("Pawn", (7, 1), False)
bPawn2 = Piece("Pawn", (7, 2), False)
bPawn3 = Piece("Pawn", (7, 3), False)
bPawn4 = Piece("Pawn", (7, 4), False)
bPawn5 = Piece("Pawn", (7, 5), False)
bPawn6 = Piece("Pawn", (7, 6), False)
bPawn7 = Piece("Pawn", (7, 7), False)
bPawn8 = Piece("Pawn", (7, 8), False)

#prompts the player for moves
def getMove(player:str):
    print(f"{player} player's move")
    #stores the colour of the player
    isWhite = True if player == "White" else False
    
    temp = input("Please enter the square of the piece you want to move (Eg: 1,1)): ")
    temp = tuple(int(i) for i in temp.split(","))

    print(f"{player} to move")
    if chess_board.board[temp] == None:
        print("There are no pieces on the entered square, please enter a different coordinate")
        getMove(player)
    elif chess_board.board[temp].white == isWhite:
        destination = input(f"Please enter the square you want to move the {chess_board.board[temp].name} to (Eg: 1,1)): ")
        destination = tuple(int(i) for i in destination.split(","))
        return [chess_board.board[temp], destination]
    else:
        print("The piece on the entered square is of the opposite colour. Please enter a different coordinate")
        getMove(player)

def game(move:list,player:str):
    if move[1] in alg.getLegalMoves(move[0]) and alg.checkKingDanger(move[0], move[1]) == False:
        print("its valid")
    else:
        print("its not valid")
        alg.printBoard()
        game(getMove(player), player)


    

while gameStart:
    if turn % 2 == 0:
        player = "Black"
    else:
        player = "White"
    
    move = getMove(player)
    game(move, player)
    if chess_board.board[move[1]] != None:
        chess_board.board[move[1]].is_captured = True
    move[0].position = move[1]

    if alg.checkGameEnd(True if player == "White" else False) == True:
        print(f"game end, {player} won")
        gameStart = False

    alg.printBoard()
    turn += 1

