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

    os.system('clear')

    pc_submarine = Ship("Submarine", 2)
    pc_cruiser = Ship("Cruiser", 3)
    npc_submarine = Ship("Submarine", 2)
    npc_cruiser = Ship("Cruiser", 3)

    while True:
        os.system('clear')
        print(player.render(True))
        sub_coords = input("Pick two empty coordinates for your submarine, space separated ('A1 A2') \n")
        if player.isValidPlacement(pc_submarine, sub_coords.split(' ')) == False:
            os.system('clear')
            print(player.render(True))
            print("Please pick empty coordinates that are consecutive and not diagonal")
        else:
            player.place(pc_submarine, sub_coords.split(' '))
            break

    while True:
        os.system('clear')
        print(player.render(True))
        cruiser_coords = input("Pick three empty coordinates, space separated ('A1 A2 A3') \n")
        if player.isValidPlacement(pc_cruiser, cruiser_coords.split(' ')) == False:
            os.system('clear')
            print(player.render(True))
            print("Please pick empty coordinates that are consecutive and not diagonal")
        else:
            player.place(pc_cruiser, cruiser_coords.split(' '))
            break
elif choice.lower() == "q":
    print("Quit")
else:
    print("Please pick a valid option")
