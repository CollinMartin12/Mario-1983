import random
import pyxel
from Constants import *

class Enemy:
    """Class that represents an enemy and is being inherited as the base class for all the enemies subclasses.

    Attributes:
        x (float): X coordinate of the enemy
        y (float): Y coordinate of the enemy
        alive (bool): Is the enemy alive or not
        width (int)(readonly): Width of the enemy
        height (int)(readonly): Height of the enemy
        speed (int)(readonly): Speed of the enemy

    Methods:
        update(): Updates the enemy position and removes the shots that go off the screen
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.speed = 1
        self.alive = True

    def update(self):
        if self.alive:
            self.x += self.speed


        # If the enemy goes off of the screen by more the 30 pixels (dead)
        if self.x - self.width < -30 or self.x > pyxel.width + 30 or self.y - self.height < -30 or self.y > pyxel.height + 30:
            self.health = 0



    def draw(self):
        if self.alive:
            pyxel.rect(self.x, self.y, self.x + self.width, self.y + self.height, pyxel.COLOR_RED)



# Example usage:
if __name__ == "__main__":
    pyxel.init(160, 120, title="Mario Enemy Example")
    enemy = Enemy(20, 20)  # Create an enemy instance
    pyxel.run(enemy.update, enemy.draw)