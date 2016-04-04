**Tonk Engine** will be the game engine for [Arcade Tonk Tanks](http://code.google.com/p/arcade-tonk-tanks/) version 0.2.0. Since I'm currently working on Arcade Tonk Tanks 0.1.0 which does not use the Tonk Engine, development on this project is on hold for a while.

[![](http://www.python.org/community/logos/python-powered-w-200x80.png)](http://www.python.org/)       [![](http://www.pygame.org/docs/pygame_powered.gif)](http://www.pygame.org/project-Arcade+Tonk+Tanks-1078-2412.html)

I've decided to split the engine off from the game itself and to try to make it as generic as possible for a broad class of 2D games with a scrolling background. The code is still in a very early stage of development and not beyond the point of running a simple [demo program](http://code.google.com/p/tonk-engine/source/browse/trunk/TonkEngineDemo.py). Performance is low, use of this engine in a game is currently not advised.

## To Do: ##
  * implement network protocol on top of [UDP](http://en.wikipedia.org/wiki/User_Datagram_Protocol)
  * implement [A\* path finding](http://en.wikipedia.org/wiki/A*_search_algorithm) & other Artificial Intelligence components
  * implement a GUI for options screens, dialogs, &c.
  * port collision detection from Arcade Tonk Tanks
  * replace graphics back-end by OpenGL

If you are (thinking of) writing a game in Python yourself, you may want to have a look at the GameProgrammingResourcesWiki.

![http://tonk-engine.googlecode.com/files/TonkEngineDemo_000.png](http://tonk-engine.googlecode.com/files/TonkEngineDemo_000.png)

Last updated on 2010-10-03.