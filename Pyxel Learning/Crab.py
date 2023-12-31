from Enemy import Enemy
import random
import pyxel


class Crab(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.shell_color = (0, 255, 0)
        self.direction_speed = random.choice([-1, 1])

        self.paused = False
        self.jumper = False
        self.lives = 2

    def move(self):
        if not self.paused:
            if self.x == 0:
                self.direction_speed = 1  # Move right if spawned at x = 0
            elif self.x == pyxel.width:
                self.direction_speed = -1

    def draw(self):
        if self.direction_speed == -1:
            pyxel.blt(self.x, self.y, 0, 0, 200, 16, 16, 0)
        elif self.direction_speed == 1:  # Change to 1 for the other direction
            pyxel.blt(self.x, self.y, 0, 0, 200, 16, 16, 0)
        else:
            raise Exception("The direction of the enemy is not supported")
