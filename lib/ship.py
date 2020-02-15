class Ship(object):
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length

    def is_sunk(self):
        if self.health > 0:
            return False
        elif self.heatlh <= 0:
            return True
