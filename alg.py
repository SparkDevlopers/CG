from typing import Tuple
import numpy as np
from piece import Piece
import chess_board

#decides which function to call depending on it name
def getLegalMove(piece :Piece):
    name = piece.name
    match name:
        case "Pawn":
            return Pawn(piece)
        case "Rook":
            return Rook(piece)
        case "Knight":
            return Knight(piece)
        case "Bishop":
            return Bishop(piece)
        case "Queen":
            return Queen(piece)
        case "King":
            return King(piece)


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
    pos = piece.position
    remove = set()
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]+i), (pos[0]-i, pos[1]-i), (pos[0]-i, pos[1]+i), (pos[0]+i, pos[1]-i)]
        if remove:
            result = [v for i, v in enumerate(temp) if i not in remove]
        else:
            result = temp
            
        for f in result:
            if checkInBoard(f) == True:
                if checkPos(f) == False:
                    legal_moves.append(f)
                elif checkPos(f).white != piece.white:
                    legal_moves.append(f)
                    remove.add(temp.index(f))
                else:
                    remove.add(temp.index(f))
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

def King(piece :Piece):
    pass


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


tPawn1 = Piece("Pawn", (6,6), True, True)  
tPawn2 = Piece("Pawn", (3,7), False, True)      
tBishop = Piece("Bishop", (5,5), True, True)

Bishop(tBishop)

