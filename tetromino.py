from constants import BOARDWIDTH


# Handle all Tetrominos
class Tetromino:
    O_MINO = {
        "shape": "O",
        "block": [
            [[10, 10, 0, 0],
            [10, 10, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],
                
            [[10, 10, 0, 0],
            [10, 10, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[10, 10, 0, 0],
            [10, 10, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[10, 10, 0, 0],
            [10, 10, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2 + 1,
        "y": -2,
        "u": 0,
        "v": 208,
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
        "u": 0,
        "v": 80,
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
        "u": 0,
        "v": 112,
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
        "u": 0,
        "v": 144,
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
        "u": 0,
        "v": 176,
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
        "u": 0,
        "v": 48,
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
        "u": 0,
        "v": 16,
        "centre": (1, 1)
        }

    def __init__(self, generator):
        self.tetrominos = [self.O_MINO, self.S_MINO, self.Z_MINO, self.J_MINO, self.L_MINO, self.T_MINO, self.I_MINO]
        self.mino = self.tetrominos[generator]
        self.block = self.mino["block"][0]
        self.estimate = (48, self.mino["v"])  # The (u, v) coordinate in the image map for the colour of the ghost version of the tetromino
        self.destroy = (32, 0)  # The (u, v) coordinate in the image map for the colour of the tetromino before clearing the line
        self.rotations = 4
        self.current_orientation = 0
        self.orientations = self.get_orientations()
        self.wallkicks = self.get_wallkicks()

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

    # Attempts to kick the tetromino into a valid position if the normal rotation is invalid
    def get_wallkicks(self): 
        if self.mino["shape"] != "I":
            wallkicks = [
                [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # L -> 0 orientation: 0
                [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],  # 0 -> R  orientation: 1
                [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],  # R -> 2 orientation: 2
                [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],  # 2 -> L orientation: 3
                [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],  # R -> 0 orientation: 0
                [(0, 0), (-1, 0), (-1, 1), (0, 2), (-1, 2)],  # 2 -> R orientation: 1
                [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # L -> 2 orientation: 2
                [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)]  # 0 -> L orientation: 3
            ]
        else:
            wallkicks = [
                [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],  # L -> 0 
                [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],  # 0 -> R 
                [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)],  # R -> 2 
                [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],  # 2 -> L 
                [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],  # R -> 0 
                [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],  # 2 -> R 
                [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],  # L -> 2 
                [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)]  # 0 -> L 
            ]
        return wallkicks