from typing import Tuple


#Stores all the pieces
activeWPieces = []
activeBPieces = []
capturedWPieces = []
capturedBPieces = []

board:dict[Tuple[int, int], None|object] = {
    (1,1): None, (1,2): None, (1,3): None, (1,4): None, (1,5): None, (1,6): None, (1,7): None, (1,8): None,
    (2,1): None, (2,2): None, (2,3): None, (2,4): None, (2,5): None, (2,6): None, (2,7): None, (2,8): None,
    (3,1): None, (3,2): None, (3,3): None, (3,4): None, (3,5): None, (3,6): None, (3,7): None, (3,8): None,
    (4,1): None, (4,2): None, (4,3): None, (4,4): None, (4,5): None, (4,6): None, (4,7): None, (4,8): None,
    (5,1): None, (5,2): None, (5,3): None, (5,4): None, (5,5): None, (5,6): None, (5,7): None, (5,8): None,
    (6,1): None, (6,2): None, (6,3): None, (6,4): None, (6,5): None, (6,6): None, (6,7): None, (6,8): None,
    (7,1): None, (7,2): None, (7,3): None, (7,4): None, (7,5): None, (7,6): None, (7,7): None, (7,8): None,
    (8,1): None, (8,2): None, (8,3): None, (8,4): None, (8,5): None, (8,6): None, (8,7): None, (8,8): None,
}