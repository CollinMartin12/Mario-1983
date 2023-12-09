import Constants
import pyxel
from Block import Block
from Player import Player
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

    def check_collisions(self, block1, block2):
        return (
                block1.x < block2.x + block2.width
                and block1.x + block1.width > block2.x
                and block1.y < block2.y + block2.height
                and block1.y + block1.height > block2.y
        )

    def check_all_collisions(self, block):
        if self.check_collisions(self.__mario, block):
            overlap_left = (block.x + block.width) - self.__mario.x
            overlap_right = (self.__mario.x + self.__mario.width) - block.x
            overlap_top = (block.y + block.height) - self.__mario.y
            overlap_bottom = (self.__mario.y + self.__mario.height) - block.y

            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_left:
                self.__mario.x = block.x + self.__mario.width

            if min_overlap == overlap_right:
                self.__mario.x = block.x - self.__mario.width

            if min_overlap == overlap_bottom:
                self.__mario.y = block.y - self.__mario.height
                self.__mario.dy = 0
                print("bottom")
                # Only handle jumping if there's no bottom collision
                if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                    self.__mario.dy = self.__mario.jump_strength  # Adjust this value for jump strength
                    self.__mario.jumping = True
                    print(self.__mario.dy)

            if min_overlap == overlap_top:
                self.__mario.y = block.y + self.__mario.height

        for enemy in self.enemies:
            if self.check_collisions(self.__mario, enemy):
                overlap_left = (block.x + block.width) - self.__mario.x
                overlap_right = (self.__mario.x + self.__mario.width) - block.x
                overlap_top = (block.y + block.height) - self.__mario.y
                overlap_bottom = (self.__mario.y + self.__mario.height) - block.y

                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                if min_overlap == overlap_left:
                    self.__mario.x = block.x + self.__mario.width

                if min_overlap == overlap_right:
                    self.__mario.x = block.x - self.__mario.width

                if min_overlap == overlap_bottom:
                    self.__mario.y = block.y - self.__mario.height
                    self.__mario.dy = 0
                    print("bottom")
                    # Only handle jumping if there's no bottom collision
                    if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                        self.__mario.dy = self.__mario.jump_strength  # Adjust this value for jump strength
                        self.__mario.jumping = True
                        print(self.__mario.dy)

                if min_overlap == overlap_top:
                    self.__mario.y = block.y + self.__mario.height

            for enemy in self.enemies:
                if self.check_collisions(self.__mario, enemy):
                    overlap_left = (enemy.x + enemy.width) - self.__mario.x
                    overlap_right = (self.__mario.x + self.__mario.width) - enemy.x
                    overlap_top = (enemy.y + enemy.height) - self.__mario.y
                    overlap_bottom = (self.__mario.y + self.__mario.height) - enemy.y

                    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                    if min_overlap == overlap_left:
                        self.__mario.x = enemy.x + self.__mario.width
                        print("HIT")
                    if min_overlap == overlap_right:
                        self.__mario.x = enemy.x - self.__mario.width
                        print("HIT")
                    if min_overlap == overlap_bottom:
                        self.__mario.y = enemy.y - self.__mario.height
                        self.__mario.dy = 0
                        print("HIT")
                        # Only handle jumping if there's no bottom collision
                        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                            self.__mario.dy = self.__mario.jump_strength  # Adjust this value for jump strength
                            self.__mario.jumping = True
                            print("HIT")

                    if min_overlap == overlap_top:
                        self.__mario.y = enemy.y + self.__mario.height
                        print("HIT")

    def update(self):
        self.__mario.update()

        for block_info in Constants.BLOCK_INITIAL:
            block_x, block_y, block_type = block_info
            block = Block(block_x, block_y, block_type)
            self.check_all_collisions(block)

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
