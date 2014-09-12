#!/usr/bin/env python
# coding: utf-8

"""This python script file is generated automatically by ../config.py

Please do not modify this file manually, or it will be overwritten."""

import sys

if sys.version_info.major < 3:
    import constants
else:
    from pyui import constants

host = sys.platform
ver = sys.version_info.major
ui = constants.CLI
