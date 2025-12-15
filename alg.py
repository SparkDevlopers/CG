from typing import Tuple
import numpy as np
from piece import Piece
import chess_board


#generates the legal moves for the Knight
def Knight(piece :Piece):

    legal_moves = []
    pos = piece.position
    mod = [(1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1)]
    for i in mod:
        temp =tuple(np.add(np.array(pos), np.array(i)).tolist())
        if checkInBoard(temp) == True and (checkPos(temp) == False or checkPos(temp).white != piece.white):
            legal_moves.append(temp)
        else:
            continue
    
    #to test if the function works
    print(legal_moves)

#generates the legal moves for the Bishop
def Bishop(piece :Piece):
    legal_moves =[]
    metAPiece = False
    pos = piece.position
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]+i), (pos[0]-i, pos[1]-i), (pos[0]-i, pos[1]+i), (pos[0]+i, pos[1]-i)]
        for f in temp:
            if checkInBoard(f) == True and metAPiece == False and (checkPos(f) == False or checkPos(f).white != piece.white):
                legal_moves.append(f)
                metAPiece = True
                #my idea is to use legal_moves.remove() to removve a modifire when i meet a piece in that axis
            else:
                metAPiece = True
    #to test if the function works
    print(legal_moves)

#generates the legal moves for the Rook
def Rook(piece :Piece):
    legal_moves =[]
    pos = piece.position
    #The maximum number of legal moves the rook can have in each axis is 8, so:
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]), (pos[0]-i, pos[1]), (pos[0], pos[1]+i), (pos[0], pos[1]-i)]
        print(temp) #for debugging
        for f in temp:
            if checkInBoard(f) == True:
                legal_moves.append(f)
            else:
                continue


#generates the legal moves for the Queen
def Queen(piece :Piece):
    legal_moves =[]
    pos = piece.position
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]), (pos[0]-i, pos[1]), (pos[0], pos[1]+i), (pos[0], pos[1]-i), (pos[0]+i, pos[1]+i), (pos[0]-i, pos[1]-i), (pos[0]-i, pos[1]+i), (pos[0]+i, pos[1]-i)]
        for f in temp:  
            if checkInBoard(f) == True:
                legal_moves.append(f)
            else:
                continue

#generates the legal moves for the Pawn
def Pawn(piece :Piece):
    legal_moves =[]
    pos = piece.position

    if piece.has_moved == True:
        if piece.white == True:
            legal_moves.extend([(pos[0]+1, pos[1])])
        else:
            legal_moves.extend((pos[0]-1, pos[1]))
    else:
        if piece.white == True:
            legal_moves.extend([(pos[0]+2, pos[1]), (pos[0]+1, pos[1])])
        else:
            legal_moves.extend([(pos[0]-2, pos[1]), (pos[0]-1, pos[1])])


def checkInBoard(cpos: Tuple[int, int]):
    #Checks if a generated coord is within bounds
    if 1<= cpos[0] <= 8 and 1<= cpos[1] <= 8:
        return True
    else:
        return False

#checks if there is a piece in a given square
def checkPos(pos: Tuple[int, int]):
    if chess_board.board[pos] == None:
        return False
    else:
        return chess_board.board[pos]


tPawn = Piece("Pawn", (2,2), False, True)    
tBishop = Piece("Bishop", (1,1), True, True)

Bishop(tBishop)

