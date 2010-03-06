# TonkEngine.TileMap by Koen Lefever 2010, GPL v.3 licensed

import pygame
from pygame.locals import *

class TileMap():
    """background map"""
    
    def __init__(self, map_of_tiles = [[]], nr_of_rows = -1, nr_of_columns = -1, tilenr = 0, description = ''):
        self.map = map_of_tiles
        self.columns = len(self.map)
        self.rows = len(max(self.map))
        if self.columns < nr_of_columns:
            self.columns = nr_of_columns
        if self.rows < nr_of_rows:
            self.rows = nr_of_rows
        # make tilemap rectangular
        for x in range (0, self.columns):
            if self.columns >= len(self.map):
                self.map.append([])
            while len(self.map[x]) < self.rows:
                self.map[x].append(tilenr)
        
    def set_tile(self, x = 0, y = 0, tilenr = 0):
        self.map[x][y] = tilenr

    def set_border(self, depth = 1, tilenr = 0):
        for d in range(0, depth):
            for x in range(0,self.columns):
                self.map[x][d] = tilenr
                self.map[x][self.rows - d - 1] = tilenr
            for y in range(0, self.rows):
                self.map[d][y] = tilenr
                self.map[self.columns -d - 1][y] = tilenr

    def fill_rect(self, x = 0 , y = 0, width = -1, height = -1, xmax = -1, ymax = -1, tilenr = 0):
        if xmax < 0:
            xmax = x + width + 1
        if ymax < 0:
            ymax = y + height + 1
        for col in range(x, xmax):
            for row in range(y, ymax):
                self.map[col][row] = tilenr

        
