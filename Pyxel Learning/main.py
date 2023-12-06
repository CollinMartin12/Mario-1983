import pyxel
import Constants
from Board import Board

WIDTH = 256
HEIGHT = 224
FLOOR = 100

# Mario
MARIO_INITIAL = (WIDTH / 2, 200)
MARIO_SPRITE = (1, 0, 0, 16, 16)


# Enemies
SPRITE_BLOCK_1 = (0, 0, 0, 16, 16)
SPRITE_BLOCK_2 = (0, 32, 0, 16, 16)
SPRITE_POW = (0, 16, 0, 16, 16)
BLOCK_INITIAL = ((0, 40, "BLOCK1"), (16, 40, "BLOCK1"),
                 (32, 40, "BLOCK1"), (48, 40, "BLOCK1"),
                 (124, 150, "POW"), (240, 40, "BLOCK2"),
                 (224, 40, "BLOCK2"), (208, 40, "BLOCK2"),
                 (192, 40, "BLOCK2"))


def run_game():
    # pyxel.init(160, 120, title="Mario Game")

    # game = Mario()
    board = Board(300, 300)
    pyxel.load("my_resource.pyxres")  # Load your .pyxel image file
    pyxel.run(board.update, board.draw)

if __name__ == "__main__":
    run_game()


