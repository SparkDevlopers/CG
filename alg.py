from typing import Tuple
import numpy as np
from piece import Piece
import chess_board

#decides which function to call depending on it name
def getLegalMoves(piece :Piece):
    match piece.name:
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
    raise RuntimeError(f"Unknown piece name: {piece.name!r}")


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
    
    return legal_moves

#generates the legal moves for the Bishop
def Bishop(piece :Piece):
    legal_moves = []
    pos = piece.position
    remove = set()
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]+i), (pos[0]-i, pos[1]-i), (pos[0]-i, pos[1]+i), (pos[0]+i, pos[1]-i)]
        #removes the modifiers that are unnessary
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
    return legal_moves

#generates the legal moves for the Rook
def Rook(piece :Piece):
    legal_moves = []
    pos = piece.position
    remove = set()
    for i in range(1, 8):
        temp = [(pos[0]+i, pos[1]), (pos[0]-i, pos[1]), (pos[0], pos[1]+i), (pos[0], pos[1]-i)]
        #removes the modifiers that are unnessary
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
    return legal_moves


#generates the legal moves for the Queen
def Queen(piece :Piece):
    return Rook(piece)+Bishop(piece)
    
    

#generates the legal moves for the Pawn
def Pawn(piece :Piece):
    legal_moves = []
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

#checks if a cetain move puts the king in danger
def checkKingDanger(piece:Piece, move:Tuple[int,int]):
    currentPos = piece.position
    #searches the activeWPieces or activeBPieces(depending on the colour of the current piece) for the King and gets its position
    kingPos = next(o.position for o in (chess_board.activeWPieces if piece.white else chess_board.activeBPieces) if o.name == "King")
    allEnemyMoves = []
    piece.position = move   #temporarily setting the position of the piece to the new position
    
    
    if piece.white == True:
        for i in chess_board.activeBPieces:
            allEnemyMoves.extend(getLegalMoves(i))
    else:
        for i in chess_board.activeWPieces:
            allEnemyMoves.extend(getLegalMoves(i))
    
    #checks if the king is in danger
    if kingPos in allEnemyMoves:
        piece.position = currentPos
        return True
    else:
        piece.position = currentPos
        return False
        


#WQueen = Piece("Queen", (2,4), True)      
#WKing = Piece("King", (1,5), True)
#BBishop = Piece("Bishop", (5,1), False)
BBishop = Piece("Knight", (7,3), False)
#x,y = input().split()
#move  = (int(x), int(y))
#print("valid move" if move in (getLegalMoves(BBishop)) and checkKingDanger( BBishop, move)else "fck")

print(getLegalMoves(BBishop))
