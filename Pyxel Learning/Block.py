import pyxel
import Constants


class Block:
    '''This is a Class For the blocks to be printed
    it runs through the Constants file where the dimmensions are stored and then prints a block
    in each desired area'''
    def __init__(self, x: int, y: int, block_type: str):
        ''' Init method, creates the initial attributes of the block '''
        self.x = x
        self.y = y
        self.block_type = block_type
        self.width = 8
        self.height = 32




    def draw(self):

        pyxel.blt(self.x, self.y, 0, 32, 72, self.height, self.width, colkey=0)



