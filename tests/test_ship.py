import unittest
from lib.ship import Ship

class ShipClass(unittest.TestCase):
    def test_it_exists(self):
        cruiser = Ship("Cruiser", 3)
        self.assertIsInstance(cruiser, Ship)
        self.assertEqual(cruiser.name, "Cruiser")
        self.assertEqual(cruiser.length, 3)
