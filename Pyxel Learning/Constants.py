WIDTH = 256
HEIGHT = 224
FLOOR = 180

# Mario
MARIO_INITIAL = (WIDTH / 2, 180)
MARIO_SPRITE = (0, 0, 8, 16, 24)
TURTLE_SPRITE = (0, 0, 184, 16, 16)
TURTLE_INITIAL = (0, 180)

# Define sprite coordinates
LEFT_RUNNING_SPRITE = (0, 16, 8, 16, 24, 0)
LEFT_JUMPING_SPRITE = (0, 64, 8, 16, 24, 0)
LEFT_DEFAULT_SPRITE = (0, 0, 8, 16, 24, 0)
RIGHT_RUNNING_SPRITE = (0, 16, 8, 16, 24, 0)
RIGHT_JUMPING_SPRITE = (0, 64, 8, 16, 24, 0)
RIGHT_DEFAULT_SPRITE = (0, 0, 8, 16, 24, 0)

POW = (124, 150, "POW")

# Enemies

SPRITE_BLOCK_1 = (0, 0, 112, 16, 8)  # ALL SPRITE BLOCKS ARE THE COORDINATES OF WHERE THEY ARE ON THE PYXEL EDITOR

SPRITE_BLOCK_2 = (0, 0, 128, 16, 8)

SPRITE_BLOCK_3 = (0, 0, 144, 16, 8)

SPRITE_BLOCK_4 = (0, 112, 144, 16, 8)

SPRITE_POW = (0, 88, 48, 16, 16)
SPRITE_PIPE_LEFT = (0, 48, 88, 16, 16)
SPRITE_PIPE_RIGHT = (0, 96, 88, 16, 16)
SPRITE_FLOOR = (0, 64, 48, 16, 16)

SPRITE_PIPE_RIGHT_UPPER_LEFT = (0, 0, 64, 16, 16)
SPRITE_PIPE_RIGHT_LOWER_LEFT = (0, 0, 88, 16, 16)
SPRITE_PIPE_RIGHT_UPPER = (0, 24, 64, 16, 16)
SPRITE_PIPE_RIGHT_LOWER = (0, 24, 88, 16, 16)

SPRITE_PIPE_LEFT_UPPER_LEFT = (0, 120, 64, 16, 16)  # PIPE LEFT
SPRITE_PIPE_LEFT_LOWER_LEFT = (0, 120, 88, 16, 16)
SPRITE_PIPE_LEFT_UPPER_RIGHT = (0, 144, 64, 16, 16)
SPRITE_PIPE_LEFT_LOWER_RIGHT = (0, 144, 88, 16, 16)

PIPES_INITIAL = [(0, 176, "PIPE_RIGHT"), (240, 176, "PIPE_LEFT"), (240, 32, 'PIPE_RIGHT_LOWER'),
                 (224, 32, "PIPE_RIGHT_LOWER_LEFT"), (0, 16, "PIPE_LEFT_UPPER_LEFT"),
                 (0, 32, "PIPE_LEFT_LOWER_LEFT"),
                 (224, 16, "PIPE_RIGHT_UPPER_LEFT"),
                 (16, 16, "PIPE_LEFT_UPPER_RIGHT"),
                 (16, 32, "PIPE_LEFT_LOWER_RIGHT"),
                 (240, 16, "PIPE_RIGHT_UPPER_RIGHT"),
                 ]
PIPE_Y_POSITION = 100  # Example pipe y-coordinate
PIPE_X_POSITION_LEFT = 100  # Example left pipe x-coordinate
PIPE_X_POSITION_RIGHT = 200  # Example right pipe x-coordinate
PIPE_WIDTH = 20  # Example pipe width
TOP_OF_SCREEN_Y = 0

LEVEL1 = [
    (0, 50, "BLOCK1"), (16, 50, "BLOCK1"), (32, 50, "BLOCK1"), (48, 50, "BLOCK1"),
    (64, 50, "BLOCK1"), (80, 50, 'BLOCK1'), (124, 150, "POW"), (210, 50, "BLOCK1"),
    (240, 50, "BLOCK1"), (224, 50, "BLOCK1"), (208, 50, "BLOCK1"), (192, 50, "BLOCK1"),
    (176, 50, "BLOCK1"), (164, 50, "BLOCK1"), (224, 110, "BLOCK1"), (0, 110, "BLOCK1"),
    (16, 110, "BLOCK1"), (240, 110, "BLOCK1"), (224, 110, "BLOCK1"), (240, 110, "BLOCK1"),
    (124, 100, "BLOCK1"), (112, 100, "BLOCK1"), (140, 100, "BLOCK1"), (156, 100, "BLOCK1"),
    (96, 100, "BLOCK1"), (86, 100, "BLOCK1"), (208, 150, "BLOCK1"), (192, 150, "BLOCK1"),
    (0, 150, "BLOCK1"), (16, 150, "BLOCK1"), (32, 150, "BLOCK1"), (48, 150, "BLOCK1"),
    (240, 150, "BLOCK1"), (224, 150, "BLOCK1"), (208, 150, "BLOCK1"), (192, 150, "BLOCK1"),
    (0, 195, "FLOOR"),
    (16, 195, "FLOOR"), (32, 195, "FLOOR"), (48, 195, "FLOOR"), (64, 195, "FLOOR"),
    (80, 195, "FLOOR"),
    (96, 195, "FLOOR"),
    (112, 195, "FLOOR"),
    (128, 195, "FLOOR"),
    (144, 195, "FLOOR"),
    (160, 195, "FLOOR"),
    (176, 195, "FLOOR"),
    (192, 195, "FLOOR"),
    (208, 195, "FLOOR"),
    (224, 195, "FLOOR"),
    (240, 195, "FLOOR"), ]
LEVEL2 = [(x, y, "BLOCK2") if block == "BLOCK1" else (x, y, block) for x, y, block in LEVEL1]

LEVEL3 = [(x, y, "BLOCK3") if block == "BLOCK2" else (x, y, block) for x, y, block in LEVEL2]

LEVEL4 = [(x, y, "BLOCK4") if block == "BLOCK3" else (x, y, block) for x, y, block in LEVEL3]







