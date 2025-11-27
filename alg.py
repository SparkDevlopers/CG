from typing import Tuple

from piece import Piece

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

    return p

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
    return p

def checkInBoard(cpos: Tuple[int, int]):
    if 0<= cpos[0] <= 7 and 0<= cpos[1] <= 7:
        return True
    else:
        return False

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
    return p

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
    return p

def pPawn(piece :Piece):
    p =[]
    pos = piece.position

    if piece.has_moved == True:
        if piece.white == True:
            p.extend([(pos[0]+2, pos[1]), (pos[0]+1, pos[1])])
        else:
            p.extend([(pos[0]-2, pos[1]), (pos[0]-1, pos[1])])
    else:
        pass
    return p

def putYourPenisInMyBooty():
    print("glug glug glug")

tPiece = Piece((0,1), True, True)

print(pPawn(tPiece))



