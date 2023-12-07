import Constants
from Mario import Mario
import pyxel
from Block import Block
from Player import Player


class Board:
    """This class contains the necessary information to
    represent the board"""

    def __init__(self):


        self.Player = Player(self.width, self.height)
        self.enemies = []
        self.highscore = 0
        self.screen = "Start Screen"

        # Create the blocks
        self.blocks = []

        self.__mario = Player(* Constants.MARIO_INITIAL)

        for element in Constants.BLOCK_INITIAL:
            self.blocks.append(Block(*element))





    @property
    def width(self) -> int:
        return 256
    @property
    def height(self) -> int:
        return 200


    def __drawBlocks(self):
        for element in self.blocks:
            pyxel.blt(element.x, element.y, *element.sprite, colkey=0)

    def __drawMario(self):
        pyxel.blt(self.__mario.x, self.__mario.y, * self.__mario.sprite())


    def draw(self):
        pyxel.cls(0)
        self.__drawMario()
        self.__drawBlocks()
    def update(self):
        self.__mario.update()
