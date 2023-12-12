import pyxel
import Constants


class Block:
    '''This is a Class For the blocks to be printed
    it runs through the Constants file where the dimmensions are stored and then prints a block
    in each desired area'''

    def __init__(self, x: int, y: int, block_type: str):
        """ Init method, creates the initial attributes of the block """
        self.x = x
        self.y = y
        self.block_type = block_type
        self.width = 16
        self.height = 8
        self.block_hit = False
        self.animation_frames = 0


    def update(self):
        if self.block_hit:
            if self.animation_frames < 3:

                self.block_type = f'HIT{self.animation_frames + 1}'
                print(self.block_type)

                self.animation_frames += 1
            else:

                self.block_hit = False
                self.block_type = 'BLOCK1'
                self.animation_frames = 0

    @property
    def sprite(self) -> tuple:
        global sprite
        if self.block_type == "BLOCK1":
            sprite = Constants.SPRITE_BLOCK_1
        elif self.block_type == 'HIT1':
            sprite = Constants.HIT_BLOCK_1
        elif self.block_type == "BLOCK2":
            sprite = Constants.SPRITE_BLOCK_2
        elif self.block_type == "POW":
            sprite = Constants.SPRITE_POW
        elif self.block_type == "PIPE_LEFT":
            sprite = Constants.SPRITE_PIPE_LEFT
        elif self.block_type == "PIPE_RIGHT":
            sprite = Constants.SPRITE_PIPE_RIGHT
        elif self.block_type == "FLOOR":
            sprite = Constants.SPRITE_FLOOR
        return sprite
