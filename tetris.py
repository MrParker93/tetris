import pyxel
import random
from ui import UI
import constants as C
from board import Board
from score import Score
from movement import Move
from constants import Scene
from copy import copy, deepcopy
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
        self.lock_delay = C.LOCK_DELAY
        self.block_fall_speed = C.FALL_SPEED
        self.s = Score()
        self.ui = UI(self.s.level, self.s.score, self.s.lines, self.s.combos, self.s.spins)
        random.shuffle(C.BAG)
        self.tetromino = Tetromino(C.BAG[0])
        self.block_position_x = self.tetromino.mino["x"]  
        self.block_position_y = self.tetromino.mino["y"]
        self.current_block_orientation = self.tetromino.current_orientation
        self.next_tetromino = Tetromino(C.BAG[1])
        self.b = Board(C.BOARDWIDTH, C.BOARDHEIGHT)
        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

    # Handles key presses and game logic every frame
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
        # Resets the game
        if self.state == "running" or self.state == "stopped":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()
        
        # Pauses the game
        if pyxel.btn(pyxel.KEY_P):
            if self.state == "running" and not self.is_gameover and not self.scene == Scene.GAMEOVER_SCENE:
                self.state = "paused"
            else:
                self.state = "running"

        if self.state == "running":

            # Makes the tetromino fall after a specific number of frames
            if pyxel.frame_count % int(60 / self.block_fall_speed) == 0:
                if not self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                    self.block_position_y += 1
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                else:
                    if pyxel.frame_count % self.lock_delay == 0:
                        self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                        self.b.grid = deepcopy(self.b.board)
                        if self.check_game_over():
                            self.is_gameover = True
                            self.state = "stopped"
                            self.scene = Scene.GAMEOVER_SCENE
                        self.generate_new_block()

            # Move the tetromino left
            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                if self.block_position_y > -1:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.block_position_x = self.move.move_left()
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

            # Move the tetromino right
            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                if self.block_position_y > -1:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.block_position_x = self.move.move_right()
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

            # Move the tetromino down
            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                if self.block_position_y > -1:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.block_position_y = self.move.move_down()
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                        
                    if pyxel.frame_count % self.lock_delay == 0:
                        if self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                            self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                            self.b.grid = deepcopy(self.b.board)
                            if self.check_game_over():
                                self.is_gameover = True
                                self.state = "stopped"
                                self.scene = Scene.GAMEOVER_SCENE
                    #         self.add_scores()
                            self.generate_new_block()

            # Instantly drop the tetromino towards the bottom
            if pyxel.btn(pyxel.KEY_SPACE):
                if self.block_position_y > -1:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.block_position_y = self.move.hard_drop()
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

                    if pyxel.frame_count % self.lock_delay == 0:
                        if self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                            self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                            self.b.grid = deepcopy(self.b.board)
                            if self.check_game_over():
                                self.is_gameover = True
                                self.state = "stopped"
                                self.scene = Scene.GAMEOVER_SCENE
                    #         self.add_scores()
                            self.generate_new_block()

            # Rotate the tetromino right
            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                if self.block_position_y > -1:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.current_block_orientation = self.move.rotate_right()
                    # self.rotated = True

                    if not self.move.can_rotate(self.tetromino, self.block_position_x, self.block_position_y, self.current_block_orientation):
                        wallkicks = self.tetromino.wallkicks[:4]
                        for x, y in wallkicks[self.current_block_orientation]:
                            if self.move.can_rotate(self.tetromino, self.block_position_x + x, self.block_position_y + y, self.current_block_orientation):
                                self.block_position_x += x
                                self.block_position_y += y
                                self.rotated = True
                                break
                        else:
                            self.current_block_orientation -= 1 if self.current_block_orientation > 0 else -3
                    #         self.rotated = False

                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

            # Rotate the tetromino left
            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                if self.block_position_y > -1:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.current_block_orientation = self.move.rotate_left()
                    # self.rotated = True

                    if not self.move.can_rotate(self.tetromino, self.block_position_x, self.block_position_y, self.current_block_orientation):
                        wallkicks = self.tetromino.wallkicks[4:]
                        for x, y in wallkicks[self.current_block_orientation]:
                            if self.move.can_rotate(self.tetromino, self.block_position_x + x, self.block_position_y + y, self.current_block_orientation):
                                self.block_position_x += x
                                self.block_position_y += y
                                self.rotated = True
                                break
                        else:
                            self.current_block_orientation += 1 if self.current_block_orientation < 3 else -3
                    #         self.rotated = False

                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

    # Draws the game every frame, runs at 60fps
    def draw(self):
        pyxel.cls(0)  # Clears screen and sets background to black
        self.ui.text()
        self.ui.draw_game_borders()
        self.b.draw_next(self.next_tetromino)
        self.b.draw_board(self.tetromino.mino, self.tetromino.estimate, self.tetromino.current_orientation)

        # Pause screen
        if self.state == "paused":
            self.ui.paused()

        # Game over screen
        if self.is_gameover:
            self.ui.game_over_screen()
            self.state = "stopped"
    
    # Checks if game over condition is true
    def check_game_over(self):
        return self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation) if self.block_position_y < 0 else False
    
    # Generates a new tetromino
    def generate_new_block(self):
        self.tetromino = self.next_tetromino
        self.block_position_x = self.tetromino.mino["x"]
        self.block_position_y = self.tetromino.mino["y"]
        self.current_block_orientation = self.tetromino.current_orientation
        self.next_tetromino = Tetromino(C.BAG[random.randint(0, 6)])

if __name__ == "__main__":
    Tetris()