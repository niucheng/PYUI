#!/usr/bin/env python
# coding: utf-8

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pyui import pyui

if __name__ == "__main__":
    pyui.puts('')
    pyui.puts('Have a lot of fun!')
    pyui.puts('Have a lot of fun!', 'Hello world!')
    pyui.info('')
    pyui.info('Have a lot of fun!')
    pyui.info('Have a lot of fun!', 'Hello world!')
    pyui.warn('')
    pyui.warn('Have a lot of fun!')
    pyui.warn('Have a lot of fun!', 'Hello world!')
    pyui.error('')
    pyui.error('Have a lot of fun!')
    pyui.error('Have a lot of fun!', 'Hello world!')
    pyui.success('')
    pyui.success('Have a lot of fun!')
    pyui.success('Have a lot of fun!', 'Hello world!')
    #
    pyui.info(pyui.gets(''))
    pyui.info(pyui.gets('IP'))
    pyui.info(pyui.gets('', ''))
    pyui.info(pyui.gets('IP', 'localhost'))
    pyui.info(pyui.gets('', '', ''))
    pyui.info(pyui.gets('IP', 'localhost', 'STRING'))
    pyui.info(pyui.gets('', '', '', ''))
    pyui.info(pyui.gets('IP', 'localhost', 'STRING', '?'))
    pyui.info(pyui.get_int(''))
    pyui.info(pyui.get_int('Port'))
    pyui.info(pyui.get_int('', ''))
    pyui.info(pyui.get_int('Port', 23))
    pyui.info(pyui.get_int('', '', ''))
    pyui.info(pyui.get_int('Port', 23, 'INT'))
    pyui.info(pyui.get_int('', '', '', ''))
    pyui.info(pyui.get_int('Port', 23, 'INT', '!'))

