import pyxel
import Constants
from Board import Board
from Player import Player


board = Board()

# Initializes pyxel
pyxel.init(board.width, board.height, "Mario")  # type: ignore
# Loads the resource file
pyxel.load("compact.pyxres")


# Runs the game
pyxel.run(board.update, board.draw)


