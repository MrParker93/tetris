import os
import pytest
from .context import tetromino, board

from board import Board
from tetromino import Tetromino


class TestBoard:
    @pytest.fixture
    def b(self):
        board = Board(6, 10)
        yield board

    @pytest.fixture
    def t(self):
        mino = Tetromino(5)
        mino.mino["x"] = 1
        mino.mino["y"] = 0
        yield mino

    def test_size_of_the_board(self, b):
        assert b.board == [[0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0]]

    def test_tetrominos_spawn_at_middle_top_of_the_board(self, b, t):
        b.drop_block(t.mino["x"], t.mino["y"], t.mino, t.current_orientation)
        assert b.grid == [[0, 0, 2, 0, 0, 0],
                          [0, 2, 2, 2, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]]

    def test_tetrominos_shows_estimate_parallel_to_current_position(self, b, t):
        b.drop_block(t.mino["x"], t.mino["y"], t.mino, t.current_orientation)
        b.drop_block_estimate(t.mino["x"], t.mino["y"], t.mino, t.current_orientation)
        assert b.grid == [[0, 0, 2, 0, 0, 0],
                          [0, 2, 2, 2, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0],
                          [0, 1, 1, 1, 0, 0]]