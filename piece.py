from typing import Tuple
from dataclasses import dataclass
import chess_board


@dataclass
class Piece:
    name:str
    _position: Tuple[int, int]
    white: bool
    has_moved: bool = False
    #update sthe position of the piece on the board just after its initialised
    def __post_init__(self):
        chess_board.board[self._position] = self

    #to access the position of the piece
    @property
    def position(self):
        return self._position
    
    #setter function for position
    @position.setter
    def position(self, inp:Tuple[int, int]):
        chess_board.board[self._position] = None
        self._position = inp
        chess_board.board[self._position] = self

