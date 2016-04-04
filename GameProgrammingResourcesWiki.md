## Python ##
  * [Python](http://www.python.org/) programming language by Guido van Rossum

  * Documentation:
    * [Python documentation](http://www.python.org/doc/)

  * Tutorials:
    * [Official Python tutorial](http://docs.python.org/tutorial/)
    * [Dive into Python](http://www.diveintopython.net/) by Mark Pilgrim
    * [How to Think Like a Computer Scientist](http://www.greenteapress.com/thinkpython/thinkpython.html) by Allen B. Downey

  * [List of Python game programming tools](http://wiki.python.org/moin/GameProgramming)

  * [Python on the Game Programming Wiki](http://gpwiki.org/index.php/Python)

## Pygame ##
  * [Pygame](http://www.pygame.org/) by Pete Shinners (Pygame is based on Sam Lantinga's [SDL](http://www.libsdl.org/) - Simple DirectMedia Layer)

  * Documentation:
    * [Pygame documentation](http://www.pygame.org/docs/)

  * Tutorials:
    * [Pygame tutorials](http://www.pygame.org/wiki/tutorials)
    * [Pygame cookbook](http://www.pygame.org/wiki/CookBook)
    * [Python Game Programming](http://rene.f0o.com/mywiki/PythonGameProgramming) by Rene Dudfield & Geoff Howland
    * [Invent your own computer games with Python](http://inventwithpython.com/) by Albert Sweigart
    * [Game Programming - L Line](http://www.cs.iupui.edu/~aharris/pygame/) by Andy Harris, book and video online course

  * [List of Pygame Libraries](http://www.pygame.org/tags/libraries)

## Networking ##
  * Documentation:
    * [Socket](http://docs.python.org/library/socket.html) Low-level networking interface
    * [SocketServer](http://docs.python.org/library/socketserver.html) framework for network servers

  * Protocols:
    * [UDP](http://en.wikipedia.org/wiki/User_Datagram_Protocol): User Datagram Protocol ([socket.SOCK\_DGRAM](http://wiki.python.org/moin/UdpCommunication))
      * [ICE-UDP](http://xmpp.org/extensions/xep-0176.html): Interactive Connectivity Establishment UDP Transport Method by Yunhong Gu
        * The PySoy 3D engine uses ICE-UDP
      * [UDT](http://udt.sourceforge.net/index.html): UDP-based Data Transfer
      * [Notify](http://opentnl.sourceforge.net/doxydocs/structTNL_1_1NetConnection_1_1PacketNotify.html): Torque Network Library protocol
        * implementations (C++): [OpenTNL](http://opentnl.sourceforge.net/doxydocs/fundamentals.html) & [TNL2](http://github.com/nardo/tnl2)
      * [enet](http://enet.bespin.org/): another network gaming protocol on top of UDP (C++)
    * [AMP](http://twistedmatrix.com/documents/8.1.0/api/twisted.protocols.amp.html): Asynchronous Messaging Protocol
      * [AMP chat example code](http://www.ripton.net/blog/?p=16) by David Ripton
      * [AMP game example code](https://launchpad.net/game) by Christopher Armstrong & Jp Calderone
    * [TCP](http://en.wikipedia.org/wiki/Transmission_Control_Protocol):  Transmission Control Protocol ([socket.SOCK\_STREAM](http://wiki.python.org/moin/TcpCommunication)) In general, TCP is not advised for real-time action games. It is fine for turn-based games or for games where you don't have to aim for the opponent (such as WoW where you select a character/object and then click on the action/spell you want to use on it.)
      * [HTTP](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is usually implemented on top of TCP and is important for web browser games

  * Tutorials:
    * [Sockets in Python](http://www.devshed.com/c/a/Python/Sockets-in-Python-Into-the-World-of-Python-Network-Programming/) (UDP & TCP) by A.P.Rajshekhar
    * [Python network programming](http://ilab.cs.byu.edu/python/)  (UDP & TCP) by Daniel Zappala
    * [Networking for game programmers](http://gafferongames.com/networking-for-game-programmers/) by Glenn Fiedler: this tutorial uses C++ for its examples, but it gives a good explanation on how to build a protocol on top of UDP [here](http://www.gaffer.org/networking-for-game-programmers/virtual-connection-over-udp) & [here](http://www.gaffer.org/networking-for-game-programmers/reliability-and-flow-control)
      * [tutorial C++ code](http://code.google.com/p/netgame/)
    * [Network game programming](http://www.flipcode.com/archives/Network_Game_Programming-Issue_01_Things_that_make_you_go_hmm.shtml) by Dan Royer: this is an old (1999) tutorial using C++ & TCP; UDP is briefly mentioned as a novelty. [Here](http://www.gamedev.net/community/forums/topic.asp?topic_id=509977)'s a follow-up discussion
    * [Write your own MMORPG in four hours using Python](http://www.enchantedage.com/pymmo) (TCP) by Jon Watte

  * Libraries:
    * [RakNet](http://www.jenkinssoftware.com/raknet/index.html) uses UDT and supports features such as [NAT Punchthrough](http://www.jenkinssoftware.com/raknet/manual/natpunchthrough.html)
      * [PyRakNet](http://www.pygame.org/project-pyraknet-260-632.html) Python bindings for RakNet by Gerald Kaszuba
    * [Twisted framework](http://twistedmatrix.com/trac/) (UDP, AMP, TCP...)
      * [Untwisting Python network programming](http://onlamp.com/pub/a/python/2006/08/10/untwisting-python-network-programming.html) by Kendrew Lau
      * [Network programming with the Twisted framework](http://www.ibm.com/developerworks/linux/library/l-twist1.html) by David Mertz
      * [Grokking Twisted](http://www.artima.com/weblogs/viewpost.jsp?thread=156396) by Bruce Eckel
    * [Mastermind networking lib](http://www.pygame.org/project-Mastermind+Networking+Lib-859-.html) (UDP & TCP) by Ian Mallett
      * [Spacewar Multi](http://www.pygame.org/project-Spacewar+Multi-1025-.html) example game using TCP
    * [Astral Networking](http://www.pygame.org/project-Astral+Networking-1605-2838.html) by Patrick Mullen on top of TCP.
    * [PygLibs.net](http://www.pygame.org/project-PygLibs.net-835-.html) by RoeBros
    * [Podsixnet game networking library](http://code.google.com/p/podsixnet/) (TCP) by Chris McCormick
    * [Eventlet](http://wiki.secondlife.com/w/index.php?title=Eventlet&oldid=51543) is a HTTP networking library written in Python by Bob Ippolito, used in Second Life

  * [List of network resources](http://gafferongames.com/2009/01/25/game-networking-resources/) by Glenn Fiedler
  * [List of network resources](http://www.pygame.org/tags/network) on PyGame


## Browser Games ##
  * A [list](http://www.pbbg.org/links.asp) of Persistent Browser Based Games (PBBGs) and tutorials
  * On the server side, one of these [web frameworks](http://wiki.python.org/moin/WebFrameworks) could be used, for example [Django](http://www.djangoproject.com/)
  * For the client side, [pyjamas](http://code.google.com/p/pyjamas/) could be used to generate [JavaScript](http://en.wikipedia.org/wiki/JavaScript) which runs in the browser

## Physics ##
  * Tutorial:
    * [Game physics tutorial](http://gafferongames.com/game-physics/) by Glenn Fiedler is a good introduction (examples in C++) to the concepts and algorithms of game physics

  * Libraries:
    * [Box2D](http://www.box2d.org/)
      * [Pybox2D](http://www.pygame.org/project-pyBox2D-723-.html) Python bindings for Box2D by Ken Lauer
    * [ODE 3D](http://www.ode.org/) Open Dynamics Engine
      * [Pyode](http://pyode.sourceforge.net/) Python bindings for ODE 3D
    * [Bullet 3D](http://bulletphysics.org/wordpress/) by Erwin Coumans, ([code](http://code.google.com/p/bullet/))
      * Blender 3D provides a [Python API](http://wiki.blender.org/index.php/Doc:Manual/Game_Engine/Python_API/Bullet_physics) for Bullet 3D

  * [PAL: Physics Abstraction Layer](http://www.adrianboeing.com/pal/index.html) by Adrian Boeing

## Graphics ##
  * Documentation:
    * [OpenGL documentation](http://www.opengl.org/documentation/)
    * [PyOpenGL documentation](http://pyopengl.sourceforge.net/documentation/)

  * Tutorials:
    * [NeHe OpenGL tutorial](http://nehe.gamedev.net/)
      * [NeHe Python code](http://www.pygame.org/gamelets/games/nehe1-10.zip)
    * [Anomalistic Technologies OpenGL Tutorial](http://anomtech.uuuq.com/Index.php?page=Tutorials)

  * Libraries:
    * [PyOpenGL](http://pyopengl.sourceforge.net/)
      * You may want to use [NumPy](http://numpy.scipy.org/) for [matrix transformations](http://www.ruthless.zathras.de/facts/apps/polygonesia/3d-transformation-matrix.php)
    * [Pyglet multimedia library](http://pyglet.org/), the funtionality of Pyglet largely overlaps with Pygame's funtionality, but Pyglet is written in pure Python and does not rely on the SDL as Pygame does.
      * [Pyglet game programming tutorial](http://www.learningpython.com/2007/11/10/creating-a-game-with-pyglet-and-python/)
    * [PGU](http://code.google.com/p/pgu/) Phil's pyGame Utilities by Phil Hassey & Peter Rogers
    * [PyGL2D](http://code.google.com/p/pygl2d/) by PyMike
    * [glLib Reloaded](http://www.pygame.org/project-glLib+Reloaded-1326-.html) by Ian Mallett

  * 2D engines:
    * [Rabbyt fast sprite engine](http://matthewmarshall.org/projects/rabbyt/) by Matthew Marshall
    * [Kyra](http://www.grinninglizard.com/kyra/) sprite engine, based on the SDL
      * [Pykyra](http://www.alobbs.com/pykyra) Python bindings for Kyra by Alvaro Lopez Ortega
    * [Flamingo](http://code.google.com/p/flamingoengine/) and [Opossum](http://pygame.org/project-Opossum+Engine-1340-.html) 2D game engines by Bradley Zeis
    * Tonk Engine

  * 2.5D isometric engines:
    * [FIFE](http://www.fifengine.de/) Flexible Isometric Free Engine
    * [Isomyr](http://www.pygame.org/project-Isomyr-1316-.html) by Duncan McGreggor
    * [PyTile](http://www.pygame.org/project-pyTile-871-.html) by Timothy Baldock
    * [Shmup & Build](http://www.pygame.org/project-Shmup+%26+Build-1667-2904.html) by Bander

  * 3D engines:
    * [Ogre](http://www.ogre3d.org/) Object-Oriented Graphics Rendering Engine
      * [PyOgre](http://www.ogre3d.org/wiki/index.php/PyOgre) Python bindings for Ogre
    * [Crystal Space 3D](http://www.crystalspace3d.org/main/Main_Page) can use both the ODE 3D and Bullet 3D physics engines
      * [PyCrystal](http://www.crystalspace3d.org/main/PyCrystal) Python bindings for Crystal Space 3D
    * [Irrlicht](http://irrlicht.sourceforge.net/) by Nikolaus Gebhardt
      * [Pyrr](https://opensvn.csie.org/traccgi/pyrr) Python bindings for Irrlicht (out of date & no longer maintained)
    * [Panda 3D](http://www.panda3d.org/) by Disney Imagineering & Carnegie-Mellon's Entertainment Technology Center
    * [Soya 3D](http://home.gna.org/oomadness/en/soya3d/index.html) by Jean-Baptiste Lamy & Bertrand Lamy
    * [PySoy 3D](http://www.pysoy.org/) is a fork of Soya 3D by Arc Riley
    * [PYGGEL](http://www.pygame.org/project-PYGGEL-968-.html) Python Graphical Game Engine + Libraries by RoeBros
    * [Game Blender](http://en.wikipedia.org/wiki/Game_Blender), the engine of Blender 3D

  * 3D content creation:
    * [Blender 3D](http://www.blender.org/) content creation suite
      * [Blender 3D Python scripting](http://wiki.blender.org/index.php/Doc:Manual/Extensions/Python)
      * [Blender 3D Python tutorials](http://wiki.blender.org/index.php/Extensions:Py/Scripts)
      * [Death to usability, or learn Blender in 20 minutes nonetheless](http://www.ruthless.zathras.de/facts/apps/polygonesia/blender.php)
      * Free books on the Blender game engine: [here](http://download.blender.org/documentation/gamekit1/) & [here](http://download.blender.org/documentation/gamekit2/)

  * [List of Python 3D Software](http://www.vrplumber.com/py3d.py)
  * [List of game engines](http://www.moddb.com/engines/) at Mod DB
  * [List of game engines](http://gpwiki.org/index.php/Game_Engines) at Game Programming Wiki

## Graphical User Interface ##
  * Libraries:
    * [Python's standard TkInter GUI](http://wiki.python.org/moin/TkInter)
      * [Tutorial: Making a CD Player with pygame and Tkinter in Python](http://www.informit.com/articles/article.aspx?p=27103&redir=1) by Harvey Deitel & Paul Deitel
    * [Albow](http://www.pygame.org/project-Albow-338-853.html) widgetry for PyGame & PyOpenGL by Gregory Ewing
    * [Simple Game GUI](http://www.pygame.org/project-simple+game+gui-740-.html) by Canio Massimo Tristano
    * [Roebros' GUI](http://www.pygame.org/project-RoeBros%27+GUI-656-.html)
    * [pqGUI](http://www.pygame.org/project-pqGUI-1026-.html) by Poiuy Qwert

  * [List of Python GUI tools](http://wiki.python.org/moin/GuiProgramming)
  * [List of Pygame GUI tools](http://www.pygame.org/tags/gui)

## Artificial Intelligence ##
  * Tutorials:
    * [A\* Pathfinding for Beginners](http://www.policyalmanac.org/games/aStarTutorial.htm) by Patrick Lester
    * [Pathfinding in Blender 3D](http://www.pxleyes.com/ext-tutorial/blender/10926/Game-Engine-AI-Part-1--Simple-Path.html) by Giulia

  * Libraries:
    * [Theseus](http://www.pygame.org/project-Theseus+V1.0-1426-2533.html) by Heiko Nolte
    * [Hex Stuff](http://www.pygame.org/project-Hex+stuff-773-.html) by Francesco Mastellone
    * [AStar](http://www.pygame.org/project-AStar-195-.html) by John Eriksson

  * [List of AI resources](http://www.pygame.org/tags/ai) at Pygame

## Concurrency ##

  * Documentation:
    * [threading](http://docs.python.org/library/threading.html) Higher-level threading interface

  * Tutorials:
    * [Basic Threading in Python](http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/) by Peyton McCullough
    * [A Curious Course on Coroutines and Concurrency](http://www.dabeaz.com/coroutines/) by David Beazley

  * [Stackless Python](http://www.stackless.com/), by Christian Tismer, **replaces** the Python executable (usually [CPython](http://en.wikipedia.org/wiki/CPython)). Stackless implements microthreads ("green threads"), co-routines, channels and serialization.
    * Stackless is being used by the [EVE Online](http://www.eveonline.com/) servers, presentations: [2006](http://www.slideshare.net/Arbow/stackless-python-in-eve), [2009](http://us.pycon.org/2009/conference/schedule/event/91/)
  * [Greenlet](http://pypi.python.org/pypi/greenlet) is a spin-off of Stackless, a version of CPython that supports micro-threads called "tasklets"
    * Greenlet is being used by the Second Life servers
  * [PyPy](http://pypy.org/) is a CPython replacement, written in Python. It implements a [JIT](http://en.wikipedia.org/wiki/Just-in-time_compilation) compiler and also the features of Stackless.

  * [Python-CSP](http://code.google.com/p/python-csp/) implements [Communicating Sequential Processes](http://en.wikipedia.org/wiki/Communicating_sequential_processes) on top of Python

## Compatibility ##
  * [SWIG](http://www.swig.org/) (Simplified Wrapper and Interface Generator) is used to connect programs or libraries written in C/C++ with scripting languages such as Python.
  * [Pyrex](http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/) lets you write code that mixes Python and C data types, and compiles it into a C extension for Python
  * [Cython](http://cython.org/) is a derivative of Pyrex
  * [PyInline](http://pyinline.sourceforge.net/) allows you to put source code from other programming languages directly "inline" in Python
  * [Jython](http://www.jython.org/) is an implementation of Python for the Java Virtual Machine
  * [IronPython](http://ironpython.net/) is an implementation of Python targeting the .NET Framework & Mono, by Jim Hugunin
  * [PyPlugin](http://code.google.com/p/pyplugin/) is a simple plugin framework for Python

## Distribution ##
  * [Distutils](http://docs.python.org/distutils/)
    * [py2exe](http://www.py2exe.org/) is a Distutils  extension which converts Python scripts into executable Windows programs
      * An excellent [tutorial (PDF) on building windows installers for Python games](http://www.cs.iupui.edu/~aharris/pygame/Appendix_C.pdf) by Andy Harris using py2exe, [Nullsoft NSIS](http://nsis.sourceforge.net/Main_Page) & [HM NIS Edit](http://hmne.sourceforge.net/) - this how I built the Windows installer for [Arcade Tonk Tanks](http://code.google.com/p/arcade-tonk-tanks/) 0.0.5
  * [PyInstaller](http://www.pyinstaller.org/) converts (packages) Python programs into stand-alone executables, under Windows, Linux, and Mac OS X.
  * [Python Package Index](http://pypi.python.org/pypi)

## Game developement portals ##
  * [GameDev.net](http://www.gamedev.net/)
  * [Gamasutra.com](http://www.gamasutra.com/)
  * [DevMaster.net](http://www.devmaster.net/)
  * [AiGameDev.com](http://aigamedev.com/)
  * [ModDB.com](http://www.moddb.com/)
  * [Game Programming Wiki](http://gpwiki.org/)