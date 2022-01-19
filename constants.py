from enum import Enum

# Representing different game scenes as an Enum class. Design decision for cleaner code.
class Scene(Enum):
    TITLE_SCENE = 1
    PLAY_SCENE = 2
    GAMEOVER_SCENE = 3

# Height and width of app window
WINDOW = 256

# Height and width of board (playable area)
BOARDWIDTH = 10
BOARDHEIGHT = 40

# Size of each block in pixels
GRID_SIZE = 8

# Bag of numbers to generate tetrominos
BAG = [_ for _ in range(7)]

# Padding for UI positioning
TOP_PADDING = 15
LEFTRIGHT_PADDING = 20

# Initial state of the game
LEVEL = 1
SCORE = 0
LINES = 0
COMBOS = 0
SPINS = 0
FALL_SPEED = 4
LOCK_DELAY = 60

# Scoring system
# Points given per line cleared
POINTS = {
    "0": 0,
    "1": 100,
    "2": 300,
    "3": 500,
    "4": 800
}

# Points given for different t-spins
T_SPIN = {
    "single": 800,
    "double": 1200,
    "triple": 1600,
    "b2b double": 1800,
    "b2b triple": 2400
}

# Points given for I, S, Z, J and L spins
TWISTS = {
    "single": 800,
    "double": 1200,
    "triple": 1600,
    "b2b double": 1800,
    "b2b triple": 2400
}