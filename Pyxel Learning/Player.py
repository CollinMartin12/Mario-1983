import pyxel
import Constants
import Block


class Player:
    """
    x (float): x - coordinate of Mario
    y (float): y - coordinate of Mario
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.max_dx = 2
        self.acceleration = .25
        self.dy = 0
        self.direction = 1
        self.running = False
        self.jumping = False
        self.gravity = 0.5  # Adjust gravity for jumping/falling
        self.jump_strength = -8  # Adjust jump strength
        self.lives = 3
        self.collision = False

    @property
    def width(self):
        return 16

    @property
    def height(self):
        return 16

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
            self.max_dx = 1.5

            if self.y >= Constants.FLOOR:
                self.jumping = False
                self.y = Constants.FLOOR
                self.dy = 0

        for block_info in Constants.BLOCK_INITIAL:
            block_x, block_y, block_type = block_info
            block = Block.Block(block_x, block_y, block_type)
            self.check_all_collisions(block)

    def move(self, direction):
        if direction == "right":
            self.direction = 1
        elif direction == "left":
            self.direction = -1
        else:
            self.direction = 0

        # Update velocity based on direction and acceleration
        self.dx += self.direction * self.acceleration

        # Limit velocity to max velocity
        self.dx = max(-self.max_dx, min(self.max_dx, self.dx))

        # Update position based on velocity
        self.x += self.dx

    def check_collisions(self, block):
        if (
                self.x < block.x + block.width
                and self.x + self.width > block.x
                and self.y < block.y + block.height
                and self.y + self.height > block.y
        ):
            return True
        return False

    def check_all_collisions(self, block):
        if self.check_collisions(block):
            overlap_left = (block.x + block.width) - self.x
            overlap_right = (self.x + self.width) - block.x
            overlap_top = (block.y + block.height) - self.y
            overlap_bottom = (self.y + self.height) - block.y
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_left and self.dx > 0:
                self.x = block.x + self.width

            if min_overlap == overlap_right and self.dx > 0:
                self.x = block.x - self.width

            if min_overlap == overlap_bottom:  # Ensure the player is landing (not floating in the air)
                self.y = block.y - self.height
                self.dy = 0
                self.jumping = False
                self.max_dx = 2

                if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                    self.dy += self.jump_strength
                    self.jumping = True

            if min_overlap == overlap_top:
                self.y = block.y + self.height

    def sprite(self):
        return Constants.MARIO_SPRITE
