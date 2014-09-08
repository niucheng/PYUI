#!/usr/bin/env python
# coding: utf-8

import constants

import Tkinter as tk
import tkMessageBox as tkmb

root = tk.Tk()
root.withdraw()

def info(str, title=constants.TITLE):
    tkmb.showinfo(title, str, parent=root)

if __name__ == "__main__":
    info('Hello workd!')

