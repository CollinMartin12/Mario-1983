import random
import pyxel
import Constants
from Enemy import Enemy


class Flies(Enemy):
    """This is the Flies class inherited from enemy that controls the movement of the flies.
    It also controls jump strength and has its own gravity to show that it is flying."""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.direction_speed = random.choice([-1, 1])
        self.lives = 1
        self.paused = False
        self.jump_strength = -2
        self.jumping = False
        self.jumper = True # so the enemy attribute from enemy can activate
        self.gravity = 0.1


    @property
    def width(self):
        return 16

    @property
    def height(self):
        return 12


    def move(self):
        if not self.paused:
            if self.x == 0:
                self.direction_speed = 1  # Move right if spawned at x = 0
            elif self.x == pyxel.width:
                self.direction_speed = -1


    def draw(self):
        if self.paused and (self.direction_speed == 1 or self.direction_speed == -1):
            pyxel.blt(self.x, self.y, 1, 29, 178, 15 * self.direction_speed, 16, 0)
        elif not self.paused:
            pyxel.blt(self.x, self.y, 1, 29, 154, 15 * self.direction_speed, 16, 0)
        else:
            raise Exception("The direction of the enemy is not supported")

