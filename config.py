#!/usr/bin/env python
# coding: utf-8

'''Generate ./pyui/config.py'''

import os

dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir, 'pyui', 'config.py')

if __name__ == "__main__":
    f = open('./pyui/config.py', 'w')
    f.write('#!/usr/bin/env python\n')
    f.write('# coding: utf-8\n')
    f.write('\n')
    f.write('"""This python script is generated automatically by ../config.py\n')
    f.write('\n')
    f.write('You should not modify this file manually, please."""\n')
    f.write('\n')
    f.write('import constants\n')
    f.write('\n')
    f.write('host = constants.LINUX\n')
    f.write('ui = constants.CLI\n')
    f.write('\n')
    f.close()

