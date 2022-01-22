import pyxel
import random
from ui import UI
import constants as C
from board import Board
from score import Score
from copy import copy, deepcopy
from movement import Move
from scenes import Scenes
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
        self.current_scene = Scenes(Scene.TITLE_SCENE)
        self.lock_delay = C.LOCK_DELAY
        self.block_fall_speed = C.FALL_SPEED
        self.s = Score()
        self.ui = UI()
        self.menu_selector_position = ((C.WINDOW / 2) + 50, C.WINDOW / 2)
        self.level = self.s.level
        self.levelup = ""
        self.score = self.s.score
        self.lines = self.s.lines
        self.combos = self.s.combos
        self.spins = self.s.spins
        self.consecutive_spins = 0
        self.is_spin = False
        self.is_tetris = False
        self.is_combo = False
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
        if pyxel.btnp(pyxel.KEY_P):
            if self.state == "running" and not self.is_gameover and self.current_scene.scene == Scene.PLAY_SCENE:
                self.state = "paused"
            else:
                self.state = "running"
                self.current_scene = Scenes(Scene.PLAY_SCENE)

        if self.state == "paused":
            # Navigate the pause scene
            if self.current_scene.scene == Scene.PAUSE_SCENE:
                if pyxel.btnp(pyxel.KEY_DOWN, 15, 2) and not pyxel.btn(pyxel.KEY_UP):
                    if self.menu_selector_position[1] == (C.WINDOW / 2):
                        self.menu_selector_position = (self.menu_selector_position[0], self.menu_selector_position[1] + 26)

                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 26:
                        self.menu_selector_position = (self.menu_selector_position[0], (C.WINDOW / 2))
                
                if pyxel.btnp(pyxel.KEY_UP, 15, 2) and not pyxel.btn(pyxel.KEY_DOWN):
                    if self.menu_selector_position[1] == (C.WINDOW / 2):
                        self.menu_selector_position = (self.menu_selector_position[0], (C.WINDOW / 2) + 26)

                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 26:
                        self.menu_selector_position = (self.menu_selector_position[0], (C.WINDOW / 2))

                if self.menu_selector_position[1] == (C.WINDOW / 2):
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        self.state = "running"
                        self.current_scene = Scenes(Scene.PLAY_SCENE)

                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 26:
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        self.menu_selector_position = ((C.WINDOW / 2) + 38, (C.WINDOW * 0.885))
                        self.current_scene = Scenes(Scene.CONTROLS_SCENE)

            # Navigate the controls scene
            if self.current_scene.scene == Scene.CONTROLS_SCENE:
                if self.menu_selector_position[1] == (C.WINDOW * 0.885):
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        if pyxel.frame_count % 5 == 0:
                            self.menu_selector_position = ((C.WINDOW / 2) + 50, C.WINDOW / 2)
                            self.current_scene = Scenes(Scene.PAUSE_SCENE)

        if self.state == "stopped":
        # Navigating gameover scenes
            if self.current_scene.scene == Scene.GAMEOVER_SCENE:
                if pyxel.btnp(pyxel.KEY_DOWN, 15, 2) and not pyxel.btn(pyxel.KEY_UP):
                    if self.menu_selector_position[1] == (C.WINDOW / 2):
                        self.menu_selector_position = (self.menu_selector_position[0] + 8, self.menu_selector_position[1] + 23)
                    
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 23:
                        self.menu_selector_position = (self.menu_selector_position[0] + 8, self.menu_selector_position[1] + 23)
                    
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 46:
                        self.menu_selector_position = (self.menu_selector_position[0] - 16, (C.WINDOW / 2))
                
                if pyxel.btnp(pyxel.KEY_UP, 15, 2) and not pyxel.btn(pyxel.KEY_DOWN):
                    if self.menu_selector_position[1] == (C.WINDOW / 2):
                        self.menu_selector_position = (self.menu_selector_position[0] + 16, self.menu_selector_position[1] + 46)
                    
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 23:
                        self.menu_selector_position = (self.menu_selector_position[0] - 8, self.menu_selector_position[1] - 23)
                    
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 46:
                        self.menu_selector_position = (self.menu_selector_position[0] - 8, self.menu_selector_position[1] - 23)

                if self.menu_selector_position[1] == (C.WINDOW / 2):
                    if pyxel.btn(pyxel.KEY_SPACE):
                        if pyxel.frame_count % 10 == 0:
                            self.menu_selector_position = ((C.WINDOW / 2) + 38, (C.WINDOW * 0.885))
                            self.current_scene = Scenes(Scene.RANKINGS_SCENE)

                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 23:
                    if pyxel.btnp(pyxel.KEY_SPACE):
                        self.current_scene = Scenes(Scene.PLAY_SCENE)
                        self.state = "running"
                    
                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 46:
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        self.reset()
                
            # Navigate the rankings scene
            if self.current_scene.scene == Scene.RANKINGS_SCENE:
                if self.menu_selector_position[1] == (C.WINDOW * 0.885):
                    if pyxel.btnp(pyxel.KEY_SPACE):
                        self.menu_selector_position = ((C.WINDOW / 2) + 50, C.WINDOW / 2)
                        self.current_scene = Scenes(Scene.GAMEOVER_SCENE)

        # Navigating all scenes
        if self.state == "running":

            # Navigating the title scene
            if self.current_scene.scene == Scene.TITLE_SCENE:

                # Ensure the arrow rests to the top or bottom selection when it reaches the last/first option
                if pyxel.btnp(pyxel.KEY_DOWN, 15, 2) and not pyxel.btn(pyxel.KEY_UP):
                    self.menu_selector_position = (self.menu_selector_position[0], self.menu_selector_position[1] + 16)
                    if self.menu_selector_position[1] > ((C.WINDOW / 2) + 48):
                        self.menu_selector_position = (self.menu_selector_position[0], (C.WINDOW / 2))

                if pyxel.btnp(pyxel.KEY_UP, 15, 2) and not pyxel.btn(pyxel.KEY_DOWN):
                    self.menu_selector_position = (self.menu_selector_position[0], self.menu_selector_position[1] - 16)
                    if self.menu_selector_position[1] < (C.WINDOW / 2):
                        self.menu_selector_position = (self.menu_selector_position[0], (C.WINDOW / 2) + 48)

                # Navigate to other scenes based on arrow position
                if self.menu_selector_position[1] == (C.WINDOW / 2):
                    if pyxel.btn(pyxel.KEY_SPACE):
                        if pyxel.frame_count % 10 == 0:
                            self.current_scene = Scenes(Scene.PLAY_SCENE)
                
                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 16:
                    if pyxel.btn(pyxel.KEY_SPACE):
                        if pyxel.frame_count % 10 == 0:
                            self.current_scene = Scenes(Scene.SETTINGS_SCENE)

                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 32:
                    if pyxel.btn(pyxel.KEY_SPACE):
                        if pyxel.frame_count % 10 == 0:
                            self.menu_selector_position = ((C.WINDOW / 2) + 38, (C.WINDOW * 0.885))
                            self.current_scene = Scenes(Scene.CONTROLS_SCENE)

                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 48:
                    if pyxel.btn(pyxel.KEY_SPACE):
                        if pyxel.frame_count % 10 == 0:
                            self.menu_selector_position = ((C.WINDOW / 2) + 38, (C.WINDOW * 0.885))
                            self.current_scene = Scenes(Scene.RANKINGS_SCENE)

            # Navigating the settings scene
            if self.current_scene.scene == Scene.SETTINGS_SCENE:
                if pyxel.btnp(pyxel.KEY_DOWN, 15, 2) and not pyxel.btn(pyxel.KEY_UP):
                    if self.menu_selector_position[1] == (C.WINDOW / 2) + 16:
                        self.menu_selector_position = (self.menu_selector_position[0] - 10, self.menu_selector_position[1] + 16)

                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 32:
                        self.menu_selector_position = (self.menu_selector_position[0] - 28, self.menu_selector_position[1] + 48)
                    
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 80:
                        self.menu_selector_position = (self.menu_selector_position[0] + 38, (C.WINDOW / 2) + 16)

                if pyxel.btnp(pyxel.KEY_UP, 15, 2) and not pyxel.btn(pyxel.KEY_DOWN):
                    if self.menu_selector_position[1] == (C.WINDOW / 2) + 16:
                        self.menu_selector_position = (self.menu_selector_position[0] - 38, (C.WINDOW / 2) + 80)
                    
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 32:
                        self.menu_selector_position = (self.menu_selector_position[0] + 10, self.menu_selector_position[1] - 16)
                        
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 80:
                        self.menu_selector_position = (self.menu_selector_position[0] + 28, self.menu_selector_position[1] - 48)
                
                if self.menu_selector_position[1] == (C.WINDOW / 2) + 16:
                    if pyxel.btnp(pyxel.KEY_SPACE, hold=300, repeat=300):
                            self.menu_selector_position = (self.menu_selector_position[0], self.menu_selector_position[1] + 48)
                            self.current_scene = Scenes(Scene.SELECT_SPEED_SCENE)
                    
                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 32:
                    if pyxel.btnp(pyxel.KEY_SPACE, hold=300, repeat=300):
                        self.menu_selector_position = (((C.WINDOW / 2) + 54), (C.WINDOW * 0.75) * 0.11 + (C.WINDOW * 0.2))
                        self.current_scene = Scenes(Scene.SELECT_TETRIS_SCENE)

                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 80:
                    if pyxel.btnr(pyxel.KEY_SPACE):
                            self.menu_selector_position = ((C.WINDOW / 2) + 50, C.WINDOW / 2)
                            self.current_scene = Scenes(Scene.TITLE_SCENE)
            
            # Navigating the select speed scene
            if self.current_scene.scene == Scene.SELECT_SPEED_SCENE:
                if pyxel.btnp(pyxel.KEY_LEFT):
                    self.block_fall_speed -= 1

                if pyxel.btnp(pyxel.KEY_RIGHT):
                    self.block_fall_speed += 1

                if self.block_fall_speed < 1:
                    self.block_fall_speed = 1

                elif self.block_fall_speed > 20:
                    self.block_fall_speed = 20
                
                if pyxel.frame_count % 2 == 0:
                    if pyxel.btnp(pyxel.KEY_SPACE, hold=300, repeat=300):
                        self.menu_selector_position = (((C.WINDOW / 2) + 48), (C.WINDOW / 2) + 16)
                        self.current_scene = Scenes(Scene.SETTINGS_SCENE)
            
            # Navigate the select tetris mode scene
            if self.current_scene.scene == Scene.SELECT_TETRIS_SCENE:
                if pyxel.btnp(pyxel.KEY_DOWN, 15, 2) and not pyxel.btn(pyxel.KEY_UP):
                    if self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.11 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] + 8, (C.WINDOW * 0.75) * 0.22 + (C.WINDOW * 0.2))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.22 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] + 12, (C.WINDOW * 0.75) * 0.33 + (C.WINDOW * 0.2))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.33 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] + 32, (C.WINDOW * 0.75) * 0.44 + (C.WINDOW * 0.2))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.44 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] + 8, (C.WINDOW * 0.75) * 0.55 + (C.WINDOW * 0.2))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.55 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] - 76, (C.WINDOW / 2) + 64)
                    
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 64:
                        self.menu_selector_position = (self.menu_selector_position[0] + 16, (C.WINDOW * 0.75) * 0.11 + (C.WINDOW * 0.2))

                if pyxel.btnp(pyxel.KEY_UP, 15, 2) and not pyxel.btn(pyxel.KEY_DOWN):
                    if self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.11 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] - 16, ((C.WINDOW / 2) + 64))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.22 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] - 8, (C.WINDOW * 0.75) * 0.11 + (C.WINDOW * 0.2))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.33 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] - 12, (C.WINDOW * 0.75) * 0.22 + (C.WINDOW * 0.2))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.44 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] - 32, (C.WINDOW * 0.75) * 0.33 + (C.WINDOW * 0.2))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.55 + (C.WINDOW * 0.2):
                        self.menu_selector_position = (self.menu_selector_position[0] - 8, (C.WINDOW * 0.75) * 0.44 + (C.WINDOW * 0.2))
                    
                    elif self.menu_selector_position[1] == (C.WINDOW / 2) + 64:
                        self.menu_selector_position = (self.menu_selector_position[0] + 76, (C.WINDOW * 0.75) * 0.55 + (C.WINDOW * 0.2))

                if self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.11 + (C.WINDOW * 0.2):
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        pass
                elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.22 + (C.WINDOW * 0.2):
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        pass
                elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.33 + (C.WINDOW * 0.2):
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        pass
                elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.44 + (C.WINDOW * 0.2):
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        pass
                elif self.menu_selector_position[1] == (C.WINDOW * 0.75) * 0.55 + (C.WINDOW * 0.2):
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        pass
                elif self.menu_selector_position[1] == (C.WINDOW / 2) + 64:
                    if pyxel.btnr(pyxel.KEY_SPACE):
                        self.menu_selector_position = (((C.WINDOW / 2) + 48), (C.WINDOW / 2) + 16)
                        self.current_scene = Scenes(Scene.SETTINGS_SCENE)

            # Navigate the controls scene
            if self.current_scene.scene == Scene.CONTROLS_SCENE:
                if self.menu_selector_position[1] == (C.WINDOW * 0.885):
                    if pyxel.btnp(pyxel.KEY_SPACE, hold=300, repeat=300):
                        self.menu_selector_position = ((C.WINDOW / 2) + 50, C.WINDOW / 2)
                        self.current_scene = Scenes(Scene.TITLE_SCENE)
            
            # Navigate the rankings scene
            if self.current_scene.scene == Scene.RANKINGS_SCENE:
                if self.menu_selector_position[1] == (C.WINDOW * 0.885):
                    if pyxel.btnp(pyxel.KEY_SPACE, hold=300, repeat=300):
                        self.menu_selector_position = ((C.WINDOW / 2) + 50, C.WINDOW / 2)
                        self.current_scene = Scenes(Scene.TITLE_SCENE)
                
            if self.current_scene.scene == Scene.TEST_SCENE:
                if pyxel.btn(pyxel.KEY_W):
                    if pyxel.frame_count % 10 == 0:
                        print("KEY W PRESSED")

                if pyxel.btnp(pyxel.KEY_T):
                    print("KEY T PRESSED")
                
                if pyxel.btnp(pyxel.KEY_Y, hold=1, repeat=0):
                    print("KEY Y PRESSED")
                
                if pyxel.btnr(pyxel.KEY_U):
                    print("KEY U RELEASED")

                if pyxel.btnv(pyxel.KEY_I):
                    print(pyxel.btnv(pyxel.KEY_I))
                        
            if self.current_scene.scene == Scene.PLAY_SCENE:
                
                # Makes the tetromino fall after a specific number of frames
                if pyxel.frame_count % int(60 / self.block_fall_speed) == 0:
                    if not self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                        self.block_position_y += 1
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                    else:
                        if pyxel.frame_count % self.lock_delay == 0:
                            self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                            # self.b.grid = self.b.board

                            if self.check_game_over():
                                self.is_gameover = True
                                self.state = "stopped"
                                self.current_scene = Scenes(Scene.GAMEOVER_SCENE)
                            self.add_scores()
                            self.generate_new_block()

                # Move the tetromino left
                if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                    if self.block_position_y > 0:
                        self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                        self.block_position_x = self.move.move_left()
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

                # Move the tetromino right
                if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                    if self.block_position_y > 0:
                        self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                        self.block_position_x = self.move.move_right()
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

                # Move the tetromino down
                if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                    if self.block_position_y > 1:
                        self.move = Move(self.block_position_x, self.block_position_y, self.current_block_orientation, self.tetromino, self.b.board)
                        self.block_position_y = self.move.move_down()
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                        
                        # Reward 1 point per cell when tetromino is soft dropped
                        if not self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                            self.score += 1

                        if pyxel.frame_count % self.lock_delay == 0:
                            if self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                                self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                                # self.b.grid = self.b.board

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
                        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

                        if pyxel.frame_count % self.lock_delay == 0:
                            if self.b.detect_collision(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation):
                                self.b.fix_block(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                                # self.b.grid = self.b.board
                                
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
                        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)
                        
                        # Check if the current position of the tetromino is locked in place
                        if self.move.check_if_locked(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation):
                            self.is_locked = True

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
                        self.b.drop_block_estimate(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation)
                        self.b.drop_block(self.block_position_x, self.block_position_y, self.tetromino.mino, self.current_block_orientation)

                        # Check if the current position of the tetromino is locked in place
                        if self.move.check_if_locked(self.block_position_x, self.block_position_y, self.tetromino, self.current_block_orientation):
                            self.is_locked = True

    # Draws the game every frame, runs at 60fps
    def draw(self):
        if self.current_scene.scene == Scene.TITLE_SCENE:
            self.current_scene.title_scene()
            self.navigate_scenes()
        elif self.current_scene.scene == Scene.SETTINGS_SCENE:
            self.current_scene.settings_scene()
            self.navigate_scenes()
        elif self.current_scene.scene == Scene.SELECT_SPEED_SCENE:
            self.current_scene.select_fall_speed_scene()
            self.navigate_scenes()
        elif self.current_scene.scene == Scene.SELECT_TETRIS_SCENE:
            self.current_scene.select_tetris_scene()
            self.navigate_scenes()
        elif self.current_scene.scene == Scene.RANKINGS_SCENE:
            self.current_scene.show_rankings_scene()
            self.navigate_scenes()
        elif self.current_scene.scene == Scene.GAMEOVER_SCENE:
            self.current_scene.game_over_scene()
            self.navigate_scenes()
        elif self.current_scene.scene == Scene.PAUSE_SCENE:
            self.current_scene.pause_scene()
            self.navigate_scenes()
        elif self.current_scene.scene == Scene.CONTROLS_SCENE:
            self.current_scene.controls_scene()
            self.navigate_scenes()
        elif self.current_scene.scene == Scene.TEST_SCENE:
            self.current_scene.test_scene() 
        elif self.current_scene.scene == Scene.PLAY_SCENE:
            pyxel.cls(0)  # Clears screen and sets background to black
            self.text()
            self.ui.draw_game_borders()
            self.b.draw_next(self.next_tetromino)
            self.b.draw_board(self.tetromino.mino, self.tetromino.estimate, self.tetromino.image_map_position, self.tetromino.current_orientation)

            if self.b.clear_lines():
                self.b.draw_destoryed_lines(self.b.destroyed_lines, self.b.board)

            if self.is_spin:
                self.s.display_spin_type(self.s.show_spin, self.s.consecutive_spins)
                if pyxel.frame_count % 480 == 0:
                    self.s.show_spin = ""
                    self.is_spin = False

            if self.is_combo or self.is_tetris:
                self.s.display_score_type(self.s.show_combo, self.b.cleared_lines)
                if pyxel.frame_count % 480 == 0:
                    self.s.show_combo = ""
                    self.s.show_tetris = ""
                    self.is_combo = False
                    self.is_tetris = False
                    
            if self.levelup:
                self.show_level_up(self.levelup)
                if pyxel.frame_count % 480 == 0:
                    self.levelup = ""
            
            # Pause screen
            if self.state == "paused":
                self.current_scene = Scenes(Scene.PAUSE_SCENE)

            # Game over screen
            if self.is_gameover:
                self.state = "stopped"  
                self.current_scene = Scenes(Scene.GAMEOVER_SCENE)

    # Navigate the title screen
    def navigate_scenes(self):
        if self.current_scene.scene == Scene.TITLE_SCENE:
            pyxel.blt(self.menu_selector_position[0], self.menu_selector_position[1], 1, 0, 8, 8, 8)
            
        if self.current_scene.scene == Scene.SETTINGS_SCENE:
            pyxel.blt((self.menu_selector_position[0] + 28), self.menu_selector_position[1] - 16, 1, 0, 8, 8, 8)

        if self.current_scene.scene == Scene.SELECT_SPEED_SCENE:
            pyxel.text(C.WINDOW / 2, C.WINDOW / 2, str(self.block_fall_speed), 7)
            pyxel.blt(self.menu_selector_position[0], self.menu_selector_position[1], 1, 0, 8, 8, 8)

        if self.current_scene.scene == Scene.SELECT_TETRIS_SCENE:
            pyxel.blt(self.menu_selector_position[0], self.menu_selector_position[1], 1, 0, 8, 8, 8)

        if self.current_scene.scene == Scene.RANKINGS_SCENE:
            pyxel.blt(self.menu_selector_position[0], self.menu_selector_position[1], 1, 0, 8, 8, 8)

        if self.current_scene.scene == Scene.CONTROLS_SCENE:
            pyxel.blt(self.menu_selector_position[0], self.menu_selector_position[1], 1, 0, 8, 8, 8)

        if self.current_scene.scene == Scene.PAUSE_SCENE:
            pyxel.blt(self.menu_selector_position[0] - 10, self.menu_selector_position[1] - 12.8, 1, 0, 8, 8, 8)

        if self.current_scene.scene == Scene.GAMEOVER_SCENE:
            pyxel.blt(self.menu_selector_position[0] - 8, self.menu_selector_position[1] + 50, 1, 0, 8, 8, 8)

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
                self.is_combo = True
                self.combos += 1
            
                # Check if the last move was a t-spin
                if self.is_locked and self.s.is_valid_tspin(self.block_position_x, self.block_position_y, self.tetromino.shape, self.tetromino.centre, self.b.board, self.b.board_walls):
                    self.is_spin = True
                    self.consecutive_spins += 1
                    self.spins += 1
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=True, t_spin=True, twist=False)

                # If no valid t-spins then check for other shape twists
                elif self.is_locked and self.tetromino.shape != "T":
                    self.is_spin = True
                    self.consecutive_spins += 1
                    self.spins += 1
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=True, t_spin=False, twist=True)

                # If no valid t-spins or twists
                else:
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=True, t_spin=False, twist=False)
            
            # If no consecutive clears (no combo)
            else:
                if self.b.cleared_lines == 4:
                    self.is_tetris = True

                # There was no consecutive spin so set this back to 0
                self.consecutive_spins = 0

                # Check if the last move was a t-spin
                if self.is_locked and self.s.is_valid_tspin(self.block_position_x, self.block_position_y, self.tetromino.shape, self.tetromino.centre, self.b.board, self.b.board_walls):
                    self.is_spin = True
                    self.spins += 1
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=False, t_spin=True, twist=False)

                # If no valid t-spins then chekc for other shape twists
                elif self.is_locked and self.tetromino.shape != "T":
                    self.is_spin = True
                    self.spins += 1
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=True, t_spin=False, twist=True)

                else:
                    self.score += self.s.add_points(self.b.cleared_lines, self.consecutive_spins, combo=False, t_spin=False)

    # Generates a new tetromino
    def generate_new_block(self):
        self.tetromino = self.next_tetromino
        self.block_position_x = self.next_tetromino.mino["x"]
        self.block_position_y = self.next_tetromino.mino["y"]
        self.current_block_orientation = self.next_tetromino.current_orientation
        self.next_tetromino = Tetromino(C.BAG[random.randint(0, 6)])
        self.is_locked = False

    # Displays level up when player reaches next level
    def show_level_up(self, text):
        pyxel.text(C.WINDOW / 2 + 1, 170, text, pyxel.frame_count % 15)

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


if __name__ == "__main__":
    Tetris()