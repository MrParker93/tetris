import pyxel
import constants as C


# Handles scoring
class Score:
    def __init__(self):
        self.level = C.LEVEL
        self.score = C.SCORE
        self.lines = C.LINES
        self.combos = C.COMBOS
        self.spins = C.SPINS
        self.consecutive_spins = 0
        self.spin_type = ""
        self.score_type = ""
    
    # Checks the conditions of the score and adds points accordingly 
    def add_points(self, lines_cleared, combo=False, t_spin=False):
        score = 0
        if lines_cleared != 0:
            if combo:
                self.score_type = "COMBO!"
                if t_spin and self.consecutive_spins > 0:
                    score += self.add_spins(lines_cleared, self.consecutive_spins)
                
                elif t_spin and self.consecutive_spins == 0:
                    score += self.add_spins(lines_cleared, self.consecutive_spins)

                elif not t_spin:
                    combo_multiplier = (lines_cleared * self.level) + (50 * self.level)
                    score += C.POINTS[str(lines_cleared)] * self.level + 1 + combo_multiplier
            else:
                score += C.POINTS[str(lines_cleared)] * self.level + 1
                if lines_cleared == 4:
                    self.score_type = "TETRIS!"
            return score
    
    # Checks conditions for level up and returns true if met
    def can_level_up(self, lines, level):
        return lines > level * 5

    # Checks if conditions are met for a t-spin and returns true
    def is_valid_tspin(self, x, y, shape, centre_block, board, board_walls):

        # Ensure the tetromino is the T shape
        if shape != "T":
            return False
        
        for row in range(len(board_walls)):
            for col in range(len(board[0])):
                if col != 0 and col != 11:
                    board_walls[row][col] = board[row][col - 1]
        
        print(*board_walls,sep="\n")
        print()
        print(*board,sep="\n")
        # Diagonally adjacent grids on the board relative to centre of the tetromino
        diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Get centre of the tetromino
        centre = (y + centre_block[0], x + centre_block[1])

        # If counter is 3 then t-spin is valid
        counter = 0

        for _x, _y in diagonals:
            try:
                if board[_y + centre[0]][_x + centre[1]] != 0:
                    counter += 1
            except IndexError:
                if board_walls[_y + centre[0]][_x + centre[1]] != 0:
                    counter += 1
        if counter > 2:
            # print(f"counter if true: {counter}")
            return True
        # print(f"counter if false: {counter}")
        return False

    
    # Handles adding t_spin points to score
    def add_spins(self, lines_cleared, consecutive_spins):
        score = 0
        if consecutive_spins > 0:
            if lines_cleared == 1:
                # Back 2 back t-spin single (equivalent to a t-spin double)
                score = C.T_SPIN["double"] * self.level
                self.spin_type = "BACK TO BACK T-SPIN SINGLE!"
            
            elif lines_cleared == 2:
                # Back 2 back t-spin double
                score = C.T_SPIN["b2b double"] * self.level
                self.spin_type = "BACK TO BACK T-SPIN DOUBLE!"
            
            elif lines_cleared == 3:
                # Back 2 back t-spin triple
                score = C.T_SPIN["b2b triple"] * self.level
                self.spin_type = "BACK TO BACK T-SPIN TRIPLE!"
        else:
            if lines_cleared == 1:
                # T-spin single
                score = C.T_SPIN["single"] * self.level
                self.spin_type = "T-SPIN SINGLE!"
            
            elif lines_cleared == 2:
                # T-spin double
                score = C.T_SPIN["double"] * self.level
                self.spin_type = "T-SPIN DOUBLE!"
            
            elif lines_cleared == 3:
                # T-spin triple
                score = C.T_SPIN["triple"] * self.level
                self.spin_type = "T-SPIN TRIPLE!"
        return score