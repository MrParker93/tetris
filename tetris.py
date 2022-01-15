import pyxel
import random
from ui import UI
import constants as C
from board import Board
from tetromino import Tetromino


# Class to run Tetris
class Tetris:
    def __init__(self):
        pyxel.init(width=C.WINDOW, height=C.WINDOW, title="TETRIS", fps=60)
        pyxel.load("assets/tetrominos.pyxres")  # Load assets into app
        self.t = Tetromino(random.randint(0, 6))
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)  # Clears screen and sets background to black
        UI().draw_game_borders()
        # pyxel.tilemap(0).pset(8, 16, (self.brick[0], self.brick[1]))
        Board(C.BOARDWIDTH, C.BOARDHEIGHT).drop_block(self.t.mino["x"], self.t.mino["y"], self.t.mino, self.t.current_orientation)
        Board(C.BOARDWIDTH, C.BOARDHEIGHT).drop_block_estimate(self.t.mino["x"], self.t.mino["y"], self.t.mino, self.t.current_orientation)
        Board(C.BOARDWIDTH, C.BOARDHEIGHT).draw_board()
        # Board(C.BOARDWIDTH, C.BOARDHEIGHT).draw_bltm()
        

if __name__ == "__main__":
    Tetris()