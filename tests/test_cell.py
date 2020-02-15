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
        self.assertEqual(cell.isEmpty(), False)

    def test_fire_upon(self):
        cell = Cell("B4")
        cruiser = Ship("Cruiser", 3)
        cell.place_ship(cruiser)
        self.assertEqual(cell.isFiredUpon, False)
        cell.fire_upon()
        self.assertEqual(cell.isFiredUpon, True)
        self.assertEqual(cell.ship.health, 2)

    def test_render(self):
        cell_1 = Cell("B4")
        cell_2 = Cell("C3")
        cruiser = Ship("Cruiser", 3)
        self.assertEqual(cell_1.render(), ".")
        cell_1.fire_upon()
        self.assertEqual(cell_1.render(), "M")
