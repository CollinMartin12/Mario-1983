import pyxel
import random
import Constants


class Coins:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.speed = 4
        self.direction = random.choice([-1, 1])
        self.dy = 0
        self.gravity = 0.5
        self.actionable = True

    @property
    def width(self):
        return 4

    @property
    def height(self):
        return 4

    def update(self):
        if self.actionable:
            self.dy += self.gravity
            self.y += self.dy
            if self.x - self.width < -30 or self.x > pyxel.width + 30 or self.y - self.height < -30 or self.y > pyxel.height + 30:
                self.actionable = False
            elif self.direction == -1:
                self.x -= self.speed
            elif self.direction == 1:
                self.x += self.speed

            if self.y > Constants.FLOOR:
                self.y = Constants.FLOOR
                self.dy = 0

    def draw(self):
        """Draws the shot"""
        pyxel.blt(self.x, self.y, 0, 96, 154, self.width, self.height, 0)
