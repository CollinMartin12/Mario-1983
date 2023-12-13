import random
import pyxel
import Constants
from Enemy import Enemy


class Flies(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.shell_color = (0, 255, 0)
        self.direction_speed = random.choice([-1, 1])
        self.lives = 1
        self.paused = False
        self.jump_strength = -2
        self.jumping = False
        self.jumper = True
        self.gravity = 0.1
        self.speed = 0.5

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

