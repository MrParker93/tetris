import pyxel
import constants as C
from copy import deepcopy


# Handles board logic
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.grid = deepcopy(self.board)
    
    # Adds tetromino to board
    def drop_block(self, x, y, mino, orientation):
        block = mino["block"][orientation]
        image_map_x = mino["u"]  # x coordinate of coinciding tetromino in the image map pyxeleditor
        image_map_y = mino["v"]  # y coordinate of coinciding tetromino in the image map pyxeleditor

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    temp_row = row * 8
                    temp_col = col * 8
                    self.grid[row + y][col + x] = block[row][col]
                    pyxel.blt(x + temp_col, y + temp_row, 0, image_map_x + temp_col, image_map_y + temp_row, 8, 8)
    
    # Shows where the tetromino will land on the board
    def drop_block_estimate(self, x, y, mino, orientation):
        block = mino["block"][orientation]

        temp_x, temp_y = x, y

        while not self.detect_collision(temp_x, temp_y, mino, orientation):
            temp_y += 1

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    self.grid[row + temp_y][col + temp_x] = 1

    # Draws grid to screen
    def draw_board(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] != 0:
                    pyxel.rect(col * C.GRID_SIZE + 10, row * C.GRID_SIZE + 10, C.GRID_SIZE, C.GRID_SIZE, self.grid[row][col])

    # Checks whether the tetromino collides with the floor or another tetromino
    def detect_collision(self, x, y, mino, orientation):
        block = mino["block"][orientation]

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:

                    if row + y + 1 > 20:
                        return True
                    elif self.board[row + y + 1][col + x] != 0 and self.board[row + y + 1][col + x] != 1:
                        return True
        return False