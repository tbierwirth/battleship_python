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
        self.isFiredUpon = True
        if self.isEmpty() == False:
            self.ship.hit()

    def render(self):
        if self.isEmpty() == True and self.isFiredUpon == False:
            return "."
        elif self.isEmpty() == True and self.isFiredUpon == True:
            return "M"
