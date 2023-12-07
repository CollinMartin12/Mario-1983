import pyxel
import Constants


class Player:
    """
    x (float): x - coordinate of Mario
    y (float): y - coordinate of Mario
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 2.0
        self.dy = 0
        self.direction = 1
        self.running = False
        self.jumping = False
        self.gravity = 0.5  # Adjust gravity for jumping/falling
        self.jump_strength = -8  # Adjust jump strength
        self.lives = 3

    @property
    def width(self):
        return 16

    @property
    def height(self):
        return 14

    def update(self):
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

        if self.jumping:
            self.dy += self.gravity
            self.y += self.dy

            if self.y >= Constants.FLOOR:
                self.jumping = False
                self.y = Constants.FLOOR
                self.dy = 0

    def move(self, direction):
        if direction == "right":
            self.x += self.dx
            self.direction = 1  # Set direction to right
        elif direction == "left":
            self.x -= self.dx
            self.direction = -1  # Set direction to left

    def sprite(self):
        return Constants.MARIO_SPRITE
