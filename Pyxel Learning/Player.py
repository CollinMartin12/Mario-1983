import pyxel
import Constants
import Block


class Player:
    """
    x (float): x - coordinate of Mario
    y (float): y - coordinate of Mario
    """

    def __init__(self, x, y):
        self.hit_indicator_timer = 0
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
        self.alive = True
        self.invincible = False
        self.invincible_timer = 0
        self.score = 0
        self.invincible_timer = 120

    @property
    def width(self):
        return 16

    @property
    def height(self):
        return 24

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

            self.dy += self.gravity
            self.y += self.dy
            self.max_dx = 1.5

            if self.y >= Constants.FLOOR:
                self.jumping = False
                self.y = Constants.FLOOR
                self.dy = 0

            if self.lives == 0:
                self.alive = False
                print("DEAD")

            if self.invincible:
                if pyxel.frame_count % 20 == 0 and self.invincible_timer > 0:
                    self.invincible_timer -= 1
                    # Toggles the hit indicator to make it blink
                elif self.invincible_timer == 0:
                    self.invincible = False
                    print('not anymore')
        else:
            pass

    def register_hit(self):
        """Does the necessary actions when the player is hit."""
          # Set the player to not alive if lives reach zero
        self.invincible = True
        self.invincible_timer = 120
        print('invincible')

        self.lives -= 1
        if self.lives <= 0:
            self.alive = False
            print("SHOULD BE DEAD")

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
