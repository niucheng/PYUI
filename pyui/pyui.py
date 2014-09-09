#!/usr/bin/env python
# coding: utf-8

import config
import constants

if config.host == constants.LINUX:
    pass
else:
    pass

if config.ui == constants.GUI and True:
    import gui
    puts = gui.puts
    info = gui.info
    warn = gui.warn
    error = gui.error
    success = gui.success
    gets = gui.gets
    get_int = gui.get_int
else:
    import cli
    puts = cli.puts
    info = cli.info
    warn = cli.warn
    error = cli.error
    success = cli.success
    gets = cli.gets
    get_int = cli.get_int

