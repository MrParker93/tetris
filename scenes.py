import pyxel
import random
from constants import Scene, WINDOW

# Handles the different game scenes
class Scenes:
    def __init__(self, scene):
        self.x = random.randint(0, 256)
        self.y = random.randint(0, 256)
        self.all_tetrominos_from_tilemap = self.spawn_random_tetrominos()
        self.random_int = random.choice(self.all_tetrominos_from_tilemap)
        if scene == Scene.TITLE_SCENE:
            self.scene = scene
            self.display = self.title_scene()
        elif scene == Scene.PLAY_SCENE:
            self.scene = scene
            self.display = self.play_scene()
        else:
            self.scene = scene
            self.display = self.game_over_scene()
        
    def title_scene(self):
        pyxel.cls(0)
        pyxel.bltm(self.x, self.y, 1, 0, 8 * self.random_int, 32, 32)
        pyxel.bltm(self.x, self.y, 1, 0, 8 * self.random_int, 32, 32)
        pyxel.bltm(self.x, self.y, 1, 0, 8 * self.random_int, 32, 32)
        pyxel.bltm(self.x, self.y, 1, 0, 8 * self.random_int, 32, 32)
        pyxel.bltm((WINDOW / 2) - 92, WINDOW * 0.2, 1, 0, 0, 184, 40)
        self.y += 0.1

    def spawn_random_tetrominos(self):
        tetrominos = []
        for v in range(6, 82, 4):
            tetrominos.append(v)
        return tetrominos