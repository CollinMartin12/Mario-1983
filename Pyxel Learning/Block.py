import pyxel

import Constants

class Block:

    def __init__(self, x: int, y: int, block_type: str):
        ''' Init method, creates the initial attributes of the block '''
        self.x = x
        self.y = y
        self.block_type = block_type
        self.width = 8
        self.height = 32




    def draw(self):
        if self.block_type == "BLOCK1":
            pyxel.blt(self.x, self.y, 0, 32, 72, self.height, self.width, colkey=0)
        elif self.block_type == "BLOCK2":
            pyxel.blt(self.x, self.y, 0, 0, 64, self.height, self.width, colkey=0)
        elif self.block_type == "POW":
            pyxel.blt(self.x, self.y, 0, 0, 64, self.height, self.width, colkey=0)
        else:
            print("Block called "+self.block_type + " doesn't exist")

    """ These are the methods that will be used to assign values to the 
    attributes """


