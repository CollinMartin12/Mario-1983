import random
import pyxel
import Constants


class Enemy:
    def __init__(self, x: int, y: int):
        self.lives = 2
        self.paused = False
        self.x = x
        self.y = y
        self.speed = 1
        self.alive = True
        self.direction = random.choice([-1, 1])
        self.max_dx = 2
        self.dy = 0
        self.gravity = 0.5
        self.pause_duration = 100
        self.pause_end_frame = 0
        self.color = 'NORMAL'
        self.jumping = False
        self.jump_strength = -5
        self.jumper = True
        self.jump_delay = 30
        self.timer = 0
        self.collision = 0


    @property
    def width(self):
        return 16

    @property
    def height(self):
        return 14


    def update(self):
        if not self.paused:
            self.dy += self.gravity
            self.y += self.dy
            if self.x - self.width < -30 or self.x > pyxel.width + 30 or self.y - self.height < -30 or self.y > pyxel.height + 30:
                self.alive = False
            elif self.direction == -1:
                self.x -= self.speed
            elif self.direction == 1:
                self.x += self.speed

            if self.y > Constants.FLOOR:
                self.y = Constants.FLOOR
                self.dy = 0

            if self.x < Constants.PIPE_X_POSITION_LEFT and self.x < 0 and self.y > 150:
                self.x = 2
                self.y = 34
                self.direction = 1

            if self.x < Constants.PIPE_X_POSITION_LEFT and self.x < 0 and self.y <= 150:
                self.x = 254  # Reappear on the right side of the screen
                # Optionally, you can change other properties here, such as direction

            # Check if the enemy went through the right pipe and crossed the screen
            if self.x > Constants.PIPE_X_POSITION_RIGHT and self.x > 256 and self.y >= 150:
                self.x = 254
                self.y = 34
                self.direction = -1

            if self.x > Constants.PIPE_X_POSITION_RIGHT and self.x > 256 and self.y <= 150:
                self.x = 2

            if self.jumper and not self.jumping:
                if self.timer == 0:
                    self.timer = pyxel.frame_count + self.jump_delay

                if pyxel.frame_count >= self.timer:
                    self.jumping = True
                    self.jump()
                    self.y += self.dy


        else:

            if self.pause_end_frame == 0:
                self.pause_end_frame = pyxel.frame_count + self.pause_duration
                self.lives -= 1

            if pyxel.frame_count >= self.pause_end_frame:
                self.paused = False
                self.enemy_change_color()
                self.pause_end_frame = 0

    def jump(self):
        if self.jumping:
            self.dy = self.jump_strength


        if self.y >= Constants.FLOOR:
            self.jumping = False
            self.y = Constants.FLOOR
            self.dy = 0

    def enemy_change_color(self):
        self.color = 'CHANGED'
