import pyxel
import random
from ui import UI
import constants as C
from board import Board
from constants import Scene
from tetromino import Tetromino


# Class to run Tetris
class Tetris:
    def __init__(self):
        pyxel.init(width=C.WINDOW, height=C.WINDOW, title="TETRIS", fps=60)
        pyxel.load("assets/tetrominos.pyxres")  # Load assets into app
        self.reset()
        pyxel.run(self.update, self.draw)

    # Sets the initial state of the game 
    def reset(self):
        self.state = "running"
        self.is_gameover = False
        self.scene = Scene.TITLE_SCENE
        self.t = Tetromino(random.randint(0, 6))
        self.b = Board(C.BOARDWIDTH, C.BOARDHEIGHT)
        self.b.drop_block(self.t.mino["x"], self.t.mino["y"], self.t.mino, self.t.current_orientation)
        self.b.drop_block_estimate(self.t.mino["x"], self.t.mino["y"], self.t.mino, self.t.current_orientation)

    # Handles key presses and game logic every frame
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
        if self.state == "running" or self.state == "stopped":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()
        
        if pyxel.btn(pyxel.KEY_P):
            if self.state == "running" and not self.is_gameover and self.scene == Scene.GAMEOVER_SCENE:
                self.state = "paused"
            else:
                self.state = "running"

    # Draws the game every frame, runs at 60fps
    def draw(self):
        pyxel.cls(0)  # Clears screen and sets background to black
        UI().draw_game_borders()
        UI().draw_grid()
        self.b.draw_board(self.t.mino, self.t.estimate, self.t.current_orientation)
        # pyxel.tilemap(0).pset(8, 16, (self.brick[0], self.brick[1]))
        # Board(C.BOARDWIDTH, C.BOARDHEIGHT).draw_bltm()
        

if __name__ == "__main__":
    Tetris()