import os
import pytest
from .context import tetromino
from tetromino import Tetromino


class TestRotations:
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
        
    def test_T_tetromino_rotates_right(self, t_T):
        t_T.block = t_T.rotate_right()
        assert t_T.block == [[0, 2, 0, 0],
                             [0, 2, 2, 0],
                             [0, 2, 0, 0],
                             [0, 0, 0, 0]]

    def test_T_tetromino_rotates_left(self, t_T):
        t_T.block = t_T.rotate_left()
        assert t_T.block == [[0, 2, 0, 0],
                             [2, 2, 0, 0],
                             [0, 2, 0, 0],
                             [0, 0, 0, 0]]

    def test_T_tetromino_rotates_twice(self, t_T):
        t_T.block = t_T.rotate_left()
        t_T.block = t_T.rotate_left()
        assert t_T.block == [[0, 0, 0, 0],
                             [2, 2, 2, 0],
                             [0, 2, 0, 0],
                             [0, 0, 0, 0]]

    def test_I_tetromino_rotates_right(self, t_I):
        t_I.block = t_I.rotate_right()
        assert t_I.block == [[0, 0, 12, 0],
                             [0, 0, 12, 0],
                             [0, 0, 12, 0],
                             [0, 0, 12, 0]]

    def test_I_tetromino_rotate_left(self, t_I):
        t_I.block = t_I.rotate_left()
        assert t_I.block == [[0, 12, 0, 0],
                             [0, 12, 0, 0],
                             [0, 12, 0, 0],
                             [0, 12, 0, 0]]

    def test_I_tetromino_rotate_twice(self, t_I):
        t_I.block = t_I.rotate_right()
        t_I.block = t_I.rotate_right()
        assert t_I.block == [[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [12, 12, 12, 12],
                             [0, 0, 0, 0]]

    def test_O_tetromino_never_rotates(self, t_O):
        t_O.block = t_O.rotate_right()
        assert t_O.block == [[0, 10, 10, 0],
                             [0, 10, 10, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]

        t_O.block = t_O.rotate_left()
        assert t_O.block == [[0, 10, 10, 0],
                             [0, 10, 10, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]