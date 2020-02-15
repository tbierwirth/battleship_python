import unittest
from lib.ship import Ship

class ShipClass(unittest.TestCase):
    def test_it_exists(self):
        cruiser = Ship("Cruiser", 3)
        self.assertIsInstance(cruiser, Ship)
        self.assertEqual(cruiser.name, "Cruiser")
        self.assertEqual(cruiser.length, 3)
        self.assertEqual(cruiser.health, 3)

    def test_ship_health(self):
        cruiser = Ship("Cruiser", 3)
        self.assertEqual(cruiser.is_sunk(), False)
