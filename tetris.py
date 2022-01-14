import pyxel
import constants as C


# Class to run Tetris
class Tetris:
    def __init__(self):
        pyxel.init(width=C.WINDOW, height=C.WINDOW, title="TETRIS", fps=60)
        pyxel.load("assets/tetrominos.pyxres")  # Load assets into app
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

if __name__ == "__main__":
    Tetris()