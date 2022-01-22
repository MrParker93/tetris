import pyxel
import constants as C


# Handles all movements
class Move:
    def __init__(self, x, y, orientation, mino, board):
        self.mino = mino
        self.board = board
        self.x = x
        self.y = y
        self.orientation = orientation

    def move_left(self):
        if not self.left_collision(self.mino, self.x, self.y, self.orientation):
            self.x -= 1
            return self.x
        return self.x

    def move_right(self):
        if not self.right_collision(self.mino, self.x, self.y, self.orientation):
            self.x += 1
            return self.x
        return self.x

    def move_down(self):
        if not self.bottom_collision(self.mino, self.x, self.y, self.orientation):
            self.y += 1
            return self.y
        return self.y

    def hard_drop(self):
        while not self.bottom_collision(self.mino, self.x, self.y, self.orientation):
            self.y += 1
        return self.y

    def rotate_right(self):
        if self.orientation == 3:
            self.orientation = 0
            return self.orientation
        else:
            self.orientation += 1
            return self.orientation
    
    def rotate_left(self):
        if self.orientation == 0:
            self.orientation = 3
            return self.orientation
        else:
            self.orientation -= 1
            return self.orientation

    def bottom_collision(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]

        for row in range(4):
            for col in range(4):

                if block[row][col] != 0:
                    if row + y + 1 > 26:
                        return True

                    if self.board[row + y + 1][col + x] != 0:
                        return True
        return False

    def left_collision(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]

        for row in range(4):
            for col in range(4):

                if block[row][col] != 0:
                    if col + x - 1 < 0:
                        return True
                    elif self.board[row + y][col + x - 1] != 0:
                        return True
        return False

    def right_collision(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]

        for row in range(4):
            for col in range(4):

                if block[row][col] != 0:
                    if col + x + 1 > C.BOARDWIDTH - 1:
                        return True
                    elif self.board[row + y][col + x + 1] != 0:
                        return True
        return False

    def above_collision(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    if self.board[row + y - 1][col + x] != 0:
                        return True
        return False

    def can_rotate(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]
        
        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    if row + y > 26 or col + x < 0 or col + x > C.BOARDWIDTH - 1:
                        return False
                    
                    elif self.board[row + y][col + x] != 0:
                        return False
        return True

    def check_if_locked(self, x, y, mino, orientation):
        return self.left_collision(mino, x, y, orientation) and self.right_collision(mino, x, y, orientation) \
            and self.above_collision(mino, x, y, orientation)
