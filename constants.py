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
BOARDHEIGHT = 30

# Size of each block in pixels
GRID_SIZE = 12