import Constants
from Mario import Mario
import pyxel
from Block import Block
from Player import Player
from Enemy import Enemy
import random
from Mushroom import Mushroom
from Crab import Crab
from Turtle import Turtle


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

        self.__mario = Player(*Constants.MARIO_INITIAL)

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
        pyxel.blt(self.__mario.x, self.__mario.y, *self.__mario.sprite())

    def draw(self):
        pyxel.cls(0)
        self.__drawMario()
        self.__drawBlocks()

        for enemy in self.enemies:
            enemy.draw()

    def update(self):
        self.__mario.update()
        # self.check_all_collisions()


        for enemy in self.enemies:
            # Removes the enemy if it has 0 lives
            if enemy.lives <= 0:
                self.enemies.remove(enemy)
            else:
                enemy.update()

            # Randomly spawns enemies
        if random.randint(0, 100) == 1:
            self.enemies.append(Turtle(random.choice([0, 256]), random.choice([134, 184, 34])))
        if random.randint(0, 100) == 1:
            self.enemies.append(Mushroom(random.choice([0, 256]), random.choice([134, 34])))
        if random.randint(0, 200) == 1:
            self.enemies.append(Crab(random.choice([0, 256]), random.choice([134, 34])))
        if random.randint(0, 1200) == 1:
            pass
    #
    # def check_all_collisions(self):
    #     for block in self.blocks:
    #         # self.blocks.x, self.blocks.y, self.blocks.block_type = block_info
    #         # block = Block(self.blocks.x, self.blocks.y, self.blocks.block_type)
    #         self.check_collision(block)
    #
    # def check_collision(self, block):
    #     if self.Player.x < block.x + block.width and self.Player.x + self.Player.width > block.x and self.Player.y < block.y + block.height and self.Player.y + self.Player.height > block.y:
    #         overlap_left = (block.x + block.width) - self.Player.x
    #         overlap_right = (self.Player.x + self.Player.width) - block.x
    #         overlap_top = (block.y + block.height) - self.Player.y
    #         overlap_bottom = (self.Player.y + self.Player.height) - block.y
    #         min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
    #
    #         if min_overlap == overlap_left and self.Player.dx > 0:
    #             self.Player.x = block.x + self.Player.width
    #         if min_overlap == overlap_right and self.dx > 0:
    #             self.Player.x = block.x - self.Player.width
    #
    #         if min_overlap == overlap_bottom:  # Ensure the player is landing (not floating in the air)
    #             print("\n\n\n bottom hit \n\n\n")
    #             self.y = block.y - self.height
    #             self.dy = 0
    #             self.jumping = False
    #             self.max_dx = 2
    #             if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
    #                 self.dy += self.jump_strength
    #                 self.jumping = True
    #             else:
    #                 self.y += self.dy
    #                 self.dy += self.gravity
    #
    #         if min_overlap == overlap_top:
    #             self.y = block.y + self.height
