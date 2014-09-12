#!/usr/bin/env python
# coding: utf-8

import sys

python2 = sys.version_info.major < 3

if python2:
    import Tkinter as tk
    import tkMessageBox as tkmb
    #
    import color
    import constants
else:
    import tkinter as tk
    from tkinter import messagebox as tkmb
    #
    from pyui import color
    from pyui import constants

root = tk.Tk()
root.withdraw()

ret = None

def puts(s, title=constants.TITLE):
    tkmb.showinfo(title, str(s) % color.ANSI_NONE_COLOR_SET)

def info(s, title=color.ANSI_COLOR_INFO):
    tkmb.showinfo(title, str(s), parent=root)

def warn(s, title=color.ANSI_COLOR_WARN):
    tkmb.showwarning(title, str(s), parent=root)

def error(s, title=color.ANSI_COLOR_ERROR):
    tkmb.showerror(title, str(s), parent=root)

def success(s, title=color.ANSI_COLOR_SUCCESS):
    tkmb.showinfo(title, str(s), parent=root)

def _get(prompt, default='', ret_type='', title=constants.TITLE):
    r = tk.Tk()
    # Hide
    r.withdraw()
    def kill(event=None):
        global ret
        ret = e.get()
        r.destroy()
        r.quit()
    r.protocol('WM_DELETE_WINDOW', kill)
    r.resizable(0, 0)#(width=None, height=None)
    l = tk.Label(r, text=prompt, width=35, anchor='w')
    l.pack()
    e = tk.Entry(r, bd=5, width=35)
    e.bind('<Return>', kill)
    e.pack()
    b = tk.Button(r, text=constants.OK, width=35, command=kill)
    b.bind('<Return>', kill)
    b.pack()
    r.title(title)
    e.insert(tk.END, default)
    # Center
    r.update()
    r.deiconify()  # HACK
    w = r.winfo_screenwidth()
    h = r.winfo_screenheight()
    rsize = tuple(int(_) for _ in r.geometry().split('+')[0].split('x'))
    x = w/2 - rsize[0]/2
    y = h/2 - rsize[1]/2
    r.geometry('%dx%d+%d+%d' % (rsize + (x, y)))
    # Show
    r.deiconify()
    e.selection_range(0, tk.END)
    e.focus_set()
    r.mainloop()
    #
    return ret

def gets(prompt, default='', ret_type='String', title=constants.TITLE):
    return _get(prompt, default, ret_type, title)

def get_int(prompt, default=0, ret_type='Number', title=constants.TITLE):
    return _get(prompt, str(default), ret_type, title)

