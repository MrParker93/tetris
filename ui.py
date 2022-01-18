import pyxel
import constants as C
from constants import Scene


# Handles all the UI
class UI:
    def __init__(self, level, score, lines, combos, spins):
        self.level = level
        self.score = score
        self.lines = lines
        self.combos = combos
        self.spins = spins
        
    def draw_game_borders(self):
        pyxel.bltm(C.LEFTRIGHT_PADDING, C.TOP_PADDING, 0, 0, 0, C.BOARDWIDTH * 10, C.BOARDHEIGHT * 10)
        # pyxel.rectb(4, 8, (C.BOARDWIDTH * C.GRID_SIZE) + 1, (19 * C.GRID_SIZE) + 1, 7)
        # pyxel.rectb((C.WINDOW / 2) + 59, 16, 54, 48, 5)
        # pyxel.rectb(C.WINDOW / 2 , 16, 54, 48, 7)

    def draw_grid(self):
        for line in range(10):
            # Draw vertical lines of the grid
            pyxel.line(C.LEFTRIGHT_PADDING + 7 + (80 / 10 * line), C.TOP_PADDING, C.LEFTRIGHT_PADDING + 7 + (80 / 10 * line), 230, 1)

        for line in range(1, 28):
            # Draw horizontal lines of the grid
            pyxel.line(C.LEFTRIGHT_PADDING + 8, C.TOP_PADDING + (216 / 27 * line), 107, C.TOP_PADDING + (216 / 27 * line), 1)

    def paused(self):
        pyxel.cls(0)
        pyxel.text(C.WINDOW // 2 - 20, C.WINDOW // 2 - 12, "PAUSED", pyxel.frame_count % 9)

    def game_over_screen(self):
        pyxel.cls(0)
        pyxel.text(C.WINDOW // 2 - 20, C.WINDOW // 2 - 12, "GAME OVER", pyxel.frame_count % 5)

    def text(self):
        pyxel.FONT_HEIGHT = 12
        pyxel.FONT_WIDTH = 10
        # pyxel.text(C.WINDOW / 2 + 1, 9, "HOLD: ", 10)
        pyxel.text(C.WINDOW / 2, 9, "NEXT: ", 10)
        pyxel.text(C.WINDOW / 2 + 1, 70, "LEVEL: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 70, str(self.level), 6)
        pyxel.text(C.WINDOW / 2 + 1, 80, "SCORE: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 80, str(self.score), 6)
        pyxel.text(C.WINDOW / 2 + 1, 90, "LINES: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 90, str(self.lines), 6)
        pyxel.text(C.WINDOW / 2 + 1, 100, "COMBOS: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 100, str(self.combos), 6)
        pyxel.text(C.WINDOW / 2 + 1, 110, "SPINS: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 110, str(self.spins), 6)

        pyxel.text(C.WINDOW / 2 + 1, 130, "P: ", 10)
        pyxel.text(C.WINDOW / 2 + 20, 130, "PAUSE", 6)
        pyxel.text(C.WINDOW / 2 + 1, 140, "Q: ", 10)
        pyxel.text(C.WINDOW / 2 + 20, 140, "QUIT", 6)
        pyxel.text(C.WINDOW / 2 + 1, 150, "R: ", 10)
        pyxel.text(C.WINDOW / 2 + 20, 150, "RESTART", 6)

        pyxel.text(C.WINDOW / 2 + 1, 170, "LEFT: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 170, "MOVE LEFT", 6)
        pyxel.text(C.WINDOW / 2 + 1, 180, "RIGHT: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 180, "MOVE RIGHT", 6)
        pyxel.text(C.WINDOW / 2 + 1, 190, "DOWN: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 190, "MOVE DOWN", 6)
        pyxel.text(C.WINDOW / 2 + 1, 200, "SPACE: ", 10)
        pyxel.text(C.WINDOW / 2 + 30, 200, "HARD DROP", 6)

        pyxel.text(C.WINDOW / 2 + 1, 220, "Z: ", 10)
        pyxel.text(C.WINDOW / 2 + 20, 220, "ROTATE LEFT", 6)
        pyxel.text(C.WINDOW / 2 + 1, 230, "X: ", 10)
        pyxel.text(C.WINDOW / 2 + 20, 230, "ROTATE RIGHT", 6)