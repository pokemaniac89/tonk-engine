# TonkEngine.TonkTile by Koen Lefever 2010, GPL v.3 licensed

# only one screen may exist at any time (this is due to SDL on which pygame is built)

import pygame
from pygame.locals import *
import os

class Screen():
    """display - only one screen may exist at any time"""
    def __init__(self, resolution = (300, 200), camera = (150,100),
                 fullscreen = False, framerate = 40, caption = 'TonkEngine', pointer = False):
        self.resolution = resolution                            # physical screen limits
        (self.screenwidth, self.screenheight) = resolution  
        self.screenrect = Rect(0, 0, self.screenwidth, self.screenheight)                 
        self.fullscreen = fullscreen                            # True or False
        if fullscreen:
            self.bestdepth = pygame.display.mode_ok(self.screenrect.size, pygame.FULLSCREEN, 32)
            self.screen = pygame.display.set_mode(self.screenrect.size, pygame.FULLSCREEN, self.bestdepth)
        else:
            self.screen = pygame.display.set_mode(self.screenrect.size)
        self.framerate = framerate                              # for screen update timing
        pygame.display.set_caption(caption)
        self.pointer = pointer                                  # mouse pointer visibility, True or False
        pygame.mouse.set_visible(self.pointer)
        #self.background = pygame.Surface(self.screenrect.size)
        #self.background = self.background.convert()
        # screen properties relative to the game world
        (self.camera_x, self.camera_y) = camera                   # co-ordinates of center of screen in the game world
        self.visiblerect = Rect(self.camera_x - self.screenwidth/2, self.camera_y - self.screenheight/2, self.screenwidth, self.screenheight)
        self.visible_x = self.visiblerect.left
        self.visible_y = self.visiblerect.top

        filename = os.path.join('Sprites', 'background_bottom.png')
        try:
            self.background_bottom = pygame.image.load(filename)
        except pygame.error:
            raise SystemExit, 'Could not load image "%s" %s'%(filename, pygame.get_error())
        self.background_bottom = self.background_bottom.convert()
        
        filename = os.path.join('Sprites', 'background_top.png')
        try:
            self.background_top = pygame.image.load(filename)
        except pygame.error:
            raise SystemExit, 'Could not load image "%s" %s'%(filename, pygame.get_error())
        self.background_top = self.background_top.convert()
        colorkey = self.background_top.get_at((0,0))
        self.background_top.set_colorkey(colorkey, RLEACCEL)

        self.background = self.background_bottom.copy()
        self.background.blit(self.background_top, (0, 0))
        
        
    def show_pointer(self):
        self.pointer = True
        pygame.mouse.set_visible(self.pointer)

    def hide_pointer(self):
        self.pointer = False
        pygame.mouse.set_visible(self.pointer)

    def move_camera_to(self, x, y):
        self.camera_x = x
        self.camera_y = y
        self.visiblerect = Rect(self.camera_x - (self.screenwidth/2), self.camera_y - (self.screenheight/2), self.screenwidth, self.screenheight)
        self.visible_x = self.visiblerect.left
        self.visible_y = self.visiblerect.top
    
    def draw_background(self, world):
        for tile in world.tileset.tilelist:
            tile.update()
        for y in range(self.visible_y / world.tileset.tileheight,
                       (self.visible_y + self.screenheight) / world.tileset.tileheight + 1):
            for x in range(self.visible_x / world.tileset.tilewidth,
                           (self.visible_x + self.screenwidth) / world.tileset.tilewidth + 1):
                if x < 0 or y < 0 or x >= world.tilemap.columns or y >= world.tilemap.rows:
                    tilenr = 0
                else:
                    tilenr = world.tilemap.map[x][y]
                xpos = (x * world.tileset.tilewidth) - self.visible_x
                ypos = (y * world.tileset.tileheight) - self.visible_y
                self.background.blit(world.tileset.tilelist[tilenr].image, (xpos, ypos))
        self.screen.blit(self.background, (0,0))

    def update_sprites(self, world):
        self.visiblesprites = []
        for sprite in world.tonkspritelist:
            sprite.update()
            if sprite.visible:
                if sprite.absolute or self.visiblerect.colliderect(Rect(sprite.x, sprite.y, sprite.rect.width, sprite.rect.height)):
                    self.visiblesprites.append(sprite)

    def draw_sprites(self):
        # sorting by z-axis does not work yet
        #self.visiblesprites.sort(cmp = lambda sprite1, sprite2: (sprite1.z <= sprite2.z))
        for sprite in self.visiblesprites:
            if sprite.absolute:
                screen_x = sprite.x
                screen_y = sprite.y
            else:
                screen_x = sprite.x - self.visible_x
                screen_y = sprite.y - self.visible_y
            self.screen.blit(sprite.image, (screen_x, screen_y))
                
    def paint(self, world):
        self.screen.fill((0,33,33))
        #self.draw_background(world)
        self.draw_sprites()
        pygame.display.flip()

