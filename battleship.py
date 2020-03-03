from colored import fg, bg, attr
import os
from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board

print ('%s Welcome to BATTLESHIP %s' % (fg(1), attr(0)))
choice = input("Press P to play or Q to quit \n")
if choice.lower() == "p":
    os.system('clear')
    while True:
        width = int(input("What width of board would you like to play with? \n"))
        if width not in range(4, 26):
            os.system('clear')
            print("Please enter a number greater than 4")
        else:
            break

    while True:
        height = int(input("What height of board would you like to play with? \n"))
        if height not in range(4, 26):
            os.system('clear')
            print("Please enter a number greater than 4")
        else:
            break
    player = Board(int(width), int(height))
    cpu = Board(int(width), int(height))
elif choice.lower() == "q":
    print("Quit")
else:
    print("Please pick a valid option")
