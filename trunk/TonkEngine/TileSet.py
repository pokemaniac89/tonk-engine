# TonkEngine.TileSet by Koen Lefever 2010, GPL v.3 licensed

import TonkTile
from pygame.locals import *

class TileSet():
    """set of background tiles"""
    
    def __init__(self, tilelist = [], description = ''):
        self.tilelist = tilelist
        if self.tilelist == []:
            (self.tilewidth, self.tileheight) = (-1, -1)
        else:
            self.tilewidth = self.tilelist[0].image.get_width()
            self.tileheight = self.tilelist[0].image.get_height()
            self.tilesize = (self.tilewidth, self.tileheight)
            self.tilerect = Rect(0, 0, self.tilewidth, self.tileheight)  # all background tiles must have this size
        self.description = description
