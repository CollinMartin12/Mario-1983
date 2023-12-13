import pyxel
import random
from Enemy import Enemy


class Coins(Enemy):


    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.collected = False
        self.direction_speed = random.choice([-2, 2])
        self.jumper = False



    def move(self):
        if not self.collected:
            if self.x == 0:
                self.direction_speed = 1  # Move right if spawned at x = 0
            elif self.x == pyxel.width:
                self.direction_speed = -1

    def draw(self):
        '''draws the coin'''
        pyxel.blt(self.x, self.y, 0, 96, 154, self.width, self.height, 0)
