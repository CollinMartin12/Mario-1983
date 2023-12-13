from Enemy import Enemy
import random
import pyxel


class Turtle(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.shell_color = (0, 255, 0)
        self.direction_speed = random.choice([-1, 1])
        self.lives = 1
        self.paused = False
        self.jumper = False
        self.color = 'NORMAL'

    def move(self):
        if not self.paused:
            if self.x == 0:
                self.direction_speed = 1  # Move right if spawned at x = 0
            elif self.x == pyxel.width:
                self.direction_speed = -1

    def draw(self):
        if self.color == 'NORMAL':
            if self.paused and (self.direction_speed == 1 or self.direction_speed == -1):
                pyxel.blt(self.x, self.y, 0, 112, 184, 16, 16, 0)
            elif not self.paused:
                pyxel.blt(self.x, self.y, 0, 0, 184, 16 * self.direction, 16, 0)
        elif self.color == "CHANGED":
            if self.paused and (self.direction_speed == 1 or self.direction_speed == -1):
                pyxel.blt(self.x, self.y, 0, 200, 184, 16 * self.direction_speed, 16, 0)
            elif not self.paused:
                pyxel.blt(self.x, self.y, 0, 184, 184, 16 * self.direction, 16, 0)
        else:
            raise Exception("The direction of the enemy is not supported")
