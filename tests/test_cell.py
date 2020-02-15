import unittest
from lib.ship import Ship
from lib.cell import Cell

class CellClass(unittest.TestCase):
    def test_it_exists(self):
        cell = Cell("B4")
        self.assertEqual(cell.coordinate, "B4")
        self.assertEqual(cell.ship, None)
        self.assertEqual(cell.isEmpty(), True)

    def test_place_ship(self):
        cell = Cell("B4")
        cruiser = Ship("Cruiser", 3)
        cell.place_ship(cruiser)
        self.assertEqual(cell.ship, cruiser)
