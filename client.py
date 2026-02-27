import alg
import pygame
import math
import chess_board
from piece import Piece
from typing import Tuple

pygame.init()

#creates a window
screen = pygame.display.set_mode((1366, 768))
bgColour = (255,255,255) 


font = pygame.font.Font(None, 28)  

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

turn =1

#to resize the chess board and the pieces
scale = 1.5
squareSize = 50*scale

"""image = pygame.image.load("Sprites/Knight.png")
image = pygame.transform.scale(image, (50, 50))"""

sprites = {}
pgn = []
    

#laods all the required spriets into memory
def loadSprites():
    colours = ["White", "Black"]
    pieces = ["Pawn", "Rook", "Knight", "Bishop", "Queen", "King"]
    for i in colours:
        for k in pieces:
            image = pygame.image.load(f"Sprites/{i}/{k}.png")
            image = pygame.transform.scale(image, (squareSize, squareSize))
            sprites[(i,k)] = image

loadSprites()

#render chess pieces
def renderPieces():
    for i in chess_board.board:
        piece =chess_board.board[i]
        if piece != None:
            pos = (piece.position[1]*squareSize, (9-piece.position[0])*squareSize)
            colour = "White" if piece.white else "Black"

            image = sprites[(colour, piece.name)]
            screen.blit(image, pos)
        
#hover effect for the chess board
def onHover():
    x,y = pygame.mouse.get_pos()
    x,y = math.floor(x/squareSize), math.floor(y/squareSize)
    if 1 <= x <= 8 and 1 <= y <= 8:
        pygame.draw.rect(screen,(153, 255, 153),(squareSize*x,squareSize*y,squareSize,squareSize))
    #print(f"{x} and {9-y}")

#renders the chess board
def drawboard():
    for k in range(1,9):
        temp =k
        for i in range (1,9):
            if temp%2 == 0:
                colour = (51,25,0)
            else:
                colour = (243,238,170)
            pygame.draw.rect(screen,colour,(squareSize*i,squareSize*k,squareSize,squareSize))

            temp += 1

move = []
def getMove(pos:Tuple[int, int]):
    if not move:
        if chess_board.board[pos] != None and chess_board.board[pos].white == False if turn % 2 == 0 else True :
            move.append(pos)
    else:
        move.append(pos)
        pos, destination = move[0], move[1]
        move.clear()
        game(pos, destination)

def moveHistory(piece:Piece, pos,  destination, capture:bool, state):
    pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Pawn"]
    symbols = ["R", "N", "B", "Q", "K", ""]
    columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    pieceSymbol = symbols[pieces.index(piece.name)]
    row = ""
    if capture:
        if piece.name == "Pawn":
            row = columns[pos[1]-1]

    capture = "x" if capture == True else ""
    destination = (columns[destination[1]-1], destination[0])

    pgn.append(f"{row}{pieceSymbol}{capture}{destination[0]}{destination[1]}{state}")
    print(f"{row}{pieceSymbol}{capture}{destination[0]}{destination[1]}{state}")


def game(pos, destination):
    global turn 
    isWhite = False if turn % 2 == 0 else True
    piece = chess_board.board[pos]
    if piece != None and piece.white == isWhite :
        if destination in alg.getLegalMoves(piece) and alg.checkKingDanger(piece, destination) == False:
            captures = False
            if chess_board.board[destination] != None:
                chess_board.board[destination].is_captured = True
                captures = True
            piece.position = destination

            checkSymbol = "+" if next(p.position for p in (chess_board.activeWPieces if not piece.white else chess_board.activeBPieces) if p.name == "King") in alg.getLegalMoves(piece) else ""

            turn += 1

            white_just_moved = (turn % 2 == 0)
            if alg.checkGameEnd(white_just_moved):
                moveHistory(piece,pos, destination, captures, "#")
                print("Checkmate!\n" + ("White" if white_just_moved else "Black") + " Won!")
            else:
                moveHistory(piece,pos, destination, captures, checkSymbol)
            
def displayPGN():
    temp = 1
    chunks = [" ".join(pgn[i:i+2]) for i in range(0, len(pgn), 2)]
    for i in chunks:
        text_surface = font.render(i, True, (0, 0, 0))
        screen.blit(text_surface, (700, temp*50+100))

        temp += 1

capturedBlackPieces = pygame.Surface((400, 300))
capturedWhitePieces = pygame.Surface((400, 300))
capturedBlackPieces.fill(bgColour)
capturedWhitePieces.fill(bgColour)


def displayCapturedPieces():
        
    x = 0 

    for piece in chess_board.capturedBPieces:
        capturedBlackPieces.blit(sprites[("Black", piece.name)], (x * squareSize, 100))
        x += 1
    x = 0 
    for piece in chess_board.capturedWPieces:
        capturedWhitePieces.blit(sprites[("White", piece.name)], (x * squareSize, 100))
        x += 1

open = True
while open:
    for event in pygame.event.get():
        #checks if the user tries to close the window
        if event.type == pygame.QUIT:
            open = False
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            x,y = math.floor(x/squareSize), math.floor(y/squareSize)
            if 1 <= x <= 8 and 1 <= y <= 8:
                print(f"The user clicked on {9-y} and {x}")
                getMove((9-y,x))

    
    #changes the background colour
    screen.fill(bgColour)

    displayPGN()
    """Fix the Issue where if you click the wrong coloured piece and then tries to make an actual move evrything breaks"""
    
    drawboard()
    onHover()
    renderPieces()
    displayCapturedPieces()
    screen.blit(capturedBlackPieces, (850, 0))
    screen.blit(capturedWhitePieces, (850, 300))

    #print(alg.checkGameEnd(False if turn%2 == 0 else True))
    #print (chess_board.capturedBPieces, chess_board.capturedWPieces)
    pygame.display.flip()

