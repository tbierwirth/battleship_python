class Cell(object):
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None
        self.isFiredUpon = False

    def isEmpty(self):
        if self.ship == None:
            return True
        elif self.ship != None:
            return False

    def place_ship(self, ship):
        self.ship = ship

    def fire_upon(self):
        self.ship.hit()
        self.isFiredUpon = True
