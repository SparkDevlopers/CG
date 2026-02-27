from typing import Tuple, Optional, List
import numpy as np
from piece import Piece
import chess_board
import copy

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

def printBoard(chessboard:dict|list):
    pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Pawn"]
    symbols = ["R", "N", "B", "Q", "K", "P"]
    board = ""
    temp = 1
    for i in chessboard:
        if chessboard[i] != None:
            name = chessboard[i].name
            if name in pieces:
                board = board+(symbols[pieces.index(name)].lower() if chessboard[i].white == False else symbols[pieces.index(name)])+("\n" if temp%8==0 else " ")
        else:
            board = board+"."+("\n" if temp%8==0 else " ")
        temp +=1

    print(f"\n{board}\n")

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

    mod = 1 if piece.white == True else -1

    temp = [(pos[0]+mod, pos[1]+1), (pos[0]+mod, pos[1]-1)]
    enPassant = [(pos[0], pos[1]+1), (pos[0], pos[1]-1)]
    for i in temp:
        if (checkInBoard(i) == True and (checkPos(i) != False and checkPos(i).white != piece.white)) or (checkInBoard(enPassant[temp.index(i)]) == True and checkPos(enPassant[temp.index(i)]) != False and checkPos(enPassant[temp.index(i)]).white != piece.white and checkPos(enPassant[temp.index(i)]).moveNo ==1):
            legal_moves.append(i)

    if piece.has_moved == True:
        legal_moves.extend([(pos[0]+mod, pos[1])])
    else:
        temp = [(pos[0]+(2*mod), pos[1]), (pos[0]+mod, pos[1])]
        for i in temp:
            if checkInBoard(i) == True and (checkPos(i) == False):
                legal_moves.append(i)
    return legal_moves



def King(piece :Piece):
    pos = piece.position
    legal_moves = []
    temp = [(pos[0]+1, pos[1]+1), (pos[0]-1, pos[1]-1),(pos[0]+1, pos[1]-1), (pos[0]-1, pos[1]+1), (pos[0], pos[1]+1), (pos[0], pos[1]-1),(pos[0]+1, pos[1]), (pos[0]-1, pos[1])]
    for i in temp:
        if checkInBoard(i) == True and ((checkPos(i) == False) or (checkPos(i).white != piece.white)):
            legal_moves.append(i)
    return legal_moves


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
def checkKingDanger(piece: Piece, move: Tuple[int, int]):

    original_pos = piece.position
    captured_piece = chess_board.board.get(move)

    chess_board.board[original_pos] = None

    piece._position = move
    chess_board.board[move] = piece

    if captured_piece:
        if captured_piece.white:
            chess_board.activeWPieces.remove(captured_piece)
        else:
            chess_board.activeBPieces.remove(captured_piece)

    if piece.name == "King":
        king_pos = move
    else:
        king_pos = next(
            p.position for p in
            (chess_board.activeWPieces if piece.white else chess_board.activeBPieces)
            if p.name == "King"
        )

    enemy_pieces = chess_board.activeBPieces if piece.white else chess_board.activeWPieces
    all_enemy_moves = []

    for enemy in enemy_pieces:
        all_enemy_moves.extend(getLegalMoves(enemy))

    in_check = king_pos in all_enemy_moves

    chess_board.board[move] = captured_piece
    piece._position = original_pos
    chess_board.board[original_pos] = piece

    if captured_piece:
        if captured_piece.white:
            chess_board.activeWPieces.append(captured_piece)
        else:
            chess_board.activeBPieces.append(captured_piece)

    return in_check
        
def checkGameEnd(white_just_moved: bool):

    defending_pieces = chess_board.activeBPieces if white_just_moved else chess_board.activeWPieces

    # 1️⃣ Check if defending king is currently in check
    king = next(p for p in defending_pieces if p.name == "King")

    currentPieces = chess_board.activeWPieces if white_just_moved else chess_board.activeBPieces
    allMoves = []

    for piece in currentPieces:
        allMoves.extend(getLegalMoves(piece))  # now pseudo-legal

    if king.position not in allMoves:
        return False  # Not even in check → no checkmate

    # 2️⃣ Try every possible move by defending side
    for piece in defending_pieces:
        pseudo_moves = getLegalMoves(piece)

        for move in pseudo_moves:
            if not checkKingDanger(piece, move):
                return False  # Found escape move

    return True  # In check and no escape → checkmate



def pRook(piece : Piece):
    p = []
    pos = piece.position
    for i in range(1, 8):
        temp = [(pos[0] + i, pos[1]), (pos[0] - i, pos[1]), (pos[0], pos[1] + i), (pos[0], pos[1] - i)]
        for f in temp:
            if checkInBoard(f) == True:
                p.append(f)
            else:
                continue
    return p






"""  #searches the activeWPieces or activeBPieces(depending on the colour of the current piece) for the King and gets its position
    oppositeKing = next(p for p in (chess_board.activeBPieces if white else chess_board.activeWPieces)if p.name == "King")
    allMoves = []
    
    if white == False:
        for i in chess_board.activeBPieces:
            allMoves.extend(getLegalMoves(i))
    else:
        for i in chess_board.activeWPieces:
            allMoves.extend(getLegalMoves(i))
    #checks if the king is in danger
    if oppositeKing.position in allMoves:
        temp =0
        for i in getLegalMoves(oppositeKing):
            if checkKingDanger(oppositeKing, i) == False:
                temp +=1
        print(temp)
        if temp>0:
            return True
        else:
            return False     
    else:
        return False"""


"""WQueen = Piece("Queen", (2,4), True)      
WQueen.is_captured = True"""
#WKing = Piece("King", (1,5), True)
"""BBishop = Piece("Bishop", (5,1), False)
print(chess_board.activeBPieces, chess_board.board)
BBishop.position=(1,1)
print(chess_board.activeBPieces, chess_board.board)"""

#BBishop = Piece("Knight", (7,3), False)
#x,y = input().split()
#move  = (int(x), int(y))
#print("valid move" if move in (getLegalMoves(BBishop)) and checkKingDanger( BBishop, move)else "fck")