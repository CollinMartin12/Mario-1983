from Enemy import Enemy
import random
import pyxel


class Crab(Enemy):
    """This is the Crab class inhertied from enemy that controls
    the movement and the sprites of the crab"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.direction_speed = random.choice([-1, 1])
        self.paused = False
        self.jumper = False
        self.lives = 2
        self.speed = 2

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
            pyxel.blt(self.x, self.y, 0, 208, 200, 16 * -self.direction, 16, 0)
        elif not self.paused:
            pyxel.blt(self.x, self.y, 0, 0, 200, 16 * -self.direction, 16, 0)
        else:
            raise Exception("The direction of the enemy is not supported")
