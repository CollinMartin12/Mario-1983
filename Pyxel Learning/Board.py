import Constants
from Mario import Mario
import pyxel
from Block import Block
from Player import Player


class Board:
    """This class contains the necessary information to
    represent the board"""

    def __init__(self):
        """These parameters are the width and height of the board"""

        self.Player = Player(self.width, self.height)
        self.enemies = []
        self.highscore = 0
        self.screen = "Start Screen"

        # Create the blocks
        self.blocks = []

        for element in Constants.BLOCK_INITIAL:
            self.blocks.append(Block(*element))


    @property
    def width(self) -> int:
        return 254
    @property
    def height(self) -> int:
        return 254



    def update(self):
        self.Player.update()


    def __drawBlocks(self):
        for block in self.blocks:
            block.draw()

    def __drawMario(self):
        self.Player.draw()


    def draw(self):
        self.__drawMario()
        self.__drawBlocks()

