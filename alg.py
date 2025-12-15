from typing import Tuple
import numpy as np
from piece import Piece
import chess_board


#generates the pseudo legal moves for the Knight
def pKnight(piece :Piece):
    p = []
    pos = piece.position
    mod = [(1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1)]
    for i in mod:
        temp =tuple(np.add(np.array(pos), np.array(i)).tolist())
        if checkInBoard(temp) == True:
            p.append(temp)
        else:
            continue

    finalValidation(p, piece)

#generates the pseudo legal moves for the Bishop
def pBishop(piece :Piece):
    p =[]
    pos = piece.position
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]+i), (pos[0]-i, pos[1]-i), (pos[0]-i, pos[1]+i), (pos[0]+i, pos[1]-i)]
        for f in temp:
            if checkInBoard(f) == True:
                p.append(f)
            else:
                continue
    finalValidation(p, piece)

#generates the pseudo legal moves for the Rook
def pRook(piece :Piece):
    p =[]
    pos = piece.position
    #The maximum number of legal moves the rook can have in each axis is 8, so:
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]), (pos[0]-i, pos[1]), (pos[0], pos[1]+i), (pos[0], pos[1]-i)]
        print(temp) #for debugging
        for f in temp:
            if checkInBoard(f) == True:
                p.append(f)
            else:
                continue

    print(p)    #for debugging
    finalValidation(p, piece)

#generates the pseudo legal moves for the Queen
def pQueen(piece :Piece):
    p =[]
    pos = piece.position
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]), (pos[0]-i, pos[1]), (pos[0], pos[1]+i), (pos[0], pos[1]-i), (pos[0]+i, pos[1]+i), (pos[0]-i, pos[1]-i), (pos[0]-i, pos[1]+i), (pos[0]+i, pos[1]-i)]
        for f in temp:  
            if checkInBoard(f) == True:
                p.append(f)
            else:
                continue
    finalValidation(p, piece)

#generates the pseudo legal moves for the Pawn
def pPawn(piece :Piece):
    p =[]
    pos = piece.position

    if piece.has_moved == True:
        if piece.white == True:
            p.extend([(pos[0]+1, pos[1])])
        else:
            p.extend((pos[0]-1, pos[1]))
    else:
        if piece.white == True:
            p.extend([(pos[0]+2, pos[1]), (pos[0]+1, pos[1])])
        else:
            p.extend([(pos[0]-2, pos[1]), (pos[0]-1, pos[1])])
    finalValidation(p, piece)

def checkInBoard(cpos: Tuple[int, int]):
    #Checks if a generated coord is within bounds
    if 1<= cpos[0] <= 8 and 1<= cpos[1] <= 8:
        return True
    else:
        return False


def finalValidation(lMoves , piece: Piece):
    #list of generated pseudo legal moves is passed as lMoves
    tempWPos = []   
    tempBPos = []

    for i in chess_board.activeBPieces:
        #checks if any black pieces are on the pseudo legal squares
        if i.position in set(lMoves):
            tempBPos.append(i.position)
    for i in chess_board.activeWPieces:
        #checks if any white pieces are on the pseudo legal squares
        if i.position in set(lMoves):
            tempWPos.append(i.position)
    
    #removing the position of the same colour pieces from the list of legal moves
    if piece.white == True:
        lMoves = set(lMoves)-set(tempWPos)
    else:
        lMoves = set(lMoves)-set(tempBPos)

    print(lMoves)  #temporary to test the function

