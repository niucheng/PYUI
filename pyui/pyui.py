#!/usr/bin/env python
# coding: utf-8

import cli
import config
import constants
import gui

if config.host == constants.LINUX:
    pass
else:
    pass

if config.ui == constants.GUI and True:
    info = gui.info
else:
    info = cli.info

if __name__ == "__main__":
    info('Hello world!')
    gui.info('Hello world!')
    cli.info('Hello world!')

