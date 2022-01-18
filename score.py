import pyxel
import constants as C


# Handles scoring
class Score:
    def __init__(self):
        self.level = C.LEVEL
        self.score = C.SCORE
        self.lines = C.LINES
        self.combos = C.COMBOS
        self.spins = C.SPINS
        self.spin_type = ""
        self.score_type = ""
    
    