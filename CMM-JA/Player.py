import pyxel
import Constants
import Block


class Player:
    """ This is the player Class for Mario. It controls movement
    and other game implementations such as gravity sprites and attributes"""


    def __init__(self, x, y):

        self.hit_indicator_timer = 0
        self.x = x # X coordinate for Mario
        self.y = y
        self.dx = 0
        self.max_dx = 2  # Max speed for mario to achieve
        self.dy = 0  # How fast moving up or down(goes with gravity)
        self.direction = 1
        self.running = False
        self.jumping = False
        self.gravity = 0.5
        self.jump_strength = -8
        self.lives = 3
        self.alive = True
        self.invincible = False
        self.invincible_timer = 0
        self.score = 0

    @property
    def width(self):
        return 16

    @property
    def height(self):
        return 24

    @property
    def speed(self):
        return 2

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("The value must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("The value must be an integer")
        else:
            self.__y = value

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, value):
        if type(value) != int:
            raise TypeError("The number of lives must me an integer")
        else:
            self.__lives = value

    def update(self):
        if self.alive:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.running = True
                self.move("right")
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.running = True
                self.move("left")
            else:
                self.running = False

            if pyxel.btnp(pyxel.KEY_SPACE) and not self.jumping or pyxel.btnp(pyxel.KEY_UP) and not self.jumping:
                self.jumping = True
                self.dy = self.jump_strength
                self.max_dx = 1.5

            self.dy += self.gravity
            self.y += self.dy


            if self.y >= Constants.FLOOR:
                self.jumping = False
                self.y = Constants.FLOOR
                self.dy = 0

            if self.lives == 0:
                self.alive = False

    def register_hit(self):
        """Does the necessary actions when the player is hit."""

        self.invincible = True
        self.invincible_timer = 120

        self.lives -= 1
        if self.lives <= 0:
            self.alive = False

    def move(self, direction):
        if direction == "right":
            self.direction = 1
            self.x = (self.x + self.direction * self.max_dx) % pyxel.width
        elif direction == "left":
            self.direction = -1
            self.x = (self.x + self.direction * self.max_dx) % pyxel.width
        else:
            self.direction = 0

    def sprite(self):
        if self.running:
            return (0, 16, 8, 16 * self.direction, 24, 0)  # Change these coordinates to match your left running sprite
        elif self.jumping:
            return (0, 64, 8, 16 * self.direction, 24, 0)  # Change these coordinates to match your left jumping sprite
        else:
            return (0, 0, 8, 16 * self.direction, 24, 0)  # Change these coordinates to match your left default sprite
