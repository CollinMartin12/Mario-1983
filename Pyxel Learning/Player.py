class Player:
    """
    x (float): x - coordinate of Mario
    y (float): y - coordinate of Mario
    """

    def __init__(self, x, y):
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
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.running = True
            self.move("right")
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.running = True
            self.move("left")
        else:
            self.running = False

        if pyxel.btnp(pyxel.KEY_SPACE) and not self.jumping:
            self.jumping = True
            self.dy = self.jump_strength

        if self.jumping:
            self.dy += self.gravity
            self.y += self.dy

            if self.y >= FLOOR:
                self.jumping = False
                self.y = FLOOR
                self.dy = 0
    def move(self, direction):
        if direction == "right":
            self.x += self.dx
            self.direction = 1  # Set direction to right
        elif direction == "left":
            self.x -= self.dx
            self.direction = -1  # Set direction to left


    def draw(self):

        pyxel.blt(self.x, self.y, 0, 0, 0, 16 * self.direction, 16, colkey=0)

