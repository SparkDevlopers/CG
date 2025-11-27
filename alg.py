from typing import Tuple
import numpy as np
from piece import Piece
import chess_board

#temporary for testing
king = Piece((1, 5), True, True)
chess_board.activeWPieces.append(king)
tPiece = Piece((1,8), True, True)

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

def pRook(piece :Piece):
    p =[]
    pos = piece.position
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]), (pos[0]-i, pos[1]), (pos[0], pos[1]+i), (pos[0], pos[1]-i)]
        for f in temp:
            if checkInBoard(f) == True:
                p.append(f)
            else:
                continue

    print(p)    #for debugging
    finalValidation(p, piece)

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
    if 0<= cpos[0] <= 7 and 0<= cpos[1] <= 7:
        return True
    else:
        return False
    

def finalValidation(lMoves, piece :Piece):
    tempWPos = []
    tempBPos = []

    for i in chess_board.activeBPieces:
        if i.position in set(lMoves):
            tempBPos.append(i.position)
    for i in chess_board.activeWPieces:
        if i.position in set(lMoves):
            tempWPos.append(i.position)
    
    #removing the position of the same colour pieces from the list of legal moves
    if piece.white == True:
        lMoves = set(lMoves)-set(tempWPos)
    else:
        lMoves = set(lMoves)-set(tempBPos)

    print(lMoves)  #temporary to test the function


pRook(tPiece)