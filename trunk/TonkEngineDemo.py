#!/usr/bin/env python
#
# TonkEngineDemo, Koen Lefever 2010, GPL v.3 licensed
#
#
#####################################################################

import pygame
from pygame.locals import *         # http://www.pygame.org/
import TonkEngine
import math

def main(winstyle = 0):

    # Create the display
    display_created = False
    while not display_created:
        print 'TonkEngine 0.0.1 Demo'
        print '---------------------'
        print
        print '1. 200 * 200 in a window'
        print '2. 1024 * 600 in a window'
        print '3. 1024 * 600 full screen'
        print '4. 1024 * 768 in a window'
        print '5. 1024 * 768 full screen'
        print '6. Other resolution in a window'
        print '7. Other resolution full screen'
        print
        screenmode = raw_input('Select resolution (1-7): ')
        print
        if screenmode == '2':
            resolution = (1024, 600)
            fullscreen = False        
        elif screenmode == '3':
            resolution = (1024, 600)
            fullscreen = True        
        elif screenmode == '4':
            resolution = (1024, 768)
            fullscreen = False        
        elif screenmode == '5':
            resolution = (1024, 768)
            fullscreen = True
        elif screenmode == '6':
            screenwidth = int(raw_input('Window width : '))
            screenheight = int(raw_input('Window height: '))
            resolution = (screenwidth, screenheight)
            fullscreen = False
        elif screenmode == '7':
            screenwidth = int(raw_input('Screen width : '))
            screenheight = int(raw_input('Screen height: '))
            resolution = (screenwidth, screenheight)
            fullscreen = True
        else:
            screenmode = '1'
            resolution = (200, 200)
            fullscreen = False
        try:
            display = TonkEngine.Screen(resolution = resolution, fullscreen = fullscreen,
                                        camera = (1800,1400), framerate = 90,
                                        caption = 'TonkEngine Demo', pointer = False)
            display_created = True
        except:
            print "This resolution is not accepted."
            print

    # create tileset
    tileset = TonkEngine.TileSet([TonkEngine.Tile(['b00.PNG'], 0, [0], False, 'water / out of map')])

    # create map of the world
    tilemap = TonkEngine.TileMap(nr_of_rows = 50, nr_of_columns = 50, tilenr = 0, description = 'Demo map')

    # Create game world
    world = TonkEngine.World(tileset = tileset, tilemap = tilemap)

    # create sprites
    background_bottom = TonkEngine.Sprite(x = 0, y = 0, z = 0, angle =0, imageslist = [display.background_bottom], absolute = False)
    background_top = TonkEngine.Sprite(x = 0, y = 0, z = 6, angle =0, imageslist = [display.background_top], absolute = False)
    red_tank = TonkEngine.Sprite(x = 2567, y = 2780,z = 2, angle =0, filelist = ['red_tank.png'], absolute = False)
    red_shadow = TonkEngine.Sprite(x = 2564, y = 2783,z = 2, angle =0, filelist = ['tank_shadow1.png'], absolute = False)
    grey_tank = TonkEngine.Sprite(x = 2312, y = 2595, z = 4, filelist = ['grey_tank.png'], absolute = False)
    grey_shadow = TonkEngine.Sprite(x = 2309, y = 2598, z = 4, filelist = ['tank_shadow.png'], absolute = False)
    explosion = TonkEngine.Sprite(x = 2247, y = 2555, z=5, absolute = False,
                           filelist = ['boom-1-0001.png', 'boom-1-0002.png', 'boom-1-0003.png', 'boom-1-0004.png', 'boom-1-0005.png',
                                       'boom-1-0006.png', 'boom-1-0007.png', 'boom-1-0008.png', 'boom-1-0009.png', 'boom-1-0010.png',
                                       'boom-1-0011.png', 'boom-1-0012.png', 'boom-1-0013.png', 'boom-1-0014.png', 'boom-1-0015.png',
                                       'boom-1-0016.png', 'boom-1-0017.png', 'boom-1-0018.png', 'boom-1-0019.png', 'boom-1-0020.png',
                                       'boom-1-0027.png', 'boom-1-0030.png', 'boom-1-0033.png', 'boom-1-0036.png', 'boom-1-0039.png',
                                       'boom-1-0042.png', 'boom-1-0045.png', 'boom-1-0048.png', 'boom-1-0051.png', 'boom-1-0054.png',
                                       'boom-1-0057.png', 'boom-1-0060.png', 'boom-1-0063.png', 'boom-1-0066.png', 'boom-1-0069.png',
                                       'boom-1-0072.png', 'boom-1-0075.png', 'boom-1-0078.png', 'boom-1-0081.png', 'boom-1-0084.png',
                                       'boom-1-0087.png', 'boom-1-0090.png', 'boom-1-0093.png', 'boom-1-0096.png', 'boom-1-0099.png'])
    logo = TonkEngine.Sprite(x = 2912, y = 2570, z = 0, filelist = ['tonk_engine.png'], angle = 20, absolute = False)
    world.tonkspritelist += [background_bottom, grey_shadow, grey_tank, red_shadow,
                             red_tank, background_top, logo, explosion]
    if display.screenwidth > 500:
        simplesprite = TonkEngine.Sprite(x = display.screenwidth - 395, y = display.screenheight - 200, z = 10,
                                  filelist = ['simplesprite.png'], absolute = True)        
        world.tonkspritelist.append(simplesprite)

    # create minimap
    imageslist = []
    maxmap = min(resolution)
    scaleslist = [1]
    for s in range(50, maxmap + 1, 50):
        scaleslist.append(s)
    for minimap_size in scaleslist:
        #scaled_map = TonkEngine.ScaledMap(world, width = minimap_size, height = minimap_size, smooth = True, floating_point = True)
        scaled_map = pygame.transform.scale(display.background,
                                                     (minimap_size, minimap_size))
        imageslist.append(scaled_map)
    minimap = TonkEngine.Sprite(x = 5, y = 5, z = 10,
                                  imageslist = imageslist, absolute = True, auto_anim = False)
    if screenmode in ('1', '6', '7'):
        minimap.animstep = 1
    else:
        minimap.animstep = 4
    world.tonkspritelist.append(minimap)

    # start engine
    game = TonkEngine.Game(world, display)
    
    auto_forward = False
    auto_reverse = False
    auto_repeat_delay = 0
    speed = 0
    
    # Main game loop
    start_time = pygame.time.get_ticks()
    while game.state == 1:

        # move player tank
        xoffset = int(round(math.cos(red_tank.angle * math.pi / 180) * speed))
        yoffset = int(round(- math.sin(red_tank.angle * math.pi / 180) * speed))
        red_tank.move(xoffset, yoffset)
        red_shadow.move_to(red_tank.x - 4, red_tank.y + 4, angle = red_tank.angle)

        # move grey tank and rotating logo
        xoffset = int(round(math.cos(grey_tank.angle * math.pi / 180) * 3))
        yoffset = int(round(- math.sin(grey_tank.angle * math.pi / 180) * 3))
        grey_tank.move(xoffset, yoffset, angle = grey_tank.angle + 2)
        grey_shadow.move_to(grey_tank.x - 4, grey_tank.y + 4, angle = grey_tank.angle)
        logo.move(0, 0, angle = logo.angle - 1)

        # move the camera
        (camera_x, camera_y) = red_tank.rect.center
        display.move_camera_to(camera_x, camera_y)

        display.update_sprites(world)

        # draw tank positions on minimap
        if minimap.animstep > 1:
            scale = world.worldwidth / scaleslist[minimap.animstep]
            grey_tank_pos = (int(grey_tank.x / scale), int(grey_tank.y / scale))
            red_tank_pos = (int(red_tank.x / scale), int(red_tank.y / scale))
            pygame.draw.circle(minimap.image, Color('grey'), grey_tank_pos, 3, 0)
            pygame.draw.circle(minimap.image, Color('red'), red_tank_pos, 3, 0)

        # game cycle - the screen gets rendered in here
        (events, keystate, mouse_x, mouse_y) = game.update()

        # handle player input
        speed = 0
        if keystate[K_UP] or auto_forward:
            if keystate[K_RCTRL] or keystate[K_LCTRL]:
                speed = 6
            else:
                speed = 4
        if keystate[K_DOWN] or auto_reverse:
            if keystate[K_RCTRL] or keystate[K_LCTRL]:
                speed = -6
            else:
                speed = -4
        if keystate[K_LEFT]:
            red_tank.angle += 2
        if keystate[K_RIGHT]:
            red_tank.angle -= 2

        # fold map (zoom out)
        if keystate[K_PAGEUP]:
            if auto_repeat_delay <= 0:
                if minimap.animstep > 0:
                    minimap.animstep -= 1
                    if minimap.animstep == 0:
                        minimap.visible = False
                minimap.moved = True
                auto_repeat_delay = 10

        # unfold map (zoom in)    
        if keystate[K_PAGEDOWN]:
            if auto_repeat_delay <= 0:
                minimap.visible = True
                if minimap.animstep < len(minimap.images) -1:
                    minimap.animstep += 1
                minimap.moved = True
                auto_repeat_delay = 10

        if keystate[K_SPACE]:
            print red_tank.x, red_tank.y
            
        # auto-forward and auto-reverse
        if keystate[K_DOWN] or keystate[K_UP]:
            if auto_repeat_delay <= 0:
                auto_forward = False
                auto_reverse = False
        if keystate[K_UP] and (keystate[K_LSHIFT] or keystate[K_RSHIFT]):
            auto_forward = True
            auto_repeat_delay = 15
        if keystate[K_DOWN] and (keystate[K_LSHIFT] or keystate[K_RSHIFT]):
            auto_reverse = True
            auto_repeat_delay = 15

        if auto_repeat_delay > 0:
            auto_repeat_delay -= 1


    end_time = pygame.time.get_ticks()
    playing_time_in_seconds = (end_time - start_time)/1000
    fps = game.framecounter / playing_time_in_seconds
    print 'Average frames per second:', fps
    
#####################################################################
#call the "main" function if running this script
if __name__ == '__main__': main()

