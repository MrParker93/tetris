import pyxel
import constants as C
from constants import Scene


# Handles all the UI
class UI:
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
