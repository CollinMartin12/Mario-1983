import pyxel
import Constants
from Board import Board
from Player import Player

"""THIS is the Main.py that runs everything from our 
sprints to everything inside the board"""

board = Board()

# Initializes pyxel
pyxel.init(board.width, board.height, "Mario")  # type: ignore
# Loads the resource file
pyxel.load("my_resources.pyxres")


# Runs the game
pyxel.run(board.update, board.draw)



