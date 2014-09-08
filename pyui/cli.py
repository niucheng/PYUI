#!/usr/bin/env python
# coding: utf-8

import color

def puts(str, end='\n'):
    if end == '\n':
        print str % color.ANSI_COLOR_SET
    else:
        print str % color.ANSI_COLOR_SET,

def info(str, title=''):
    puts('[%sINFO%s] %s' % ('%(INFO)s', '%(NORMAL)s', str))

if __name__ == "__main__":
    puts('Hello world!')
    info('Hello workd!')

