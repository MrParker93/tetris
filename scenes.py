import string
import pyxel
from constants import Scene, WINDOW

# Handles the different game scenes
class Scenes:
    def __init__(self, scene):
        self.x = 0
        self.y = 0
        self.scene = scene
        self.destroy = pyxel.tilemap(2)
        self.tetromino_width_and_height_in_tilemap = [
            (4, 1),
            (4, 2),
            (4, 2),
            (4, 2),
            (4, 2),
            (4, 2),
            (3, 2)
        ]

        if scene == Scene.TITLE_SCENE:
            self.scene = scene
            self.display = self.title_scene
        elif scene == Scene.CONTROLS_SCENE:
            self.scene = scene
            self.display = self.controls_scene
        elif scene == Scene.SETTINGS_SCENE:
            self.scene = scene
            self.display = self.settings_scene
        elif scene == Scene.SELECT_SPEED_SCENE:
            self.scene = scene
            self.display = self.select_fall_speed_scene
        elif scene == Scene.SELECT_TETRIS_SCENE:
            self.scene = scene
            self.display = self.select_tetris_scene
        elif scene == Scene.RANKINGS_SCENE:
            self.scene = scene
            self.display = self.show_rankings_scene
        elif scene == Scene.PAUSE_SCENE:
            self.scene = scene
            self.display = self.pause_scene
        elif scene == Scene.GAMEOVER_SCENE:
            self.scene = scene
            self.display = self.game_over_scene
        elif scene == Scene.ADD_NAME_SCENE:
            self.scene = scene
            self.display = self.add_player_name
        elif scene == Scene.ADD_SCORE_SCENE:
            self.scene = scene
            self.display = self.add_highscore
        elif scene == Scene.TEST_SCENE:
            self.scene = scene
            self.display = self.test_scene
        else:
            self.scene = Scene.PLAY_SCENE
        
    def title_scene(self):
        pyxel.cls(0)

        # Displaying tilemap(2) to draw to
        pyxel.bltm(20, 0, 2, 0, 16, WINDOW, WINDOW)

        # Displays each tetromino at the bottom of the window
        for index, v in enumerate(range(50, 70, 3)):
            pyxel.tilemap(2).blt(
                x=index * 4,   # The x coordinate relative to pyxel.bltm x coordinate. If pyxel.bltm x=3 and this x value = 5
                               # then the x value on screen will be 3 + 5 = 8. Moves 8px per 1.
                y=(32 * 0.95) + 1 if index == 0 else (32 * 0.95),   # The y coordinate relative to pyxel.bltm y coordinate. If pyxel.bltm y=3 and this y value = 5
                                                                      # then the y value on screen will be 3 + 5 = 8. Moves 8px per 1.
                tm=0, # The tilemap you want to reference. Can be any tilemap from 0-7 in the pyxeleditor.
                u=0,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                v=v,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                w=self.tetromino_width_and_height_in_tilemap[index][0],  # The width of the tile in the tilemap. 1 tile = 1, so w=10 means 10 tiles across
                h=self.tetromino_width_and_height_in_tilemap[index][1],  # The height of the tile in the tilemap. 1 tile = 1, so h=1 means 1 tile high.
            )

        # Display the title "TETRIS"
        pyxel.bltm((WINDOW / 2) - 92, WINDOW * 0.2, 0, 0, 72 * 8, WINDOW, 40)

        # Displays "START GAME"
        pyxel.bltm((WINDOW / 2) - 40, (WINDOW / 2), 1, 0, 16, 80, 8)

        # Displays "SETTINGS"
        pyxel.bltm((WINDOW / 2) - 32, (WINDOW / 2) + 16, 1, 0, 0, 64, 8)

        # Display "CONTROLS"
        pyxel.bltm((WINDOW / 2) - 32, (WINDOW / 2) + 32, 1, 0, 32, 64, 8)
        
        # Displays "RANKINGS"
        pyxel.bltm((WINDOW / 2) - 32, (WINDOW / 2) + 48, 1, 0, 64, 64, 8)

    def settings_scene(self):
        pyxel.cls(0)

        # Displaying tilemap(2) to draw to
        pyxel.bltm(20, 0, 2, 0, 16, WINDOW, WINDOW)

        # Displays each tetromino at the bottom of the window
        for index, v in enumerate(range(50, 70, 3)):
            pyxel.tilemap(2).blt(
                x=index * 4,   # The x coordinate relative to pyxel.bltm x coordinate. If pyxel.bltm x=3 and this x value = 5
                               # then the x value on screen will be 3 + 5 = 8. Moves 8px per 1.
                y=(32 * 0.95) + 1 if index == 0 else (32 * 0.95),   # The y coordinate relative to pyxel.bltm y coordinate. If pyxel.bltm y=3 and this y value = 5
                                                                      # then the y value on screen will be 3 + 5 = 8. Moves 8px per 1.
                tm=0, # The tilemap you want to reference. Can be any tilemap from 0-7 in the pyxeleditor.
                u=0,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                v=v,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                w=self.tetromino_width_and_height_in_tilemap[index][0],  # The width of the tile in the tilemap. 1 tile = 1, so w=10 means 10 tiles across
                h=self.tetromino_width_and_height_in_tilemap[index][1],  # The height of the tile in the tilemap. 1 tile = 1, so h=1 means 1 tile high.
            )

        # Displays "SETTINGS"
        pyxel.bltm((WINDOW / 2) - 32, WINDOW * 0.2, 1, 0, 0, 64, 8)

        # Displays "SELECT FALL SPEED"
        pyxel.bltm((WINDOW / 2) - 68, (WINDOW / 2), 1, 0, 48, 136, 8)
        
        # Displays "SELECT TETRIS"
        pyxel.bltm((WINDOW / 2) - 52, (WINDOW / 2) + 16, 1, 0, 80, 104, 8)

        # Displays "GO BACK"
        pyxel.bltm((WINDOW / 2) - 28, (WINDOW / 2) + 64, 1, 0, 176, 56, 8)
    
    def select_fall_speed_scene(self):
        pyxel.cls(0)

        # Displaying tilemap(2) to draw to
        pyxel.bltm(20, 0, 2, 0, 16, WINDOW, WINDOW)

        # Displays each tetromino at the bottom of the window
        for index, v in enumerate(range(50, 70, 3)):
            pyxel.tilemap(2).blt(
                x=index * 4,   # The x coordinate relative to pyxel.bltm x coordinate. If pyxel.bltm x=3 and this x value = 5
                               # then the x value on screen will be 3 + 5 = 8. Moves 8px per 1.
                y=(32 * 0.95) + 1 if index == 0 else (32 * 0.95),   # The y coordinate relative to pyxel.bltm y coordinate. If pyxel.bltm y=3 and this y value = 5
                                                                      # then the y value on screen will be 3 + 5 = 8. Moves 8px per 1.
                tm=0, # The tilemap you want to reference. Can be any tilemap from 0-7 in the pyxeleditor.
                u=0,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                v=v,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                w=self.tetromino_width_and_height_in_tilemap[index][0],  # The width of the tile in the tilemap. 1 tile = 1, so w=10 means 10 tiles across
                h=self.tetromino_width_and_height_in_tilemap[index][1],  # The height of the tile in the tilemap. 1 tile = 1, so h=1 means 1 tile high.
            )

        # Display "SPEED"
        pyxel.bltm((WINDOW / 2) - 20, (WINDOW / 2) - 32, 1, 0, 192, 40, 8)

        # Display arrow representing left and right to select speed
        pyxel.bltm(WINDOW * 0.20, (WINDOW / 2), 1, 40, 192, 8, 8)
        pyxel.bltm(WINDOW * 0.80 - 8, (WINDOW / 2), 1, 40, 192, -8, 8)
        
        # Displays "GO BACK"
        pyxel.bltm((WINDOW / 2) - 28, (WINDOW / 2) + 64, 1, 0, 176, 56, 8)

    def select_tetris_scene(self):
        pyxel.cls(0)
        
        # Displaying tilemap(2) to draw to
        pyxel.bltm(20, 0, 2, 0, 16, WINDOW, WINDOW)

        # Displays each tetromino at the bottom of the window
        for index, v in enumerate(range(50, 70, 3)):
            pyxel.tilemap(2).blt(
                x=index * 4,   # The x coordinate relative to pyxel.bltm x coordinate. If pyxel.bltm x=3 and this x value = 5
                               # then the x value on screen will be 3 + 5 = 8. Moves 8px per 1.
                y=(32 * 0.95) + 1 if index == 0 else (32 * 0.95),   # The y coordinate relative to pyxel.bltm y coordinate. If pyxel.bltm y=3 and this y value = 5
                                                                      # then the y value on screen will be 3 + 5 = 8. Moves 8px per 1.
                tm=0, # The tilemap you want to reference. Can be any tilemap from 0-7 in the pyxeleditor.
                u=0,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                v=v,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                w=self.tetromino_width_and_height_in_tilemap[index][0],  # The width of the tile in the tilemap. 1 tile = 1, so w=10 means 10 tiles across
                h=self.tetromino_width_and_height_in_tilemap[index][1],  # The height of the tile in the tilemap. 1 tile = 1, so h=1 means 1 tile high.
            )
        
        # Display "CHOOSE TETRIS MODE"
        pyxel.bltm((WINDOW / 2) - 72, WINDOW * 0.1, 1, 0, 208, 144, 8)
        
        # Display "TETRIS 1985"
        pyxel.bltm((WINDOW / 2) - 44, (WINDOW * 0.75) * 0.11 + (WINDOW * 0.2), 1, 0, 96, 88, 8)

        # Display "TETRIS WORLDS"
        pyxel.bltm((WINDOW / 2) - 52, (WINDOW * 0.75) * 0.22 + (WINDOW * 0.2), 1, 0, 144, 104, 8)

        # Display "TETRIS, NINTENDO"
        pyxel.bltm((WINDOW / 2) - 64, (WINDOW * 0.75) * 0.33 + (WINDOW * 0.2), 1, 0, 112, 128, 8)
        
        # Display "TETRIS: THE GRAND MASTER"
        pyxel.bltm((WINDOW / 2) - 96, (WINDOW * 0.75) * 0.44 + (WINDOW * 0.2), 1, 0, 128, 192, 8)
        
        # Display "TETRIS: THE GRAND MASTER 3"
        pyxel.bltm((WINDOW / 2) - 104, (WINDOW * 0.75) * 0.55 + (WINDOW * 0.2), 1, 0, 160, 208, 8)

        # Displays "GO BACK"
        pyxel.bltm((WINDOW / 2) - 28, (WINDOW / 2) + 64, 1, 0, 176, 56, 8)

    def show_rankings_scene(self):
        pyxel.cls(0)
        
        # Displaying tilemap(2) to draw to
        pyxel.bltm(20, 0, 2, 0, 16, WINDOW, WINDOW)

        # Displays each tetromino at the bottom of the window
        for index, v in enumerate(range(50, 70, 3)):
            pyxel.tilemap(2).blt(
                x=index * 4,   # The x coordinate relative to pyxel.bltm x coordinate. If pyxel.bltm x=3 and this x value = 5
                               # then the x value on screen will be 3 + 5 = 8. Moves 8px per 1.
                y=(32 * 0.95) + 1 if index == 0 else (32 * 0.95),   # The y coordinate relative to pyxel.bltm y coordinate. If pyxel.bltm y=3 and this y value = 5
                                                                      # then the y value on screen will be 3 + 5 = 8. Moves 8px per 1.
                tm=0, # The tilemap you want to reference. Can be any tilemap from 0-7 in the pyxeleditor.
                u=0,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                v=v,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                w=self.tetromino_width_and_height_in_tilemap[index][0],  # The width of the tile in the tilemap. 1 tile = 1, so w=10 means 10 tiles across
                h=self.tetromino_width_and_height_in_tilemap[index][1],  # The height of the tile in the tilemap. 1 tile = 1, so h=1 means 1 tile high.
            )

        # Draw border to display rankings
        pyxel.rectb(WINDOW * 0.1, WINDOW * 0.05, WINDOW * 0.8, WINDOW * 0.85, 7)
        
        # Displays "RANKINGS"
        pyxel.bltm((WINDOW / 2) - 32, (WINDOW * 0.04), 1, 0, 64, 64, 8)

        # Display mock rankings
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.1), 1, 0, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.2), 1, 16, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.3), 1, 32, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.4), 1, 48, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.5), 1, 64, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.6), 1, 80, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.7), 1, 96, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.8), 1, 112, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + ((WINDOW * 0.78) * 0.9), 1, 128, 224, 16, 8)
        pyxel.bltm(((WINDOW * 0.1) + 10), (WINDOW * 0.05) + (WINDOW * 0.78), 1, 144, 224, 24, 8)

        # Displays "GO BACK"
        pyxel.bltm((WINDOW / 2) - 28, WINDOW * 0.885, 1, 0, 176, 56, 8)

    def game_over_scene(self):
        pyxel.cls(0)

        # Display "GAMEOVER"
        pyxel.bltm((WINDOW / 2) - 64, WINDOW * 0.05, 2, 0, 0, 128, 32)

        # Draw border to display user achievements
        pyxel.rectb(WINDOW * 0.1, WINDOW * 0.15, WINDOW * 0.8, WINDOW * 0.5, 7)

        # Display "FINAL SCORE"
        pyxel.bltm((WINDOW * 0.1) + 10, (WINDOW * 0.1) + ((WINDOW * 0.9) * 0.1), 1, 0, 272, 96, 8)
        
        # Display "HIGHEST LEVEL"
        pyxel.bltm((WINDOW * 0.1) + 10, (WINDOW * 0.1) + ((WINDOW * 0.9) * 0.2), 1, 0, 336, 112, 8)
        
        # Display "LINES CLEARED"
        pyxel.bltm((WINDOW * 0.1) + 10, (WINDOW * 0.1) + ((WINDOW * 0.9) * 0.3), 1, 0, 288, 112, 8)
        
        # Display "COMBOS EARNED"
        pyxel.bltm((WINDOW * 0.1) + 10, (WINDOW * 0.1) + ((WINDOW * 0.9) * 0.4), 1, 0, 304, 112, 8)
        
        # Display "SPINS EXECUTED"
        pyxel.bltm((WINDOW * 0.1) + 10, (WINDOW * 0.1) + ((WINDOW * 0.9) * 0.5), 1, 0, 320, 120, 8)

        # Display "RANKINGS"
        pyxel.bltm((WINDOW / 2) - 32, (WINDOW * 0.2) + ((WINDOW * 0.9) * 0.55), 1, 0, 64, 64, 8)

        # Display "ADD HIGHSCORE"
        pyxel.bltm((WINDOW / 2) - 52, (WINDOW * 0.2) + ((WINDOW * 0.9) * 0.65), 1, 0, 240, 104, 8)
        
        # Display "TITLE SCREEN"
        pyxel.bltm((WINDOW / 2) - 48, (WINDOW * 0.2) + ((WINDOW * 0.9) * 0.75), 1, 0, 256, 96, 8)

    def pause_scene(self):
        pyxel.cls(0)

        # Displays "PAUSED"
        pyxel.text((WINDOW / 2) - 10, WINDOW * 0.25, "PAUSED", pyxel.frame_count % 9)

        # Display "RESUME"
        pyxel.bltm((WINDOW / 2) - 24, WINDOW * 0.45, 1, 0, 352, 48, 8)
        
        # Display "CONTROLS"
        pyxel.bltm((WINDOW / 2) - 32, WINDOW * 0.55, 1, 0, 32, 64, 8)

    def controls_scene(self):
        pyxel.cls(0)

         # Displaying tilemap(2) to draw to
        pyxel.bltm(20, 0, 2, 0, 16, WINDOW, WINDOW)

        # Displays each tetromino at the bottom of the window
        for index, v in enumerate(range(50, 70, 3)):
            pyxel.tilemap(2).blt(
                x=index * 4,   # The x coordinate relative to pyxel.bltm x coordinate. If pyxel.bltm x=3 and this x value = 5
                               # then the x value on screen will be 3 + 5 = 8. Moves 8px per 1.
                y=(32 * 0.95) + 1 if index == 0 else (32 * 0.95),   # The y coordinate relative to pyxel.bltm y coordinate. If pyxel.bltm y=3 and this y value = 5
                                                                      # then the y value on screen will be 3 + 5 = 8. Moves 8px per 1.
                tm=0, # The tilemap you want to reference. Can be any tilemap from 0-7 in the pyxeleditor.
                u=0,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                v=v,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                w=self.tetromino_width_and_height_in_tilemap[index][0],  # The width of the tile in the tilemap. 1 tile = 1, so w=10 means 10 tiles across
                h=self.tetromino_width_and_height_in_tilemap[index][1],  # The height of the tile in the tilemap. 1 tile = 1, so h=1 means 1 tile high.
            )

        # Display "CONTROLS"
        pyxel.bltm((WINDOW / 2) - 32, WINDOW * 0.1, 1, 0, 32, 64, 8)

        # Display "MOVE LEFT"
        pyxel.bltm((WINDOW / 2) - 68, (WINDOW * 0.1) + ((WINDOW * 0.75) * 0.125), 1, 0, 368, 136, 8)

        # Display "MOVE RIGHT"
        pyxel.bltm((WINDOW / 2) - 68, (WINDOW * 0.1) + ((WINDOW * 0.75) * 0.25), 1, 0, 384, 136, 8)

        # Display "SOFT DROP"
        pyxel.bltm((WINDOW / 2) - 68, (WINDOW * 0.1) + ((WINDOW * 0.75) * 0.375), 1, 0, 400, 136, 8)

        # Display "HARD DROP"
        pyxel.bltm((WINDOW / 2) - 68, (WINDOW * 0.1) + ((WINDOW * 0.75) * 0.50), 1, 0, 416, 136, 8)

        # Display "ROTATE LEFT"
        pyxel.bltm((WINDOW / 2) - 68, (WINDOW * 0.1) + ((WINDOW * 0.75) * 0.625), 1, 0, 432, 136, 8)

        # Display "ROTATE RIGHT"
        pyxel.bltm((WINDOW / 2) - 68, (WINDOW * 0.1) + ((WINDOW * 0.75) * 0.750), 1, 0, 448, 136, 8)

        # Display "HOLD TETROMINO"
        pyxel.bltm((WINDOW / 2) - 68, (WINDOW * 0.1) + ((WINDOW * 0.75) * 0.875), 1, 0, 464, 136, 8)

        # Displays "GO BACK"
        pyxel.bltm((WINDOW / 2) - 28, WINDOW * 0.885, 1, 0, 176, 56, 8)
        
    def add_highscore(self, score, lines, combos, spins, name):
        # Will be linked to a database to store player names and stats
        # Initially store names and scores in a csv or txt file
        # Users will be able to add any name they want
        pass

    def add_player_name(self, char="", letter_count=0):
        pyxel.cls(0)

        # Displaying tilemap(2) to draw to
        pyxel.bltm(20, 0, 2, 0, 16, WINDOW, WINDOW)

        # Displays each tetromino at the bottom of the window
        for index, v in enumerate(range(50, 70, 3)):
            pyxel.tilemap(2).blt(
                x=index * 4,   # The x coordinate relative to pyxel.bltm x coordinate. If pyxel.bltm x=3 and this x value = 5
                               # then the x value on screen will be 3 + 5 = 8. Moves 8px per 1.
                y=(32 * 0.95) + 1 if index == 0 else (32 * 0.95),   # The y coordinate relative to pyxel.bltm y coordinate. If pyxel.bltm y=3 and this y value = 5
                                                                      # then the y value on screen will be 3 + 5 = 8. Moves 8px per 1.
                tm=0, # The tilemap you want to reference. Can be any tilemap from 0-7 in the pyxeleditor.
                u=0,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                v=v,  # The (x, y) coordinates of the TOP LEFT corner of the tile in the tilemap. (x, y) maps like this -> (u, v)
                w=self.tetromino_width_and_height_in_tilemap[index][0],  # The width of the tile in the tilemap. 1 tile = 1, so w=10 means 10 tiles across
                h=self.tetromino_width_and_height_in_tilemap[index][1],  # The height of the tile in the tilemap. 1 tile = 1, so h=1 means 1 tile high.
            )

        # Corresponding tile coordinates in the tilemap to each character
        tilemap_letter_references = {
            "A": (0, 0),
            "B": (1, 0),
            "C": (0, 1),
            "D": (1, 1),   
            "E": (0, 2),
            "F": (1, 2),
            "G": (0, 3),
            "H": (1, 3),
            "I": (0, 4),
            "J": (1, 4),
            "K": (0, 5),
            "L": (1, 5),
            "M": (0, 6),
            "N": (1, 6),
            "O": (0, 7),
            "P": (1, 7),
            "Q": (0, 8),
            "R": (1, 8),
            "S": (0, 9),
            "T": (1, 9),
            "U": (0, 10),
            "V": (1, 10),
            "W": (0, 11),
            "X": (1, 11),
            "Y": (0, 12),
            "Z": (1, 12),
            "0": (0, 13),
            "1": (1, 13),
            "2": (0, 14),
            "3": (1, 14),
            "4": (0, 15),
            "5": (1, 15),
            "6": (0, 16),
            "7": (1, 16),
            "8": (0, 17),
            "9": (1, 17)
        }

        # Display "ENTER YOUR NAME"
        pyxel.bltm((WINDOW / 2) - 60, WINDOW * 0.25, 1, 0, 480, 120, 8)

        # Possible characters to spell name
        pyxel.blt(WINDOW / 2 - 64, WINDOW / 2 - 30, 1, 16, 0, 8, 8)
        pyxel.blt(WINDOW / 2 - 52, WINDOW / 2 - 30, 1, 24, 0, 8, 8)
        pyxel.blt(WINDOW / 2 - 40, WINDOW / 2 - 30, 1, 16, 8, 8, 8)
        pyxel.blt(WINDOW / 2 - 28, WINDOW / 2 - 30, 1, 24, 8, 8, 8)
        pyxel.blt(WINDOW / 2 - 16, WINDOW / 2 - 30, 1, 16, 16, 8, 8)
        pyxel.blt(WINDOW / 2 - 4, WINDOW / 2 - 30, 1, 24, 16, 8, 8)
        pyxel.blt(WINDOW / 2 + 8, WINDOW / 2 - 30, 1, 16, 24, 8, 8)
        pyxel.blt(WINDOW / 2 + 20, WINDOW / 2 - 30, 1, 24, 24, 8, 8)
        pyxel.blt(WINDOW / 2 + 32, WINDOW / 2 - 30, 1, 16, 32, 8, 8)
        pyxel.blt(WINDOW / 2 + 44, WINDOW / 2 - 30, 1, 24, 32, 8, 8)
        pyxel.blt(WINDOW / 2 + 56, WINDOW / 2 - 30, 1, 16, 40, 8, 8)
        pyxel.blt(WINDOW / 2 - 64, WINDOW / 2 - 15, 1, 24, 40, 8, 8)
        pyxel.blt(WINDOW / 2 - 52, WINDOW / 2 - 15, 1, 16, 48, 8, 8)
        pyxel.blt(WINDOW / 2 - 40, WINDOW / 2 - 15, 1, 24, 48, 8, 8)
        pyxel.blt(WINDOW / 2 - 28, WINDOW / 2 - 15, 1, 16, 56, 8, 8)
        pyxel.blt(WINDOW / 2 - 16, WINDOW / 2 - 15, 1, 24, 56, 8, 8)
        pyxel.blt(WINDOW / 2 - 4, WINDOW / 2 - 15, 1, 16, 64, 8, 8)
        pyxel.blt(WINDOW / 2 + 8, WINDOW / 2 - 15, 1, 24, 64, 8, 8)
        pyxel.blt(WINDOW / 2 + 20, WINDOW / 2 - 15, 1, 16, 72, 8, 8)
        pyxel.blt(WINDOW / 2 + 32, WINDOW / 2 - 15, 1, 24, 72, 8, 8)
        pyxel.blt(WINDOW / 2 + 44, WINDOW / 2 - 15, 1, 16, 80, 8, 8)
        pyxel.blt(WINDOW / 2 + 56, WINDOW / 2 - 15, 1, 24, 80, 8, 8)
        pyxel.blt(WINDOW / 2 - 64, WINDOW / 2, 1, 16, 88, 8, 8)
        pyxel.blt(WINDOW / 2 - 52, WINDOW / 2, 1, 24, 88, 8, 8)
        pyxel.blt(WINDOW / 2 - 40, WINDOW / 2, 1, 16, 96, 8, 8)
        pyxel.blt(WINDOW / 2 - 28, WINDOW / 2, 1, 24, 96, 8, 8)
        pyxel.blt(WINDOW / 2 - 16, WINDOW / 2, 1, 16, 104, 8, 8)
        pyxel.blt(WINDOW / 2 - 4, WINDOW / 2, 1, 24, 104, 8, 8)
        pyxel.blt(WINDOW / 2 + 8, WINDOW / 2, 1, 16, 112, 8, 8)
        pyxel.blt(WINDOW / 2 + 20, WINDOW / 2, 1, 24, 112, 8, 8)
        pyxel.blt(WINDOW / 2 + 32, WINDOW / 2, 1, 16, 120, 8, 8)
        pyxel.blt(WINDOW / 2 + 44, WINDOW / 2, 1, 24, 120, 8, 8)
        pyxel.blt(WINDOW / 2 + 56, WINDOW / 2, 1, 16, 128, 8, 8)
        pyxel.blt(WINDOW / 2 - 64, WINDOW / 2 + 15, 1, 24, 128, 8, 8)
        pyxel.blt(WINDOW / 2 - 52, WINDOW / 2 + 15, 1, 16, 136, 8, 8)
        pyxel.blt(WINDOW/2 - 40, WINDOW / 2 + 15, 1, 24, 136, 8, 8)

        # Underscores to show user how long the name should be
        pyxel.blt(WINDOW / 2 - 12, WINDOW / 2 + 50, 1, 16, 168, 8, 8)
        pyxel.blt(WINDOW / 2 - 4, WINDOW / 2 + 50, 1, 16, 168, 8, 8)
        pyxel.blt(WINDOW / 2 + 4, WINDOW / 2 + 50, 1, 16, 168, 8, 8)

        
        # The users chosen name will display here
        pyxel.bltm(WINDOW / 2 - 12, WINDOW / 2 + 45, 3, 8 * 2, 0, 3 * 8, 1 * 8, 0)

        # Add a character to player name
        if letter_count == 1:
            pyxel.tilemap(3).pset(2, 0, pyxel.tilemap(3).pget(tilemap_letter_references[char][0], tilemap_letter_references[char][1]))

        elif letter_count == 2:
            pyxel.tilemap(3).pset(3, 0, pyxel.tilemap(3).pget(tilemap_letter_references[char][0], tilemap_letter_references[char][1]))

        elif letter_count == 3:
            pyxel.tilemap(3).pset(4, 0, pyxel.tilemap(3).pget(tilemap_letter_references[char][0], tilemap_letter_references[char][1]))

        # Displays "PRESS ENTER TO START GAME!"
        pyxel.bltm((WINDOW / 2) - 84, (WINDOW / 2) + 70, 1, 0, 512, 168, 8)

    def test_scene(self):
        pyxel.cls(0)
