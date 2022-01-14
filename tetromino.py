from constants import BOARDWIDTH

class Tetromino:
    O_MINO = {
        "shape": "O",
        "block": [
            [[0, 10, 10, 0],
            [0, 10, 10, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],
                
            [[0, 10, 10, 0],
            [0, 10, 10, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 10, 10, 0],
            [0, 10, 10, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 10, 10, 0],
            [0, 10, 10, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (0, 1)
        }
        
    S_MINO = {
        "shape": "S",
        "block": [
            [[0, 3, 3, 0],
            [3, 3, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 3, 0, 0],
            [0, 3, 3, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 0]],

            [[0, 0, 0, 0],
            [0, 3, 3, 0],
            [3, 3, 0, 0],
            [0, 0, 0, 0]],

            [[3, 0, 0, 0],
            [3, 3, 0, 0],
            [0, 3, 0, 0],
            [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    Z_MINO = {
        "shape": "Z",
        "block": [
            [[8, 8, 0, 0],
            [0, 8, 8, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 0, 8, 0],
            [0, 8, 8, 0],
            [0, 8, 0, 0],
            [0, 0, 0, 0]],

            [[0, 0, 0, 0],
            [8, 8, 0, 0],
            [0, 8, 8, 0],
            [0, 0, 0, 0]],

            [[0, 8, 0, 0],
            [8, 8, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    J_MINO = {
        "shape": "J",
        "block": [
            [[5, 0, 0, 0],
            [5, 5, 5, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 5, 5, 0],
            [0, 5, 0, 0],
            [0, 5, 0, 0],
            [0, 0, 0, 0]],

            [[0, 0, 0, 0],
            [5, 5, 5, 0],
            [0, 0, 5, 0],
            [0, 0, 0, 0]],

            [[0, 5, 0, 0],
            [0, 5, 0, 0],
            [5, 5, 0, 0],
            [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    L_MINO = {
        "shape": "L",
        "block": [
            [[0, 0, 9, 0],
            [9, 9, 9, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 9, 0, 0],
            [0, 9, 0, 0],
            [0, 9, 9, 0],
            [0, 0, 0, 0]],

            [[0, 0, 0, 0],
            [9, 9, 9, 0],
            [9, 0, 0, 0],
            [0, 0, 0, 0]],

            [[9, 9, 0, 0],
            [0, 9, 0, 0],
            [0, 9, 0, 0],
            [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    T_MINO = {
        "shape": "T",
        "block": [
            [[0, 2, 0, 0],
            [2, 2, 2, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 2, 0, 0],
            [0, 2, 2, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 0]],

            [[0, 0, 0, 0],
            [2, 2, 2, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 0]],

            [[0, 2, 0, 0],
            [2, 2, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    I_MINO = {
        "shape": "I",
        "block": [
            [[0, 0, 0, 0],
            [12, 12, 12, 12],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 0, 12, 0],
            [0, 0, 12, 0],
            [0, 0, 12, 0],
            [0, 0, 12, 0]],

            [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [12, 12, 12, 12],
            [0, 0, 0, 0]],

            [[0, 12, 0, 0],
            [0, 12, 0, 0],
            [0, 12, 0, 0],
            [0, 12, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2 + 1,
        "y": -2,
        "centre": (1, 1)
        }

    def __init__(self, generator):
        self.tetrominos = [self.O_MINO, self.S_MINO, self.Z_MINO, self.J_MINO, self.L_MINO, self.T_MINO, self.I_MINO]
        self.mino = self.tetrominos[generator]
        self.block = self.mino["block"][0]
        self.rotations = 4
        self.current_orientation = 0
        self.orientations = self.get_orientations()

    def get_orientations(self):
        orientations = [
            self.block,
            self.mino["block"][1],
            self.mino["block"][2],
            self.mino["block"][3]
        ]
        return orientations
        
    def rotate_left(self):
        self.current_orientation -= 1
        return self.orientations[self.current_orientation % self.rotations]

    def rotate_right(self):
        self.current_orientation += 1
        return self.orientations[self.current_orientation % self.rotations]
