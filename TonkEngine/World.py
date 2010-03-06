# TonkEngine.World, Koen Lefever 2010, GPL v.3 licensed

import pygame
from pygame.locals import Rect

class World():
    def __init__(self, tileset = [], tilemap = [[]], tonkspritelist = []):
        self.tileset = tileset
        self.tilemap = tilemap
        self.worldheight = tilemap.columns * tileset.tileheight
        self.worldwidth = tilemap.rows * tileset.tilewidth
        self.worldrect = Rect(0, 0, self.worldwidth, self.worldheight)      # the completre game world
        self.tonkspritelist = tonkspritelist
