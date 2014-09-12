#!/usr/bin/env python
# coding: utf-8

import os
import sys

python2 = sys.version_info.major < 3

if python2:
    import color
    import puts2 as out
else:
    from pyui import color
    from pyui import puts3 as out

if python2:
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

def puts(s, end='\n'):
    out.puts(str(s) % ansi_color, end)

def info(s, title=''):
    puts('[%s%s%s]%s' % ('%s(%s)s' % ('%', color.ANSI_COLOR_INFO),
                         color.ANSI_COLOR_INFO,
                         '%s(%s)s' % ('%', color.ANSI_COLOR_NORMAL),
                         ' %s' % s if str(s) else ''))

def warn(s, title=''):
    puts('[%s%s%s]%s' % ('%s(%s)s' % ('%', color.ANSI_COLOR_WARN),
                         color.ANSI_COLOR_WARN,
                         '%s(%s)s' % ('%', color.ANSI_COLOR_NORMAL),
                         ' %s' % s if str(s) else ''))

def error(s, title=''):
    puts('[%s%s%s]%s' % ('%s(%s)s' % ('%', color.ANSI_COLOR_ERROR),
                         color.ANSI_COLOR_FAIL,
                         '%s(%s)s' % ('%', color.ANSI_COLOR_NORMAL),
                         ' %s' % s if str(s) else ''))

def success(s, title=''):
    puts('[%s%s%s]%s' % ('%s(%s)s' % ('%', color.ANSI_COLOR_SUCCESS),
                         color.ANSI_COLOR_OK,
                         '%s(%s)s' % ('%', color.ANSI_COLOR_NORMAL),
                         ' %s' % s if str(s) else ''))

def _get(prompt, default='', ret_type='', title=''):
    return input ('%s [%s%s] ' % (prompt,
                                  ret_type,
                                  ': %s' % default if str(default) else ''))

def gets(prompt, default='', ret_type='String', title=''):
    ret =  _get(prompt, default, ret_type, title)
    return ret if str(ret) else default

def get_int(prompt, default=0, ret_type='Number', title=''):
    ret = _get(prompt, str(default), ret_type, title)
    return ret if str(ret) else default

