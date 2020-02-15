class Cell(object):
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None

    def isEmpty(self):
        if self.ship == None:
            return True
        elif self.ship != None:
            return False
