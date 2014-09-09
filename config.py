#!/usr/bin/env python
# coding: utf-8

'''Generate ./pyui/config.py'''

import os

dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir, 'pyui', 'config.py')

if __name__ == "__main__":
    str = '''\
#!/usr/bin/env python
# coding: utf-8

"""This python script file is generated automatically by ../config.py

Please do not modify this file manually, or it will be overwritten."""

import sys

import constants

host = sys.platform
ver = sys.version_info.major
ui = constants.%s

''' % 'CLI'

    f = open(file, 'w')
    f.write(str)
    f.close()

    print ('Done generate config script file: %s' % file)

