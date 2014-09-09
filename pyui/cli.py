#!/usr/bin/env python
# coding: utf-8

import os

import color

input = raw_input

# Detect ANSI environment support
ansi_color = color.ANSI_COLOR_SET
#
if os.getenv('HOME'):  # HACK for linux
    pass
elif os.getenv('ANSICON'):
    pass
elif os.getenv('ConEmuANSI') == 'ON':
    # os.environ['COnEmuANSI'] == 'ON' will raise exception while no env-string
    pass
else:  # no ANSI support
    ansi_color = color.ANSI_NONE_COLOR_SET

def puts(str, end='\n'):
    if end == '\n':
        print str % ansi_color
    else:
        print str % ansi_color,

def info(str, title=''):
    puts('[%s%s%s]%s' % ('%s(%s)s' % ('%', color.ANSI_COLOR_INFO),
                          color.ANSI_COLOR_INFO,
                          '%s(%s)s' % ('%', color.ANSI_COLOR_NORMAL),
                          ' %s' % str if str else ''))

def warn(str, title=''):
    puts('[%s%s%s]%s' % ('%s(%s)s' % ('%', color.ANSI_COLOR_WARN),
                          color.ANSI_COLOR_WARN,
                          '%s(%s)s' % ('%', color.ANSI_COLOR_NORMAL),
                          ' %s' % str if str else ''))

def error(str, title=''):
    puts('[%s%s%s]%s' % ('%s(%s)s' % ('%', color.ANSI_COLOR_ERROR),
                          color.ANSI_COLOR_FAIL,
                          '%s(%s)s' % ('%', color.ANSI_COLOR_NORMAL),
                          ' %s' % str if str else ''))

def success(str, title=''):
    puts('[%s%s%s]%s' % ('%s(%s)s' % ('%', color.ANSI_COLOR_SUCCESS),
                          color.ANSI_COLOR_OK,
                          '%s(%s)s' % ('%', color.ANSI_COLOR_NORMAL),
                          ' %s' % str if str else ''))

def _get(prompt, default='', type='', title=''):
    return input ('%s [%s%s] ' % (prompt,
                                  type,
                                  ': %s' % default if default else ''))

def gets(prompt, default='', type='String', title=''):
    return _get(prompt, default, type, title)

def get_int(prompt, default=0, type='Number', title=''):
    return _get(prompt, str(default), type, title)

