import pyxel
class WorldItem:

    WALL = (0,1)
    CORRIDOR = (0,0)
    Player = (0,3)



class World:

    HEIGHT = 16
    WIDTH = 16

    def __init__(self, tilemap):
        self.tilemap = tilemap
        self.world = []
        self.player_grid_x = 0
        self.player_grid_y = 0

        for y in range(self.HEIGHT):
            self.world.append([])
            for x in range(self.WIDTH):
                if self.tilemap.pget(x,y) == WorldItem.WALL:
                    self.world[y].append(WorldItem.WALL)
                elif self.tilemap.pget(x,y) == WorldItem.CORRIDOR:
                    self.world[y].append(WorldItem.CORRIDOR)
                    self.player_grid_x = x
                    self.player_grid_y = y

def world_item_draw(pyxel,x,y,world_item):
    pyxel.blt()
    x = x
    y = y
    world_item = world_item

