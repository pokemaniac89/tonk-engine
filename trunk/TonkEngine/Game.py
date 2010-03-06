# TonkEngine.Game 0.0.1 by Koen Lefever 2010, GPL v.3 licensed
#####################################################################

import pygame
from pygame.locals import *

class Game():    
    """Simple 2D game engine with scrolling & animated background"""
    def __init__(self, world, screen):
        # test if we can load more than standard BMP
        if not pygame.image.get_extended():
            raise SystemExit, "Sorry, extended image module required"
        self.clock = pygame.time.Clock()
        # various variables
        self.screen = screen
        self.world = world
        self.framecounter = 0   # will be incremented every update
        self.state = 1          # 0 = quiting, 1 = active, 2 = Esc button pressed


    def update(self):
        # get input
        events = []
        keystate = pygame.key.get_pressed()
        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            events.append(event)
            if event.type == QUIT:
                self.state = 0
                return(events, keystate, mousex, mousey)
            elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.state = 2
            else:
                self.state = 1
        # paint screen
        self.screen.paint(self.world)
        self.clock.tick(self.screen.framerate)
        self.framecounter += 1
        return(events, keystate, mousex, mousey)
