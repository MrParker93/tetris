import pyxel
import constants as C
from copy import deepcopy


# Handles board logic
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.board_walls = self.add_board_walls()
        self.grid = deepcopy(self.board)
        self.cleared_lines = 0
        self.consecutive_clears = 0
    
    # Adds an extra board with walls and floors equal to -1 for extra collision detection
    def add_board_walls(self):

        # Create another board with 2 extra columns
        board = [[0] * (self.width + 2) for _ in range(self.height)]
        counter = 0

        # Add walls and floor in 2 extra columns and floor
        while counter < len(board):
            board[counter][0] = -1
            board[counter][len(board[0]) - 1] = -1
            if counter == 27:
                board[counter] = [-1] * len(board[0])
            counter += 1
        return board

    # Adds tetromino to board
    def drop_block(self, x, y, mino, orientation):
        block = mino["block"][orientation]

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    self.grid[row + y][col + x] = block[row][col]

    # Shows where the tetromino will land on the board
    def drop_block_estimate(self, x, y, mino, orientation):
        block = mino.mino["block"][orientation]
        image_map_x = mino.estimate[0]
        image_map_y = mino.estimate[1]

        temp_x, temp_y = x, y

        while not self.detect_collision(temp_x, temp_y, mino.mino, orientation):
            temp_y += 1

        # for row in range(4):
        #     for col in range(4):
        #         if block[row][col] != 0:
        #             self.grid[row + temp_y][col + temp_x] = block[row][col]

    # Draws grid to screen
    def draw_board(self, mino, estimate, image_position, orientation):
        image_map_x = image_position[0]
        image_map_y = image_position[1]
        estimate_image_map_x = estimate[0]
        estimate_image_map_y = estimate[1]

        # Returns row and column of block position in the grid as a tuple
        grid_coords = self.get_coordinates(self.grid)  

        # Gets the coordinates of the ghost tetromino on the grid
        grid_estimate_coords = grid_coords[-4:]

        # Returns row and column of each block in tetromino as a tuple
        block_coords = self.get_coordinates(mino["block"][orientation])  

        # Maps the grid and block coordinates in a list of tuples: [(grid_row, grid_col, block_row, block_col)]
        mapped_coords = list(map(lambda a, b: a + b, grid_coords, block_coords))

        counter = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] != 0:

                    # Set the block row and col to the corresponding value in the tuple
                    _, _, b_row, b_col = mapped_coords[counter]

                    # Get current block in the tetromino and * C.GRID_SIZE to reference pyxel editor coordinates
                    current_block_row = b_row * C.GRID_SIZE  
                    current_block_col = b_col * C.GRID_SIZE
                    
                    # if grid_estimate_coords:
                    #     # Set the ghost tetromino position on the grid (row, col) to corresponding value in the tuple
                    #     ghost_grid_row, ghost_grid_col = grid_estimate_coords[counter]
                        
                    #     # Draws the current tetromino's ghost on the grid
                    #     pyxel.blt(ghost_grid_col * C.GRID_SIZE + C.LEFTRIGHT_PADDING + 8, ghost_grid_row * C.GRID_SIZE + C.TOP_PADDING, 0, estimate_image_map_x + current_block_col, estimate_image_map_y + current_block_row, C.GRID_SIZE, C.GRID_SIZE)

                    # Draws the current tetromino on the grid
                    pyxel.blt(col * C.GRID_SIZE + C.LEFTRIGHT_PADDING + 8, row * C.GRID_SIZE + C.TOP_PADDING, 0, image_map_x + current_block_col, image_map_y + current_block_row, C.GRID_SIZE, C.GRID_SIZE)

                    if counter < 3:
                        counter += 1

    # Draw next tetromino to screen
    def draw_next(self, mino):
        block = mino.mino["block"][mino.current_orientation]
        image_map_x = mino.image_map_position[0]  # x coordinate of coinciding tetromino in the image map pyxeleditor
        image_map_y = mino.image_map_position[1]  # y coordinate of coinciding tetromino in the image map pyxeleditor

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    temp_row = row * 8
                    temp_col = col * 8
                    pyxel.blt(C.WINDOW / 2 + temp_col, 25 + temp_row, 0, image_map_x + temp_col, image_map_y + temp_row, 8, 8)

    # Gets the row and column of each non-zero value in the block/grid and returns it as a tuple
    def get_coordinates(self, two_d_list):
        coords = []
        for row in range(len(two_d_list)):
            for col in range(len(two_d_list[0])):
                if two_d_list[row][col] != 0:
                    coords.append((row, col))
        return coords

    # Checks whether the tetromino collides with the floor or another tetromino
    def detect_collision(self, x, y, mino, orientation):
        block = mino["block"][orientation]

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:

                    if row + y + 1 > 26:
                        return True
                    elif self.board[row + y + 1][col + x] != 0 and self.board[row + y + 1][col + x] != 1:
                        return True
        return False

    # Fixes the block in the current position and adds to the board
    def fix_block(self, x, y, mino, orientation):
        block = mino.mino["block"][orientation]

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    self.board[row + y][col + x] = block[row][col]
        

    # Clears a row if it's full
    def clear_lines(self):
        lines_to_clear = []

        # Loop through the board and check for full rows
        for index, row in enumerate(range(27)):
            if self.board[row].count(0) == 0:

                # Add the index of the full rows to a list
                lines_to_clear.append(index)


        if len(lines_to_clear) > 0:
            # each_block =  0
            for index in range(len(lines_to_clear)):
                # Remove the full row (clear)
                self.board.pop(lines_to_clear[index])

                # Add an empty row to the top of the board
                self.board.insert(2, [0] * C.BOARDWIDTH)
            
            self.cleared_lines = len(lines_to_clear)
            self.consecutive_clears += 1
            return True
        else:
            self.consecutive_clears = 0
            return False