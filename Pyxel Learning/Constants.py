import pyxel

WIDTH = 256
HEIGHT = 224
FLOOR = 100

# Mario
MARIO_INITIAL = (WIDTH / 2, 200)
MARIO_SPRITE = (1, 0, 0, 16, 16)


# Enemies
SPRITE_BLOCK_1 = (0, 0, 0, 16, 16)
SPRITE_BLOCK_2 = (0, 32, 0, 16, 16)
SPRITE_POW = (0, 16, 0, 16, 16)
BLOCK_INITIAL = ((0, 40, "BLOCK1"), (16, 40, "BLOCK1"),
                 (32, 40, "BLOCK1"), (48, 40, "BLOCK1"),
                 (124, 150, "POW"), (240, 40, "BLOCK2"),
                 (224, 40, "BLOCK2"), (208, 40, "BLOCK2"),
                 (192, 40, "BLOCK2"))



class Mario:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 1.0
        self.dy = 0
        self.direction = 1
        self.running = False
        self.jumping = False
        self.gravity = 0.5  # Adjust gravity for jumping/falling
        self.jump_strength = -6  # Adjust jump strength
        self.lives = 3

    def update(self):
        self.handle_movement()
        self.handle_jumping()

    def handle_movement(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.move_right()
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.move_left()
        else:
            self.running = False

    def move_right(self):
        self.running = True
        self.move("right")

    def move_left(self):
        self.running = True
        self.move("left")

    def move(self, direction):
        if direction == "right":
            self.x += self.dx
            self.direction = 1  # Set direction to right
        elif direction == "left":
            self.x -= self.dx
            self.direction = -1  # Set direction to left

    def handle_jumping(self):
        if pyxel.btnp(pyxel.KEY_SPACE) and not self.jumping:
            self.jump()

        if self.jumping:
            self.perform_jump()

    def jump(self):
        self.jumping = True
        self.dy = self.jump_strength

    def perform_jump(self):
        self.dy += self.gravity
        self.y += self.dy

        if self.y >= FLOOR:
            self.finish_jump()

    def finish_jump(self):
        self.jumping = False
        self.y = FLOOR
        self.dy = 0

    def draw(self):
        pyxel.cls(0)  # Clear the screen
        pyxel.blt(self.x, self.y, 0, 0, 0, 16 * self.direction, 16, colkey=0)
