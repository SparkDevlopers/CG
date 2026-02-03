from typing import Tuple
from dataclasses import dataclass
import chess_board


@dataclass
class Piece:
    name:str
    _position: Tuple[int, int]
    white: bool
    has_moved = False
    is_captured = False

    #update sthe position of the piece on the board just after its initialised
    def __post_init__(self):
        chess_board.board[self._position] = self

        #marks the piece as active
        if self.white:
            chess_board.activeWPieces.append(self)
        else:
            chess_board.activeBPieces.append(self)

    #to access the position of the piece
    @property
    def position(self):
        return self._position
    
    #setter function for position
    @position.setter
    def position(self, inp:Tuple[int, int]):
        chess_board.board[self._position] = None
        if self.white == True:
            chess_board.activeWPieces.remove(self)
        else:
            chess_board.activeBPieces.remove(self)
        self._position = inp
        if self.white == True:
            chess_board.activeWPieces.append(self)
        else:
            chess_board.activeBPieces.append(self)
        chess_board.board[self._position] = self
        self.has_moved = True

    #to access the status of the piece
    @property
    def is_captured(self):
        return self._position
        
    #setter function for is_captured
    @is_captured.setter
    def is_captured(self, inp:bool):
        if self.white:
            chess_board.activeWPieces.remove(self)
            chess_board.capturedWPieces.append(self)
        else:
            chess_board.activeBPieces.remove(self)
            chess_board.capturedBPieces.append(self)


