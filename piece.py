from typing import Tuple
from dataclasses import dataclass


@dataclass
class Piece:
    position: Tuple[int, int]
    white: bool
    has_moved: bool = False