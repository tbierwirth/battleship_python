import string
import re
from lib.cell import Cell

class Board(object):
    def __init__(self, width, height):
        self.cells = {}
        letters = list(string.ascii_uppercase)
        numbers = list(range(1, 26))
        for x in range(width):
            for y in range(height):
                self.cells[f"{letters[x]}{numbers[y]}"] = Cell(f"{letters[x]}{numbers[y]}")

    def isValidCoordinate(self, coordinate):
        if coordinate not in self.cells:
            return False
        else:
            return True

    def isValidPlacement(self, ship, coordinates):
        cells = list(self.cells)
        letters = []
        numbers = []
        empty = []
        for coordinate in coordinates:
            letter, number = coordinate
            letters.append(letter)
            numbers.append(number)
            empty.append(self.cells[coordinate].isEmpty())
        if ship.length == len(coordinates) and (len(set(numbers)) != len(set(letters))) and all(empty):
            if len(set(letters)) == 1 and len(set(numbers)) != 1:
                consecutive = []
                for i in range(len(numbers) - 1):
                    consecutive.append(int(numbers[i+1]) - int(numbers[i]) == 1)
                if all(consecutive):
                    return True
                else:
                    return False
            elif len(set(numbers)) == 1 and len(set(letters)) != 1:
                consecutive = []
                for i in range(len(letters) - 1):
                    consecutive.append(ord(letters[i+1]) - ord(letters[i]) == 1)
                if all(consecutive):
                    return True
                else:
                    return False
        else:
            return False

    def place(self, ship, coordinates):
        if self.isValidPlacement(ship, coordinates):
            for coordinate in coordinates:
                self.cells[coordinate].place_ship(ship)

    def render(self, reveal = False):
        letters = []
        numbers = []
        for cell in self.cells.items():
            letter = re.split('(\d+)',cell[0])[0]
            number = re.split('(\d+)', cell[0])[1]
            if letter not in letters:
                letters.append(letter)
            if number not in numbers:
                numbers.append(number)
        board = "  "
        for number in numbers:
            board += f"{number} "
        for letter in letters:
            board += f"\n{letter} "
            cells = dict(filter(lambda cell: letter in cell[0], self.cells.items()))
            for cell in cells:
                board += f"{self.cells[cell].render(reveal)} "
        return board
