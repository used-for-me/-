#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 26, 2018 03:56:31 PM CST  platform: Windows NT

import sys
from system import student_gui, manger_gui, teacher_gui, start_gui, Auth_select

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

user1 = None
password1 = None
var = None
return_value = None


def set_tk_var():
    global user1
    user1 = tk.StringVar()
    global password1
    password1 = tk.StringVar()
    global var
    var = tk.StringVar()
    var.set('false')
    global return_value
    return_value = tk.StringVar()


def put_in():
    print('known_support.put_in', var.get())
    denlu = Auth_select.DenLu(var.get(), user1.get(), password1.get())
    qqq = var.get()
    nnn = user1.get()
    ss = denlu.hh()
    if ss:
        return_value.set('成功登陆')
        destroy_window()
        if qqq == 'tb_manager':
            manger_gui.vp_start_gui(nnn)
        elif qqq == 'tb_student':
            student_gui.vp_start_gui(nnn)
        elif qqq == 'tb_teacher':
            teacher_gui.vp_start_gui(nnn)

    else:
        return_value.set('登陆失败')
    sys.stdout.flush()


def select_table():
    print('known_support.select_table')
    sys.stdout.flush()


def init(top, gui):
    global w, top_level, root, var
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    start_gui.vp_start_gui()
