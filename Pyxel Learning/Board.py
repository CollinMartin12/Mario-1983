import Constants
from Mario import Mario
import pyxel
from Block import Block





class Board:
    """This class contains the necessary information to
    represent the board"""

    def __init__(self, width: int, height: int):
        """These parameters are the width and height of the board"""
        # Initialize the object
        self.width = width
        self.height = height

        # This block initializes pyxel
        # The first thing we need to do is create the screen, see the API
        # for more parameters
        pyxel.init(self.width, self.height, title="Mario Bros")

        # Load the pyxres file we are going to use
        # pyxel.load("my_resource.pyxres")
        # If we want to load Mario from a png
        # pyxel.image(1).load(0, 0, "my_resource.pyxres")

        # Create Mario in the middle of the screen at x and y = 200
        # Make it private so that only the board can view and change it
        self.__mario = Mario(*Constants.MARIO_INITIAL)

        # Create the blocks
        self.__blocks = []
        for element in Constants.BLOCK_INITIAL:
            self.__blocks.append(Block(*element))


        # Run the game
        # pyxel.run(self.update, self.draw)

    # Here I am defining the width attribute as a property
    @property
    def width(self) -> int:
        """This is the method that will be used to read the value
        of the attribute"""
        # Here I must return the value of the attribute as if it were
        # private
        return self.__width

    # Here I am defining the height attribute as a property
    @property
    def height(self) -> int:
        """This is the method that will be used to read the value
        of the attribute"""
        # Here I must return the value of the attribute as if it were
        # private
        return self.__height

    """These are the methods that will be used to assign values to the
    attributes"""
    @width.setter
    def width(self, width:int):
        if width > 0:
            self.__width = width
        else:
            self.__width = 256

    @height.setter
    def height(self, height:int):
        if height > 0:
            self.__height = height
        else:
            self.__height = 256

    def update(self):
        """This code runs every frame, here we invoke
        the methods that update the different objects"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Only perform Mario's horizontal movement
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.__mario.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.__mario.move('left', self.width)

    def __drawMario(self):
        """Draw Mario taking values from the Mario object
        The parameters are x and y on the screen and a tuple containing:
        the image bank number, the x and y of the image in the bank,
        and the size of the image"""
        # pyxel.blt(self.__mario.x, self.__mario.y, *self.__mario.sprite)


    def __drawBlocks(self):
        for block in self.__blocks:
            block.draw()

    def draw(self):
        """This code also runs every frame, here you should draw the
        objects
        """
        pyxel.cls(0)

        self.__drawMario()
        self.__drawBlocks()
