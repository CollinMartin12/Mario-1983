import Constants


class Block:
    """Class block holds all the sprites for the necessary blocks"""

    def __init__(self, x: int, y: int, block_type: str):
        """ Init method, creates the initial attributes of the block """
        self.x = x
        self.y = y
        self.block_type = block_type
        self.width = 16
        self.height = 8

        self.used_pow = False




    @property
    def sprite(self) -> tuple:
        global sprite
        if self.block_type == "BLOCK1":
            sprite = Constants.SPRITE_BLOCK_1
        elif self.block_type == "BLOCK2":
            sprite = Constants.SPRITE_BLOCK_2
        elif self.block_type == "BLOCK3":
            sprite = Constants.SPRITE_BLOCK_3
        elif self.block_type == "BLOCK4":
            sprite = Constants.SPRITE_BLOCK_4
        elif self.block_type == "POW" and not self.used_pow:
            sprite = Constants.SPRITE_POW
        elif self.block_type == "POW" and self.used_pow:
            sprite = Constants.SPRITE_POW
        elif self.block_type == "PIPE_LEFT":
            sprite = Constants.SPRITE_PIPE_LEFT
        elif self.block_type == "PIPE_RIGHT":
            sprite = Constants.SPRITE_PIPE_RIGHT
        elif self.block_type == "FLOOR":
            sprite = Constants.SPRITE_FLOOR
        elif self.block_type == 'PIPE_RIGHT_UPPER':
            sprite = Constants.SPRITE_PIPE_RIGHT_UPPER
        elif self.block_type == 'PIPE_RIGHT_LOWER':
            sprite = Constants.SPRITE_PIPE_RIGHT_LOWER
        elif self.block_type == 'PIPE_RIGHT_UPPER_LEFT':
            sprite = Constants.SPRITE_PIPE_RIGHT_UPPER_LEFT
        elif self.block_type == 'PIPE_RIGHT_LOWER_LEFT':
            sprite = Constants.SPRITE_PIPE_RIGHT_LOWER_LEFT
        elif self.block_type == 'PIPE_RIGHT_UPPER_RIGHT':
            sprite = Constants.SPRITE_PIPE_RIGHT_UPPER
        elif self.block_type == 'PIPE_RIGHT_LOWER_RIGHT':
            sprite = Constants.SPRITE_PIPE_RIGHT_LOWER
        elif self.block_type == 'PIPE_LEFT_UPPER_LEFT':
            sprite = Constants.SPRITE_PIPE_LEFT_UPPER_LEFT
        elif self.block_type == 'PIPE_LEFT_LOWER_LEFT':
            sprite = Constants.SPRITE_PIPE_LEFT_LOWER_LEFT
        elif self.block_type == 'PIPE_LEFT_UPPER_RIGHT':
            sprite = Constants.SPRITE_PIPE_LEFT_UPPER_RIGHT
        elif self.block_type == 'PIPE_LEFT_LOWER_RIGHT':
            sprite = Constants.SPRITE_PIPE_LEFT_LOWER_RIGHT
        return sprite





