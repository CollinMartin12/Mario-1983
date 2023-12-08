import random
import pyxel
import Constants

class Enemy:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.speed = 1
        self.alive = True
        self.direction = random.choice([-1, 1])  # Corrected random.choice usage

    def update(self):

        # Kills the Enemy if it goes out of the screen by more than 30 pixels
        if self.x - self.width < -30 or self.x > pyxel.width + 30 or self.y - self.height < -30 or self.y > pyxel.height + 30:
            self.alive = False
        elif self.direction == -1:
            self.x -= self.speed
        elif self.direction == 1:
            self.x += self.speed
