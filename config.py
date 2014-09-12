#!/usr/bin/env python
# coding: utf-8

"""Generate ./pyui/config.py"""

import os

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'pyui', 'config.py')

if __name__ == "__main__":
    s = '''\
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
ui = constants.%s
''' % 'CLI'

    f = open(filename, 'w')
    f.write(s)
    f.close()

    print ('Done generate config script file: %s' % filename)

