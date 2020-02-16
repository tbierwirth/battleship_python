import string
from lib.cell import Cell

class Board(object):
    def __init__(self, width, height):
        self.cells = {}
        letters = list(string.ascii_uppercase)
        numbers = list(range(1, 26))
        for x in range(width):
            for y in range(height):
                self.cells[f"{letters[x]}{numbers[y]}"] = Cell(f"{letters[x]}{numbers[y]}")
