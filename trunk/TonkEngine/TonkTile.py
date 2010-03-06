# TonkEngine.TonkTile by Koen Lefever 2010, GPL v.3 licensed

import pygame
from pygame.locals import *
import math
import os


class Tile():
    """background tile"""
    
    def __init__(self, filelist = [], angle = 0, structure =[[0]], auto_anim = False, description = ''):
        self.images = []
        for filename in filelist:
            self.images.append(self.load_tile(filename))
        self.angle = angle
        self.structure = structure
        for imagenr in range(0, len(self.images)):
            original = self.images[imagenr]
            rect = original.get_rect()
            center = rect.center
            self.images[imagenr] = pygame.transform.rotate(original, angle)
        if len(self.images) == 0:
            raise ValueError('Tile has no image')
        elif len(self.images) == 1:
            self.auto_anim = False
            self.animated = False
        else:
            self.auto_anim = auto_anim
            self.animated = True
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.animstep = 0
        if math.sqrt(len(structure)) <> int(math.sqrt(len(structure))):
            raise ValueError('TonkTile structure must be square')
        self.description = description

    def update(self):
        if self.animated:
            if self.auto_anim:
                self.animstep += 1
                if self.animstep == len(self.images):
                    self.animstep = 0      
            self.image = self.images[self.animstep]
            self.rect = self.image.get_rect()

    def load_tile(self, filename):
        """loads an image, prepares it for play
        colourkey = -1 forces the left-top pixel colour to be transparent,
        use colourkey = None for non transparant surfaces """
        filename = os.path.join('Tiles', filename)
        try:
            surface = pygame.image.load(filename)
        except pygame.error:
            raise SystemExit, 'Could not load image "%s" %s'%(filename, pygame.get_error())
        surface = surface.convert()
        return surface

