# TonkEngine.TonkSprite by Koen Lefever 2010, GPL v.3 licensed

import pygame
from pygame.locals import *
import math
import os

def load_sprite(filename, colorkey = -1):
    """loads an image, prepares it for play
    colourkey = -1 forces the left-top pixel colour to be transparent,
    use colourkey = None for non transparant surfaces """
    filename = os.path.join('Sprites', filename)
    try:
        surface = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit, 'Could not load image "%s" %s'%(filename, pygame.get_error())
    surface = surface.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = surface.get_at((0,0))
        surface.set_colorkey(colorkey, RLEACCEL)
    return surface

def collide(sprite, spritelist):
    """determine collision of a sprite and sprites in a list (or any objects with a rect attribute)
        do not use this to detect collisions between absolute & relative sprites"""
    returnlist = []
    for testsprite in spritelist:
        if (sprite.absolute and testsprite.absolute) or (not sprite.absolute and not testsprite.absolute):
            if sprite.rect.colliderect(testsprite.rect):
                returnlist.append(spritelist.index(testsprite))
            else:
                pass
                #raise ValueError('do not use this to detect collisions between absolute & relative sprites')
    return(returnlist)

class Sprite():
    """sprite class for use in the TonkEngine, does not use pygame's built-in sprites"""
    
    def __init__(self, x = 0, y = 0, z = 0, angle = 0,
                 imageslist = [], filelist = [], colorkey = -1,
                 absolute = True, visible = True, auto_anim = True):
        self.images = []
        for img in imageslist:
            self.images.append(img)
        self.colorkey = colorkey
        for filename in filelist:
                self.images.append(load_sprite(filename, colorkey))
        if len(self.images) <= 1:
            self.auto_anim = False
            self.animated = False
        else:
            self.auto_anim = auto_anim
            self.animated = True
        self.x = x
        self.y = y
        self.absolute = absolute
        #if absolute:
        #    self.screenx = x
        #    self.screeny = y
        #else:
        #    self.worldx = x
        #    self.worldy = y
        self.z = z
        self.angle = angle
        self.visible = visible
        if len(self.images) >0:
            original = self.images[0]
            self.rect = original.get_rect()
            self.rect.move_ip(x, y)
            center = self.rect.center
            self.image = pygame.transform.rotate(original, angle)
            self.rect = self.image.get_rect(center = center)
        self.animstep = 0
        self.moved = False

    def move_to(self, x, y, z = None, angle = None, visible = None):
        x_offset = x - self.x
        y_offset = y - self.y
        self.x = x
        self.y = y
        #if self.absolute:
        #    xoffset = x - self.screenx
        #    yoffset = y - self.screeny
        #    self.screenx = x
        #    self.screeny = y
        #else:
        #    xoffset = x - self.worldx
        #    yoffset = y - self.worldy
        #    self.worldx = x
        #    self.worldy = y
        self.rect.move_ip((x_offset, y_offset))
        if not z == None:
            self.z = z
        if not angle == None:
            self.angle = angle
        if not visible == None:
            self.visible = visible
        self.moved = True

    def move(self, x_offset, y_offset, z = None, angle = None, visible = None):
        self.x += x_offset
        self.y += y_offset
        #if self.absolute:
        #    self.screenx += x_offset
        #    self.screeny += y_offset
        #else:
        #    self.worldx += x_offset
        #    self.worldy += y_offset
        self.rect.move_ip((x_offset, y_offset))
        if not z == None:
            self.z = z
        if not angle == None:
            self.angle = angle
        if not visible == None:
            self.visible = visible
        self.moved = True

    def set_animation(self, animstep, auto_anim = False):
        self.animstep = animstep
        self.auto_anim = auto_anim
        self.moved = True

    def update(self):
        if (self.animated or self.moved) and len(self.images) > 0:
            #if self.absolute:
            #    (self.x, self.y) = (self.screenx, self.screeny)
            #else:
            #    (self.x, self.y) = (self.worldx, self.worldy)
            if self.auto_anim:
                self.animstep += 1
            if self.animstep >= len(self.images):
                self.animstep = 0
            if self.angle == 0:
                self.image = self.images[self.animstep].copy()
            else:
                original = self.images[self.animstep]
                center = self.rect.center
                self.image = pygame.transform.rotate(original, self.angle)
                self.rect = self.image.get_rect(center = center)
                self.x = self.rect.left
                self.y = self.rect.top
                #if self.absolute:
                #    (self.screenx, self.screeny) = (self.x, self.y)
                #else:
                #    (self.worldx, self.worldy) = (self.x, self.y)
            self.moved = False



            
