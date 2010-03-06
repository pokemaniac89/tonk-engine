#!/usr/bin/env python
#
# TonkEngineDemo, Koen Lefever 2010, GPL v.3 licensed
#
#
#####################################################################

import pygame
from pygame.locals import *         # http://www.pygame.org/
import TonkEngine                   # http://code.google.com/tonk-engine/
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
    tileset = TonkEngine.TileSet([TonkEngine.Tile(['b00.PNG'], 0, [0], False, 'water / out of map'),
                                  TonkEngine.Tile(['water3-0.bmp','water3-1.bmp','water3-2.bmp','water3-3.bmp','water3-4.bmp','water3-5.bmp'], 0, [0], True, 'Flowing water'),
                                  TonkEngine.Tile(['grass.bmp'], 0, [0], False, 'grass'),
                                  TonkEngine.Tile(['rock1.bmp'], 270, [0], False, 'rock'),
                                  TonkEngine.Tile(['border4.bmp'], 0, [0], False, 'waterside'),
                                  TonkEngine.Tile(['a00.PNG'], 0, [0], False),      # The River scenery
                                  TonkEngine.Tile(['a01.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a02.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a03.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a04.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a05.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a06.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a07.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a10.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a11.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a12.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a13.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a14.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a15.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a16.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a17.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a20.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a21.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a22.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a23.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a24.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a25.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a26.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a27.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a30.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a31.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a32.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a33.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a34.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a35.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a36.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a37.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a40.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a41.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a42.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a43.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a44.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a45.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a46.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a47.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a50.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a51.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a52.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a53.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a54.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a55.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a56.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a57.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a60.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a61.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a62.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a63.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a64.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a65.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a66.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a67.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a70.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a71.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a72.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a73.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a74.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a75.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a76.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['a77.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['tile0.png'], 0, [0], False, 'empty tile'),
                                  TonkEngine.Tile(['grass-beach.png'], 0, [0], False,),
                                  TonkEngine.Tile(['grass-beach.png'], 90, [0], False,),
                                  TonkEngine.Tile(['grass-beach.png'], 180, [0], False,),
                                  TonkEngine.Tile(['grass-beach.png'], 270, [0], False,),
                                  TonkEngine.Tile(['tile0.png'], 0, [0], False, 'empty tile'),
                                  TonkEngine.Tile(['b00.PNG'], 0, [0], False),      # The Beach scenery
                                  TonkEngine.Tile(['b01.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b02.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b03.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b04.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b05.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b06.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b07.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b10.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b11.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b12.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b13.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b14.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b15.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b16.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b17.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b20.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b21.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b22.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b23.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b24.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b25.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b26.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b27.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b30.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b31.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b32.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b33.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b34.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b35.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b36.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b37.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b40.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b41.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b42.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b43.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b44.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b45.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b46.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b47.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b50.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b51.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b52.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b53.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b54.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b55.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b56.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b57.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b60.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b61.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b62.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b63.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b64.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b65.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b66.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b67.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b70.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b71.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b72.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b73.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b74.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b75.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b76.PNG'], 0, [0], False),
                                  TonkEngine.Tile(['b77.PNG'], 0, [0], False)])

    # create map of the world
    tilemap = TonkEngine.TileMap(nr_of_rows = 50, nr_of_columns = 50, tilenr = 2, description = 'Demo map')
    tilemap.set_border(depth = 3, tilenr = 75)    # the map is an island surrounded by water
    tilemap.fill_rect(x = 3, y = 3, xmax = 47, ymax = 10, tilenr = 129)     # beaches around
    tilemap.fill_rect(x = 3, y = 3, xmax = 10, ymax = 47, tilenr = 129)     # the island
    tilemap.fill_rect(x = 40, y = 3, xmax = 47, ymax = 47, tilenr = 129)
    tilemap.fill_rect(x = 3, y = 40, xmax = 47, ymax = 47, tilenr = 129)
    tilemap.fill_rect(x = 11, y = 10, xmax = 40, ymax = 11, tilenr = 71)    # border
    tilemap.fill_rect(x = 10, y = 11, xmax = 11, ymax = 40, tilenr = 72)    # between
    tilemap.fill_rect(x = 39, y = 10, xmax = 40, ymax = 40, tilenr = 70)    # grass &
    tilemap.fill_rect(x = 10, y = 39, xmax = 40, ymax = 40, tilenr = 73)    # beach
    tilemap.set_tile(x = 10, y = 39, tilenr = 129)
    tilemap.set_tile(x = 39, y = 39, tilenr = 129)
    tilemap.set_tile(x = 39, y = 10, tilenr = 129)
    tilemap.set_tile(x = 21, y = 2, tilenr = 1)                             # flowing river
    tilemap.set_tile(x = 22, y = 2, tilenr = 1)
    tilemap.set_tile(x = 23, y = 2, tilenr = 1)
    tilemap.set_tile(x = 24, y = 2, tilenr = 1)
    tilemap.set_tile(x = 25, y = 2, tilenr = 1)
    tilemap.set_tile(x = 26, y = 2, tilenr = 1)
    tilemap.set_tile(x = 22, y = 3, tilenr = 1)
    tilemap.set_tile(x = 23, y = 3, tilenr = 1)
    tilemap.set_tile(x = 24, y = 3, tilenr = 1)
    tilemap.set_tile(x = 25, y = 3, tilenr = 1)
    tilemap.set_tile(x = 23, y = 4, tilenr = 1)
    tilemap.set_tile(x = 24, y = 4, tilenr = 1)
    tilemap.set_tile(x = 24, y = 5, tilenr = 1)
    tilemap.set_tile(x = 24, y = 6, tilenr = 1)
    tilemap.set_tile(x = 23, y = 7, tilenr = 1)
    tilemap.set_tile(x = 24, y = 7, tilenr = 1)
    tilemap.set_tile(x = 23, y = 8, tilenr = 1)
    tilemap.set_tile(x = 22, y = 9, tilenr = 1)
    tilemap.set_tile(x = 23, y = 9, tilenr = 1)
    tilemap.set_tile(x = 21, y = 10, tilenr = 1)
    tilemap.set_tile(x = 22, y = 10, tilenr = 1)
    tilemap.set_tile(x = 21, y = 11, tilenr = 1)
    tilemap.set_tile(x = 21, y = 12, tilenr = 1)
    tilemap.set_tile(x = 21, y = 13, tilenr = 1)
    tilemap.set_tile(x = 12, y = 20, tilenr = 1)
    tilemap.set_tile(x = 12, y = 21, tilenr = 1)
    tilemap.set_tile(x = 13, y = 21, tilenr = 1)
    tilemap.set_tile(x = 13, y = 22, tilenr = 1)
    tilemap.set_tile(x = 13, y = 23, tilenr = 1)
    tilemap.set_tile(x = 14, y = 23, tilenr = 1)
    tilemap.set_tile(x = 14, y = 24, tilenr = 1)
    tilemap.set_tile(x = 15, y = 24, tilenr = 1)
    tilemap.set_tile(x = 16, y = 24, tilenr = 1)
    tilemap.set_tile(x = 16, y = 25, tilenr = 1)
    tilemap.set_tile(x = 16, y = 26, tilenr = 1)
    for c in range(0,8):
        for r in range(0,8):
            tilemap.set_tile(x = c + 3, y = r + 3, tilenr = 75 + c + r*8)       # The Beach scenery
            tilemap.set_tile(x = c + 13, y = r + 13, tilenr = 5 + c + r*8)      # The River scenery
            tilemap.set_tile(x = c + 24, y = r + 24, tilenr = 3)                # square of rocks
    
    # Create game world
    world = TonkEngine.World(tileset = tileset, tilemap = tilemap)

    # create sprites
    red_tank = TonkEngine.Sprite(x = 1760, y = 1680,z = 2, angle =0, filelist = ['red_tank.png'], absolute = False)
    red_shadow = TonkEngine.Sprite(x = 1757, y = 1683,z = 2, angle =0, filelist = ['tank_shadow1.png'], absolute = False)
    grey_tank = TonkEngine.Sprite(x = 1435, y = 1610, z = 4, filelist = ['grey_tank.png'], absolute = False)
    grey_shadow = TonkEngine.Sprite(x = 1432, y = 1613, z = 4, filelist = ['tank_shadow.png'], absolute = False)
    explosion = TonkEngine.Sprite(x = 1400, y = 1600, z=5, absolute = False,
                           filelist = ['boom-1-0001.png', 'boom-1-0002.png', 'boom-1-0003.png', 'boom-1-0004.png', 'boom-1-0005.png',
                                       'boom-1-0006.png', 'boom-1-0007.png', 'boom-1-0008.png', 'boom-1-0009.png', 'boom-1-0010.png',
                                       'boom-1-0011.png', 'boom-1-0012.png', 'boom-1-0013.png', 'boom-1-0014.png', 'boom-1-0015.png',
                                       'boom-1-0016.png', 'boom-1-0017.png', 'boom-1-0018.png', 'boom-1-0019.png', 'boom-1-0020.png',
                                       'boom-1-0027.png', 'boom-1-0030.png', 'boom-1-0033.png', 'boom-1-0036.png', 'boom-1-0039.png',
                                       'boom-1-0042.png', 'boom-1-0045.png', 'boom-1-0048.png', 'boom-1-0051.png', 'boom-1-0054.png',
                                       'boom-1-0057.png', 'boom-1-0060.png', 'boom-1-0063.png', 'boom-1-0066.png', 'boom-1-0069.png',
                                       'boom-1-0072.png', 'boom-1-0075.png', 'boom-1-0078.png', 'boom-1-0081.png', 'boom-1-0084.png',
                                       'boom-1-0087.png', 'boom-1-0090.png', 'boom-1-0093.png', 'boom-1-0096.png', 'boom-1-0099.png'])
    logo = TonkEngine.Sprite(x = 2000, y = 1250, z = 0, filelist = ['tonk_engine.png'], angle = 20, absolute = False)
    world.tonkspritelist += [logo, grey_shadow, grey_tank, red_shadow, red_tank, explosion]
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
        scaled_map = TonkEngine.ScaledMap(world, width = minimap_size, height = minimap_size, smooth = True, floating_point = True)
        imageslist.append(scaled_map.image)
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
                speed = 5
            else:
                speed = 3
        if keystate[K_DOWN] or auto_reverse:
            if keystate[K_RCTRL] or keystate[K_LCTRL]:
                speed = -5
            else:
                speed = -3
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
