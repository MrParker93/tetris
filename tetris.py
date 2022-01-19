import pyxel
import random
from ui import UI
import constants as C
from board import Board
from score import Score
from movement import Move
from scenes import Scenes
from constants import Scene
from copy import deepcopy
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
        self.current_scene = Scenes(Scene.TITLE_SCENE)
        self.lock_delay = C.LOCK_DELAY
        self.block_fall_speed = C.FALL_SPEED
        self.s = Score()
        self.ui = UI()
        self.level = self.s.level
        self.levelup = ""
        self.score = self.s.score
        self.lines = self.s.lines
        self.combos = self.s.combos
        self.spins = self.s.spins
        self.consecutive_spins = 0
        self.spin_type = ""
        self.score_type = ""
        self.is_locked = False
        random.shuffle(C.BAG)
        self.tetromino = Tetromino(C.BAG[0])
        self.block_position_x = self.tetromino.mino["x"]  
        self.block_position_y = self.tetromino.mino["y"]
        self.current_block_orientation = self.tetromino.current_orientation
        self.next_tetromino = Tetromino(C.BAG[1])
        self.prev_tetromino = self.tetromino
        self.prev_block_position_x = self.block_position_x
        self.prev_block_position_y = self.block_position_y
        self.b = Board(C.BOARDWIDTH, C.BOARDHEIGHT)
        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)

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
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                else:
                    if pyxel.frame_count % self.lock_delay == 0:
                        self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                        self.b.grid = deepcopy(self.b.board)
                        if self.check_game_over():
                            self.is_gameover = True
                            self.state = "stopped"
                            self.scene = Scene.GAMEOVER_SCENE
                        self.add_scores()
                        self.generate_new_block()

            # Move the tetromino left
            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                if self.block_position_y > 0:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.block_position_x = self.move.move_left()
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)

            # Move the tetromino right
            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                if self.block_position_y > 0:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.block_position_x = self.move.move_right()
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)

            # Move the tetromino down
            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                if self.block_position_y > 1:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.block_position_y = self.move.move_down()
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                    
                    # Reward 1 point per cell when tetromino is soft dropped
                    if not self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                        self.score += 1

                    if pyxel.frame_count % self.lock_delay == 0:
                        if self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                            self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                            self.b.grid = deepcopy(self.b.board)
                            if self.check_game_over():
                                self.is_gameover = True
                                self.state = "stopped"
                                self.scene = Scene.GAMEOVER_SCENE
                            self.add_scores()
                            self.generate_new_block()
            
            # Instantly drop the tetromino towards the bottom
            if pyxel.btnp(pyxel.KEY_SPACE):
                if self.block_position_y > 0:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.block_position_y = self.move.hard_drop()
                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)

                    if pyxel.frame_count % self.lock_delay == 0:
                        if self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                            self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                            self.b.grid = deepcopy(self.b.board)
                            if self.check_game_over():
                                self.is_gameover = True
                                self.state = "stopped"
                                self.scene = Scene.GAMEOVER_SCENE
                            self.add_scores()
                            self.generate_new_block()

            # Rotate the tetromino right
            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                if self.block_position_y > 0:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.current_block_orientation = self.move.rotate_right()

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

                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)

            # Rotate the tetromino left
            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                if self.block_position_y > 0:
                    self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                    self.current_block_orientation = self.move.rotate_left()

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

                    self.b.grid = deepcopy(self.b.board)
                    self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)

    # Draws the game every frame, runs at 60fps
    def draw(self):
        if self.current_scene.scene == Scene.TITLE_SCENE:
            self.current_scene.title_scene()
        else:
            pyxel.cls(0)  # Clears screen and sets background to black
            self.text()
            self.ui.draw_game_borders()
            self.b.draw_board(self.tetromino.mino, self.tetromino.estimate, self.tetromino.image_map_position, self.tetromino.current_orientation)
            self.b.draw_next(self.next_tetromino)
            if self.spin_type:
                self.s.display_spin_type(self.spin_type, self.s.consecutive_spins)
                if pyxel.frame_count % 480 == 0:
                    self.spin_type = ""

            if self.score_type or self.b.cleared_lines == 4:
                self.s.display_score_type(self.score_type, self.b.cleared_lines)
                if pyxel.frame_count % 480 == 0:
                    self.score_type = ""
                    
            if self.levelup:
                self.show_level_up(self.levelup)
                if pyxel.frame_count % 480 == 0:
                    self.levelup = ""
            
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
    
    # Add scores
    def add_scores(self):

        # Check if any lines were cleared
        if self.b.clear_lines():

            self.lines += self.b.cleared_lines

            if self.s.can_level_up(self.lines, self.level):
                self.level += 1
                self.block_fall_speed += 1
                self.levelup = f"LEVEL {self.level}!"

            # Check for any consecutive clears
            if self.b.consecutive_clears > 1:
                self.combos += 1
            
                # Check if the last move was a t-spin
                if self.s.is_valid_tspin(self.block_position_x, self.block_position_y, self.tetromino.shape, self.tetromino.centre, self.b.board, self.b.board_walls):
                    self.consecutive_spins += 1
                    self.spins += 1
                    self.spin_type = "T-SPIN!"
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=True, t_spin=True)

                # If no valid t-spins
                else:
                    self.score_type = "COMBO!"
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=True, t_spin=False)
            
            # If no consecutive clears (no combo)
            else:
                self.consecutive_spins = 0
                # Check if the last move was a t-spin
                if self.s.is_valid_tspin(self.block_position_x, self.block_position_y, self.tetromino.shape, self.tetromino.centre, self.b.board, self.b.board_walls):
                    self.spins += 1
                    self.spin_type = "T-SPIN!"
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=False, t_spin=True)
                else:
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=False, t_spin=False)

    # Generates a new tetromino
    def generate_new_block(self):
        self.tetromino = self.next_tetromino
        self.block_position_x = self.next_tetromino.mino["x"]
        self.block_position_y = self.next_tetromino.mino["y"]
        self.current_block_orientation = self.next_tetromino.current_orientation
        self.next_tetromino = Tetromino(C.BAG[random.randint(0, 6)])

    # Displays level up when player reaches next level
    def show_level_up(self, text):
        pyxel.text(C.WINDOW / 2 + 45, 70, text, pyxel.frame_count % 15)

    # Handles all text on UI
    def text(self):
        pyxel.FONT_HEIGHT = 12
        pyxel.FONT_WIDTH = 10
        pyxel.text(C.WINDOW / 2 + 45, 9, "HOLD: ", 10)
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


if __name__ == "__main__":
    Tetris()