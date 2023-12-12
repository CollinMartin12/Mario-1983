import Constants
import pyxel
from Block import Block
from Player import Player
import random
from Mushroom import Mushroom
from Crab import Crab
from Turtle import Turtle
from Coins import Coins


class Board:
    """This class contains the necessary information to
    represent the board"""

    def __init__(self):

        self.Player = Player(self.width, self.height)
        self.enemies = []
        self.highscore = 0
        self.game_state = "level1"
        # Create the blocks
        self.blocks = []
        self.non_collision_sprites = []
        self.coins = []
        self.enemy_counter = 0
        self.timer = 0

        self.__mario = Player(*Constants.MARIO_INITIAL)

        for element in Constants.LEVEL1:
            self.blocks.append(Block(*element))

        for pipe in Constants.PIPES_INITIAL:
            self.non_collision_sprites.append(Block(*pipe))

    @property
    def width(self) -> int:
        return 256

    @property
    def height(self) -> int:
        return 200

    def __drawBlocks_level1(self):
        for element in self.blocks:
            pyxel.blt(element.x, element.y, *element.sprite, colkey=0)
        for element2 in self.non_collision_sprites:
            pyxel.blt(element2.x, element2.y, *element2.sprite, colkey=0)

    def change_block_types(self, level):
        if level == "level2":
            for block in self.blocks:
                # Update block types for level 2
                block.block_type = Constants.LEVEL2[self.blocks.index(block)]
        # elif level == "level3":
        #     for block in self.blocks:
        #         # Update block types for level 3
        #         block.block_type = Constants.LEVEL3_BLOCK_TYPES[self.blocks.index(block)]
    #
    # def __drawBlockslevel2(self):
    #     for element in self.blocks:
    #         if element.block_type == "BLOCK2":
    #             pyxel.blt(element.x, element.y, *Constants.SPRITE_BLOCK_2, colkey=0)

        for element2 in self.non_collision_sprites:
            pyxel.blt(element2.x, element2.y, *element2.sprite, colkey=0)

    def __drawMario(self):
        pyxel.blt(self.__mario.x, self.__mario.y, *self.__mario.sprite())

    def draw(self):
        pyxel.cls(0)

        self.__drawMario()

        # if self.game_state == "game over":
        #     self.draw_game_over()
        #
        # if self.game_state == "level2":
        #     self.level_2()
        #     self.__drawBlockslevel2()
        # else:
        #     self.__drawBlocks_level1()
        if self.game_state == 'level1':
            self.change_block_types("level1")
        elif self.game_state == 'level2':
            self.change_block_types("level2")
            self.level_2()
        elif self.game_state == 'level3':
            self.change_block_types("level3")
        elif self.game_state == "game over":
            self.draw_game_over()


        for enemy in self.enemies:
            enemy.draw()

        self.__draw_stats()

        for coin in self.coins:
            Coins.draw(coin)

    def check_collisions(self, block1, block2):
        return (
                block1.x < block2.x + block2.width
                and block1.x + block1.width > block2.x
                and block1.y < block2.y + block2.height
                and block1.y + block1.height > block2.y
        )

    def check_all_collisions(self, block):
        # Check Collisions for Mario on top of Block
        if self.check_collisions(self.__mario, block):
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
                # Block.block_hit = True
                self.__mario.y = block.y + 8
                pass

            #  Checks if Mario Hits a block Under an Enemy
            for enemy in self.enemies:
                if not self.Player.invincible:
                    # Check if Mario hits a block under an enemy
                    if enemy.y + enemy.height == block.y and block.x < enemy.x < block.x + block.width:
                        enemy.paused = True
                        if enemy.paused:
                            self.Player.score += 100
                            enemy.speed = 1.5
                            # enemy.color = RED
        # Collision for Mario and Enemies
        if self.__mario.alive:
            for enemy in self.enemies:
                if not self.Player.invincible:
                    if self.check_collisions(self.__mario, enemy):
                        if enemy.paused:
                            enemy.alive = False
                            self.Player.score += 500
                        else:
                            if self.__mario.alive:
                                self.Player.register_hit()

        # Block Collision With Enemies
        for block in self.blocks:
            for enemy in self.enemies:
                if self.check_collisions(enemy, block):
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

                    if min_overlap == overlap_top:
                        enemy.y = block.y + enemy.height

        for coin in self.coins:
            if self.check_collisions(self.__mario, block):
                self.coins.remove(coin)
                self.Player.score += 800

    def update(self):
        if not self.Player.alive:
            self.game_state = "game over"
        else:
            self.__mario.update()

            for block_info in Constants.LEVEL1:
                block_x, block_y, block_type = block_info
                block = Block(block_x, block_y, block_type)
                self.check_all_collisions(block)

            for enemy in self.enemies:
                # Removes the enemy if it has 0 lives
                if not enemy.alive:
                    self.enemies.remove(enemy)
                else:
                    enemy.update()
                    # if enemy.paused:
                    #     enemy.speed
                    # else:
                    #     enemy.y = enemy.speed
            if self.Player.invincible:
                if self.Player.invincible_timer > 0:
                    self.Player.invincible_timer -= 1
                else:
                    self.Player.invincible = False

            # Randomly spawns enemies for each given level
            if self.game_state == 'level1':
                if self.enemy_counter <= 5:
                    if random.randint(0, 250) == 1:
                        self.enemy_counter += 1
                        self.enemies.append(Turtle(random.choice([0, 256]), random.choice([42, 96])))
                        print(self.enemy_counter)
                    if len(self.enemies) == 0 and self.enemy_counter >= 3:
                        self.game_state = 'level2'
                        self.enemy_counter = 0

            if self.game_state == 'level2':

                if self.enemy_counter <= 10:
                    if random.randint(0, 200) == 1:
                        self.enemies.append(Crab(random.choice([0, 256]), random.choice([134, 34])))
                        self.enemy_counter += 1
                        if len(self.enemies) == 0 and self.enemy_counter >= 4:
                            self.game_state = 'level3'

            elif self.game_state == 'level3':
                if self.enemy_counter <= 17:
                    if random.randint(0, 100) == 1:
                        self.enemies.append(Mushroom(random.choice([0, 256]), random.choice([134, 34])))
                        if len(self.enemies) == 0 and self.enemy_counter >= 4:
                            self.game_state = 'level4'

            elif self.game_state == 'level4':
                pass

            if random.randint(1, 250) == 1:
                self.coins.append(Coins(random.choice([0, 256]), 34))

    def spawn_mario_top(self):
        # Respawn Mario at the middle of the floor
        self.__mario.x = self.width // 2 - self.__mario.width // 2
        self.__mario.y = self.height - self.__mario.height  # Set Mario's y-coordinate to the floor level
        self.__mario.lives -= 1  # Reduce Mario's lives (or update as per your game logic)
        self.__mario.alive = self.__mario.lives > 0  # Update Mario's status to alive if lives are greater than 0

    def __draw_stats(self):
        """Draws the text elements in the game like score, highscore and lives indicator"""
        pyxel.text(2, 2, "SCORE", 7)
        pyxel.text(2, 10, str(self.Player.score), 7)
        pyxel.text(90, 10, f"Enemy Spawns Left:{5 - self.enemy_counter}", 7)

        pyxel.text(self.width - 20, 5, str(self.Player.lives) + "x", 7)
        pyxel.blt(self.width - 10, 3, 0, 16, 16, 8, 8, 0)

    def draw_game_over(self):
        self.game_state = "game over"
        pyxel.cls(0)

        pyxel.text(self.width // 2, self.height // 2, "Game Over", 7)

    def start_screen(self):
        pyxel.load('TitleScreen.pyxres')

    def level_2(self):

        if self.timer == 0:
            self.timer = pyxel.frame_count + 60

        if not pyxel.frame_count >= self.timer:
            pyxel.text(100, 50, "Level 2: Crabs Take 2 HITS", 7)

        # self.__drawBlocksLevel2()

    def level_3(self):

        if self.timer == 0:
            self.timer = pyxel.frame_count + 60

        if not pyxel.frame_count >= self.timer:
            pyxel.text(124, 50, "Level 3", 7)

        # self.__drawBlocksLevel2()

    # def level_3(self):
    #     pyxel.text(self.width // 2, 50, "LEVEL 3", 7)
