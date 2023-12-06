import pyxel
import Constants
from Board import Board
from Player import Player

board = Board()

# Initializes pyxel
pyxel.init(board.width, board.height, "Mario")  # type: ignore
# Loads the resource file
pyxel.load("my_resource.pyxres")
# Runs the game
pyxel.run(board.update, board.draw)


    # game = Mario()
    board = Board(300, 300)
    pyxel.load("my_resource.pyxres")  # Load your .pyxel image file
    pyxel.run(board.update, board.draw)

if __name__ == "__main__":
    run_game()


