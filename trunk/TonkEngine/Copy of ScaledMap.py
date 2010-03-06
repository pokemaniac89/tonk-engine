# TonkEngine.ScaledMap, Koen Lefever 2010, GPL v.3 licensed

import pygame
from pygame.locals import Rect

class ScaledMap():
    def __init__(self, world, width = -1, height = -1, widthscale = -1, heightscale = -1,
                 smooth = True, floating_point = False):
        if widthscale == -1 and heightscale == -1:
            if floating_point:
                self.width = float(width)
                self.height = float(height)
            else:
                self.width = int(width)
                self.height = int(height)
            self.widthscale = world.worldwidth / self.width
            self.heightscale = world.worldheight / self.height
        elif width == -1 and height == -1:
            if floating_point:
                self.widthscale = float(widthscale)
                self.heightscale = float(heightscale)
            else:
                self.widthscale = int(widthscale)
                self.heightscale = int(heightscale)
            self.width = world.worldwidth / self.widthscale
            self.height = world.worldwidth / self.heightscale
        else:
            raise ValueError('(width == -1, height == -1) xor (widthscale == -1, heightscale == -1)')
        self.image = pygame.Surface((int(round(self.width)), int(round(self.height))))
        self.scaled_tile_width = world.tileset.tilewidth / self.widthscale
        self.scaled_tile_height = world.tileset.tileheight / self.heightscale
        self.smooth = smooth
        scaled_tiles = []
        for tile in world.tileset.tilelist:
            if floating_point:
                self.scaled_tile_width = int(round(self.scaled_tile_width))
                self.scaled_tile_height = int(round(self.scaled_tile_height))
            if smooth:
                scaled_tile = pygame.transform.smoothscale(tile.images[0],
                                                           (self.scaled_tile_width, self.scaled_tile_height))
            else:
                scaled_tile = pygame.transform.scale(tile.images[0],
                                                     (self.scaled_tile_width, self.scaled_tile_height))
            scaled_tiles.append(scaled_tile.convert())
        for x in range(0, world.tilemap.rows):
            for y in range(0, world.tilemap.columns):
                self.image.blit(scaled_tiles[world.tilemap.map[x][y]],
                                (x * self.scaled_tile_width, y * self.scaled_tile_height))                
                
       
