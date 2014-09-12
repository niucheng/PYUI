#!/usr/bin/env python
# coding: utf-8

import sys

python2 = sys.version_info.major < 3

if python2:
    import config
    import constants
else:
    from pyui import config
    from pyui import constants

if config.host == constants.LINUX:
    pass
else:
    pass

if config.ui == constants.GUI and True:
    if python2:
        import gui
    else:
        from pyui import gui
    puts = gui.puts
    info = gui.info
    warn = gui.warn
    error = gui.error
    success = gui.success
    gets = gui.gets
    get_int = gui.get_int
else:
    if python2:
        import cli
    else:
        from pyui import cli
    puts = cli.puts
    info = cli.info
    warn = cli.warn
    error = cli.error
    success = cli.success
    gets = cli.gets
    get_int = cli.get_int

