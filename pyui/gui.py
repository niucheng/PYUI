#!/usr/bin/env python
# coding: utf-8

import Tkinter as tk

import config

if config.ver < 3:
    import tkMessageBox as tkmb
else:
    from Tkinter import messagebox as tkmb

import color
import constants

root = tk.Tk()
root.withdraw()

def puts(str, title=constants.TITLE):
    tkmb.showinfo(title, str % color.ANSI_NONE_COLOR_SET)

def info(str, title=color.ANSI_COLOR_INFO):
    tkmb.showinfo(title, str, parent=root)

def warn(str, title=color.ANSI_COLOR_WARN):
    tkmb.showwarning(title, str, parent=root)

def error(str, title=color.ANSI_COLOR_ERROR):
    tkmb.showerror(title, str, parent=root)

def success(str, title=color.ANSI_COLOR_SUCCESS):
    tkmb.showinfo(title, str, parent=root)

ret = None

def _get(prompt, default='', type='', title=constants.TITLE):
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

def gets(prompt, default='', type='String', title=constants.TITLE):
    return _get(prompt, default, type, title)

def get_int(prompt, default=0, type='Number', title=constants.TITLE):
    return _get(prompt, str(default), type, title)

