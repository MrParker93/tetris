import pyxel
import constants as C
from constants import Scene


# Handles all the UI
class UI:
    def draw_game_borders(self):
        pyxel.bltm(4, 10, 0, 0, 0, C.BOARDWIDTH * C.GRID_SIZE, C.BOARDHEIGHT * C.GRID_SIZE)
        # pyxel.rectb(4, 8, (C.BOARDWIDTH * C.GRID_SIZE) + 1, (19 * C.GRID_SIZE) + 1, 7)
        # pyxel.rectb((C.WINDOW / 2) + 59, 16, 54, 48, 5)
        pyxel.rectb(C.WINDOW / 2 , 16, 54, 48, 7)

    def draw_grid(self):
        for row in range(10):
            pyxel.line(12 + (8 * row), 8, 4 + (8 * row), (19 * 8) + 8, 13)
            pyxel.line(12, 8 + (8 * row), 4 + (C.BOARDWIDTH * 8), 8 + (8 * row), 13)
            pyxel.line(12, 8 + (8 * (row + 10)), 4 + (C.BOARDWIDTH * 8), 8 + (8 * (row + 10)), 13)

    def paused(self):
        pyxel.text(C.WINDOW // 2 - 20, C.WINDOW // 2 - 12, "PAUSED", pyxel.frame_count % 9)

    def game_over_screen(self):
        pyxel.text(C.WINDOW // 2 - 20, C.WINDOW // 2 - 12, "GAME OVER", pyxel.frame_count % 5)