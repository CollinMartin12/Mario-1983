import Constants
import pyxel
from Block import Block
from Flies import Flies
from Player import Player
import random
from Crab import Crab
from Turtle import Turtle
from Coins import Coins


class Board:
    """Board Class holds all the necessary elements to run the game.
    Board is then updated and drawn in main constantly to showcase the game we created.
    We hope you like it"""

    def __init__(self):

        self.Player = Player(self.width, self.height)
        self.enemies = []  # List of enemies in game
        self.game_state = "start"
        self.level_1_blocks = []  # Level# blocks to draw depending on game_state
        self.level_2_blocks = []
        self.level_3_blocks = []
        self.level_4_blocks = []
        self.callable_blocks = []  # blocks that an enemy can interact with
        self.non_collision_sprites = []
        self.coins = []  # list of coins in game
        self.enemy_counter = 0  # enemy counter on screen to determine game_state
        self.timer = 0  # Timer for when a certain amount of time is needed in between actions
        self.pow_block = (124, 150, 8, 16)  # POW block coordinates

        self.__mario = Player(*Constants.MARIO_INITIAL)

        for element in Constants.LEVEL1:
            self.callable_blocks.append(Block(*element))

        for pipe in Constants.PIPES_INITIAL:
            self.non_collision_sprites.append(Block(*pipe))

    @property
    def width(self):
        return 256

    @property
    def height(self):
        return 200

    def create_blocks(self):
        if self.game_state == 'level1':
            for element in Constants.LEVEL1:
                self.level_1_blocks.append(Block(*element))
        elif self.game_state == 'level2':
            for element in Constants.LEVEL2:
                self.level_2_blocks.append(Block(*element))
        elif self.game_state == 'level3':
            for element in Constants.LEVEL3:
                self.level_3_blocks.append(Block(*element))
        elif self.game_state == 'level4':
            for element in Constants.LEVEL4:
                self.level_4_blocks.append(Block(*element))

    def __drawBlocks(self):
        self.create_blocks()
        if self.game_state == 'level1':
            for element in self.level_1_blocks:
                pyxel.blt(element.x, element.y, *element.sprite, colkey=0)
        elif self.game_state == 'level2':
            for element in self.level_2_blocks:
                pyxel.blt(element.x, element.y, *element.sprite, colkey=0)
        elif self.game_state == 'level3':
            for element in self.level_3_blocks:
                pyxel.blt(element.x, element.y, *element.sprite, colkey=0)
        elif self.game_state == 'level4':
            for element in self.level_4_blocks:
                pyxel.blt(element.x, element.y, *element.sprite, colkey=0)

        for element2 in self.non_collision_sprites:
            pyxel.blt(element2.x, element2.y, *element2.sprite, colkey=0)

    def __drawMario(self):
        pyxel.blt(self.__mario.x, self.__mario.y, *self.__mario.sprite())

    def draw(self):
        """Draws the board and draws the necessary game_state and elements. Constantly updates from Main"""

        pyxel.cls(0)
        if self.game_state == 'start':
            self.__start_screen()
        elif self.game_state == 'game over':
            self.__draw_game_over()

        else:
            if self.game_state == 'level2':
                self.__level_2()
            elif self.game_state == 'level3':
                self.__level_3()
            elif self.game_state == 'level4':
                self.__level_4()
            elif self.game_state == 'winner':
                self.__winner()
                pyxel.cls(0)

            self.__drawBlocks()

            self.__drawMario()

            for enemy in self.enemies:
                enemy.draw()

            self.__draw_stats()

            for coin in self.coins:
                coin.draw()

    def __check_collisions(self, block1, block2):
        """Checks all collisions between two elements and returns True or False"""

        return (
                block1.x < block2.x + block2.width
                and block1.x + block1.width > block2.x
                and block1.y < block2.y + block2.height
                and block1.y + block1.height > block2.y
        )

    def __check_all_collisions(self, block):
        """Uses the check_collisions to check if collision is True, then runs the
        necessary operations for each collision type"""
        # Collisions between Mario and Block
        if self.__check_collisions(self.__mario, block):
            overlap_left = (block.x + block.width) - self.__mario.x
            overlap_right = (self.__mario.x + self.__mario.width) - block.x
            overlap_top = (block.y + block.height) - self.__mario.y
            overlap_bottom = (self.__mario.y + self.__mario.height) - block.y

            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_left:
                self.__mario.x = block.x + self.__mario.width

            if min_overlap == overlap_right:
                self.__mario.x = block.x - self.__mario.width

            if min_overlap == overlap_bottom:
                self.__mario.y = block.y - self.__mario.height
                self.__mario.dy = 0
                self.__mario.jumping = False

                if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                    self.__mario.dy = self.__mario.jump_strength
                    self.__mario.jumping = True
                    print(self.__mario.dy)

            if min_overlap == overlap_top:
                self.__mario.y = block.y + 8
                pass

            #

            if self.__check_collisions(self.__mario, Block(*Constants.POW)):

                for enemy in self.enemies:
                    enemy.paused = True

            # Checks if enemy is on top of a block mario top collides with
            for enemy in self.enemies:
                if not self.Player.invincible:
                    # +8 to extend collision range
                    if enemy.y + enemy.height == block.y and block.x - 8 < enemy.x < block.x + block.width + 8:
                        enemy.paused = True
                        self.Player.score += 100
                        enemy.speed = 2

        # Collision for Mario and Enemies
        if self.__mario.alive:
            for enemy in self.enemies:
                if not self.Player.invincible:
                    if self.__check_collisions(self.__mario, enemy):
                        if enemy.paused:
                            self.enemies.remove(enemy)
                            self.Player.score += 500
                        else:
                            if self.__mario.alive:
                                self.Player.register_hit()

        # Block Collision With Enemies
        for block in self.callable_blocks:
            for enemy in self.enemies:
                if self.__check_collisions(enemy, block):
                    overlap_left = (block.x + block.width) - enemy.x
                    overlap_right = (enemy.x + enemy.width) - block.x
                    overlap_top = (block.y + block.height) - enemy.y
                    overlap_bottom = (enemy.y + enemy.height) - block.y

                    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                    if min_overlap == overlap_left:
                        enemy.x = block.x + enemy.width

                    if min_overlap == overlap_right:
                        enemy.x = block.x - enemy.width

                    if min_overlap == overlap_bottom:
                        enemy.y = block.y - enemy.height
                        enemy.dy = 0
                        enemy.jumping = False

                    if min_overlap == overlap_top:
                        enemy.y = block.y + enemy.height

        # Block collision for coins
        for block in self.callable_blocks:
            for coin in self.coins:
                if self.__check_collisions(self.__mario, coin):
                    self.coins.remove(coin)
                    self.Player.score += 800

                if self.__check_collisions(coin, block):
                    overlap_left = (block.x + block.width) - coin.x
                    overlap_right = (coin.x + coin.width) - block.x
                    overlap_top = (block.y + block.height) - coin.y
                    overlap_bottom = (coin.y + coin.height) - block.y

                    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                    if min_overlap == overlap_left:
                        coin.x = block.x + coin.width

                    if min_overlap == overlap_right:
                        coin.x = block.x - coin.width

                    if min_overlap == overlap_bottom:
                        coin.y = block.y - coin.height
                        coin.dy = 0

                    if min_overlap == overlap_top:
                        coin.y = block.y + coin.height

    def update(self):
        """Update method for the game board. Everything in this method is looped through when called in Main"""

        if self.game_state == "start" and pyxel.btnp(pyxel.KEY_SPACE):
            self.game_state = "level1"
        if not self.Player.alive:
            self.game_state = 'game over'
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.game_state = 'start'
                return

        else:
            self.__mario.update()
            self.__check_all_collisions(self.__mario)

            for block_info in Constants.LEVEL1:
                block_x, block_y, block_type = block_info
                block = Block(block_x, block_y, block_type)
                self.__check_all_collisions(block)

            for enemy in self.enemies:
                if not enemy.alive:
                    self.enemies.remove(enemy)
                else:
                    enemy.update()

            for coin in self.coins:
                if coin.collected:
                    self.coins.remove(coin)
                else:
                    coin.update()

            if self.Player.invincible:
                if self.Player.invincible_timer > 0:
                    self.Player.invincible_timer -= 1
                else:
                    self.Player.invincible = False

            self.__spawn_enemies_and_coins()

    def __draw_stats(self):
        """Draws Text for lives Score and game_state while the game is running"""
        pyxel.text(2, 2, "SCORE", 7)
        pyxel.text(2, 10, str(self.Player.score), 7)
        pyxel.text((self.width // 2) - 10, 10, self.game_state, 7)

        pyxel.text(self.width - 20, 5, str(self.Player.lives) + "x", 7)
        pyxel.blt(self.width - 10, 3, 0, 168, 16, 8, 8, 0)

    def __draw_game_over(self):
        """Draws game_over"""
        self.game_state = "game over"
        pyxel.cls(0)

        pyxel.blt(80, 100, 1, 0, 48, 140, 16)

    def __start_screen(self):
        """Draws Start Screen"""
        pyxel.text(70,100, "START: PRESS SPACE TO BEGIN", 7)

    def __level_2(self):
        """ Draws Level2 text in middle of the screen"""
        if self.timer == 0:
            self.timer = pyxel.frame_count + 60

        if not pyxel.frame_count >= self.timer:
            pyxel.text(100, 30, "Level 2: Crabs", 7)
            self.timer = 0

    def __level_3(self):
        """ Draws Level3 text in middle of the screen"""
        if self.timer == 0:
            self.timer = pyxel.frame_count + 60

        if not pyxel.frame_count >= self.timer:
            pyxel.text(100, 50, "Level 3: FLIES", 7)
            self.timer = 0

    def __level_4(self):
        """ Draws Level4 text in middle of the screen"""
        if self.timer == 0:
            self.timer = pyxel.frame_count + 60

        if not pyxel.frame_count >= self.timer:
            pyxel.text(100, 30, "Level 4: EVERYTHING", 7)
            self.timer = 0

    def __winner(self):
        pyxel.text(100, 50, "YOU WON", 7)



    def __spawn_enemies_and_coins(self):
        """Spawns the necessary enemies per level depending on game_state"""
        if self.game_state == 'level1':
            if self.enemy_counter < 5:
                if random.randint(0, 200) == 1:
                    self.enemies.append(Turtle(random.choice([0, 256]), random.choice([42, 96])))
                    self.enemy_counter += 1
                    print(self.enemy_counter)
                if random.randint(1, 350) == 1:
                    self.coins.append(Coins(random.choice([0, 256]), 34))

            elif self.enemy_counter >= 5 and len(self.enemies) == 0:
                self.game_state = 'level2'
                self.enemy_counter = 0
                self.level_1_blocks.clear()

        elif self.game_state == 'level2':

            if self.enemy_counter < 7:
                if random.randint(0, 200) == 1:
                    self.enemies.append(Crab(random.choice([0, 256]), random.choice([134, 34])))
                if random.randint(1, 350) == 1:
                    self.coins.append(Coins(random.choice([0, 256]), 34))
                    self.enemy_counter += 1
            elif len(self.enemies) == 0 and self.enemy_counter >= 7:
                self.game_state = 'level3'
                self.enemy_counter = 0
                self.level_2_blocks.clear()

        elif self.game_state == 'level3':
            if self.enemy_counter < 7:
                if random.randint(0, 200) == 1:
                    self.enemies.append(Flies(random.choice([0, 256]), random.choice([134, 34])))
                    self.enemy_counter += 1
                if random.randint(1, 350) == 1:
                    self.coins.append(Coins(random.choice([0, 256]), 34))
            elif len(self.enemies) == 0 and self.enemy_counter >= 5:
                self.game_state = 'level4'
                self.enemy_counter = 0
                self.level_3_blocks.clear()

        elif self.game_state == 'level4':
            if self.enemy_counter < 11:
                if random.randint(0, 200) == 1:
                    self.enemies.append(Turtle(random.choice([0, 256]), random.choice([134, 34])))
                    self.enemy_counter += 1
                if random.randint(0, 250) == 1:
                    self.enemies.append(Crab(random.choice([0, 256]), random.choice([134, 34])))
                    self.enemy_counter += 1
                if random.randint(0, 350) == 1:
                    self.enemies.append(Flies(random.choice([0, 256]), random.choice([134, 34])))
                    self.enemy_counter +=1
            elif len(self.enemies) == 0 and self.enemy_counter >= 11:
                pyxel.cls(0)
                self.game_state = 'WINNER'
                self.enemy_counter = 0

