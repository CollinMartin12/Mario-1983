
WIDTH = 256
HEIGHT = 224
FLOOR = 180

# Mario
MARIO_INITIAL = (WIDTH / 2, 180)
MARIO_SPRITE = (0, 0, 0, 16, 16)


# Enemies
SPRITE_BLOCK_1 = (0, 32, 72, 16, 16) # ALL SPRITE BLOCKS ARE THE COORDINATES OF WHERE THEY ARE ON THE PYXEL EDITOR
SPRITE_BLOCK_2 = (0, 32, 72, 16, 16)
SPRITE_POW = (0, 48, 16, 16, 16)
SPRITE_PIPE_LEFT = (0, 0, 16, 16, 16)
SPRITE_PIPE_RIGHT = (0, 32, 16, 16, 16)
BLOCK_INITIAL = [
    (0, 50, "BLOCK1"), (16, 50, "BLOCK1"), (32, 50, "BLOCK1"), (48, 50, "BLOCK1"),
    (64, 50, "BLOCK1"), (80, 50, 'BLOCK1'), (124, 150, "POW"), (210, 50, "BLOCK1"),
    (240, 50, "BLOCK1"), (224, 50, "BLOCK1"), (208, 50, "BLOCK1"), (192, 50, "BLOCK1"),
    (176, 50, "BLOCK1"), (164, 50, "BLOCK1"), (224, 110, "BLOCK2"), (0, 110, "BLOCK2"),
    (16, 110, "BLOCK2"), (240, 110, "BLOCK2"), (224, 110, "BLOCK2"), (240, 110, "BLOCK2"),
    (124, 100, "MIDDLE"), (112, 100, "MIDDLE"), (140, 100, "MIDDLE"), (156, 100, "MIDDLE"),
    (96, 100, "MIDDLE"), (86, 100, "MIDDLE"), (208, 150, "BLOCK3"), (192, 150, "BLOCK3"),
    (0, 150, "BLOCK3"), (16, 150, "BLOCK1"), (32, 150, "BLOCK3"), (48, 150, "BLOCK3"),
    (240, 150, "BLOCK3"), (224, 150, "BLOCK3"), (208, 150, "BLOCK3"), (192, 150, "BLOCK3"),
    (0, 176, "PIPE_RIGHT"), (240, 176, "PIPE_LEFT")
]
