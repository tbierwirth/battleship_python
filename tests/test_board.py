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

    def test_is_valid_coordinate(self):
        board = Board(4, 4)
        self.assertEqual(board.isValidCoordinate("A1"), True)
        self.assertEqual(board.isValidCoordinate("D4"), True)
        self.assertEqual(board.isValidCoordinate("A5"), False)
        self.assertEqual(board.isValidCoordinate("E1"), False)

    def test_is_valid_placement(self):
        board = Board(4, 4)
        cruiser = Ship("Cruiser", 3)
        submarine = Ship("Submarine", 2)
        self.assertEqual(board.isValidPlacement(cruiser, ["A1", "A2"]), False)
        self.assertEqual(board.isValidPlacement(submarine, ["A2", "A3", "A4"]), False)
        self.assertEqual(board.isValidPlacement(cruiser, ["A1", "A2", "A4"]), False)
        self.assertEqual(board.isValidPlacement(submarine, ["A1", "C1"]), False)
        self.assertEqual(board.isValidPlacement(cruiser, ["A3", "A2", "A1"]), False)
        self.assertEqual(board.isValidPlacement(submarine, ["C1", "B1"]), False)
        self.assertEqual(board.isValidPlacement(cruiser, ["A1", "B2", "C3"]), False)
        self.assertEqual(board.isValidPlacement(submarine, ["C2", "D3"]), False)
        self.assertEqual(board.isValidPlacement(submarine, ["A1", "A2"]), True)
        self.assertEqual(board.isValidPlacement(cruiser, ["B1", "C1", "D1"]), True)

    def test_placing_ship(self):
        board = Board(4, 4)
        cruiser = Ship("Cruiser", 3)
        submarine = Ship("Submarine", 2)
        board.place(cruiser, ["A1", "A2", "A3"])
        self.assertEqual(board.cells["A1"].ship, cruiser)
        self.assertEqual(board.cells["A2"].ship, cruiser)
        self.assertEqual(board.cells["A3"].ship, cruiser)
        self.assertTrue(board.cells["A1"].ship == board.cells["A3"].ship)
        # Test for overlap
        self.assertFalse(board.isValidPlacement(submarine, ["A1", "B1"]))

    def test_render_boad(self):
        board = Board(4, 4)
        cruiser = Ship("Cruiser", 3)
        board.place(cruiser, ["A1", "A2", "A3"])
        self.assertEqual(board.render(),  "  1 2 3 4 \nA . . . . \nB . . . . \nC . . . . \nD . . . . ")
        self.assertEqual(board.render(True),  "  1 2 3 4 \nA S S S . \nB . . . . \nC . . . . \nD . . . . ")
        board.cells['A1'].fire_upon()
        self.assertEqual(board.render(True),  "  1 2 3 4 \nA H S S . \nB . . . . \nC . . . . \nD . . . . ")
        board.cells['A2'].fire_upon()
        board.cells['A3'].fire_upon()
        self.assertEqual(board.render(True),  "  1 2 3 4 \nA X X X . \nB . . . . \nC . . . . \nD . . . . ")
