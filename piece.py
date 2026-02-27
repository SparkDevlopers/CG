from typing import Tuple
from dataclasses import dataclass, field
import chess_board


@dataclass
class Piece:
    name: str
    _position: Tuple[int, int]
    white: bool
    has_moved: bool = False
    moveNo = 0
    _is_captured: bool = field(default=False, init=False)

    def __post_init__(self):
        chess_board.board[self._position] = self

        if self.white == True:
            chess_board.activeWPieces.append(self)
        else:
            chess_board.activeBPieces.append(self)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, inp: Tuple[int, int]):
        chess_board.board[self._position] = None

        self._position = inp
        chess_board.board[self._position] = self

        self.moveNo += 1
        self.has_moved = True
        print(f"{self.name} has moved")

    @property
    def is_captured(self):
        return self._is_captured

    @is_captured.setter
    def is_captured(self, value: bool):
        if value and not self._is_captured:
            if self.white:
                if self in chess_board.activeWPieces:
                    chess_board.activeWPieces.remove(self)
                    chess_board.capturedWPieces.append(self)
            else:
                if self in chess_board.activeBPieces:
                    chess_board.activeBPieces.remove(self)
                    chess_board.capturedBPieces.append(self)

            chess_board.board[self._position] = None
            self._is_captured = True
            print(f"{self.name} was captured!")
