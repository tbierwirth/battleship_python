import unittest

from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board

class BoardClass(unittest.TestCase):
    def test_it_exists(self):
        board = Board(4, 4)
        self.assertIsInstance(board, Board)
        self.assertEqual(len(board.cells), 16)
        self.assertIsInstance(board.cells["A1"], Cell)
        self.assertIsInstance(board.cells["D4"], Cell)
