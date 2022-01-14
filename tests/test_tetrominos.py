import os
import pytest
from .context import tetromino
from tetromino import Tetromino

class TestTetrominos:
    @pytest.fixture
    def t_O(self):  # Tetromino O
        t = Tetromino(0)
        yield t

    @pytest.fixture
    def t_T(self):  # Tetromino T
        t = Tetromino(5)
        yield t

    @pytest.fixture
    def t_I(self):  # Tetromino I 
        t = Tetromino(6)
        yield t

    def test_O_tetromino_block_shape(self, t_O):
        assert t_O.block == [[0, 10, 10, 0],
                             [0, 10, 10, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]

    def test_T_tetromino_block_shape(self, t_T):
        assert t_T.block == [[0, 2, 0, 0],
                             [2, 2, 2, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]

    def test_I_tetromino_block_shape(self, t_I):
        assert t_I.block == [[0, 0, 0, 0],
                             [12, 12, 12, 12],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]
    