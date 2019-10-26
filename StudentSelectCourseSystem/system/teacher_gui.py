from system import Auth_teacher, teacher_support

from tkinter import *

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


def vp_start_gui(user):
    # '''Starting point when module is the main routine.'''
    global val, w, root, this_user, CLdict, LCdict
    LCdict, CLdict = {}, {}
    this_user = user
    root = tk.Tk()
    teacher_support.set_tk_var(user)
    top = Toplevel1(root)
    teacher_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    # '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    teacher_support.set_tk_var()
    top = Toplevel1(w)
    teacher_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        # '''This class configures and populates the toplevel window.
        #    top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font9 = "-family {Microsoft YaHei UI} -size 12 -weight bold " \
                "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("399x399+601+123")
        top.title("教师界面")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.003)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=500)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.025, rely=0.025, height=28, width=128)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''学生选课信息：''')

        self.style.configure('Treeview.Heading', font="TkDefaultFont")
        self.Scrolled_tree_view1 = ScrolledTreeView(self.Frame1)
        self.Scrolled_tree_view1.place(relx=0.025, rely=0.225, relheight=0.618, relwidth=0.925)
        self.Scrolled_tree_view1.configure(show="headings")
        self.Scrolled_tree_view1.configure(columns=["Col1", "Col2", "Col3", "Col4"])
        self.Scrolled_tree_view1.heading("#0", text="Tree")
        self.Scrolled_tree_view1.heading("#0", anchor="center")
        self.Scrolled_tree_view1.column("#0", width="175")
        self.Scrolled_tree_view1.column("#0", minwidth="20")
        self.Scrolled_tree_view1.column("#0", stretch="1")
        self.Scrolled_tree_view1.column("#0", anchor="w")
        self.Scrolled_tree_view1.heading("Col1", text="Col1")
        self.Scrolled_tree_view1.heading("Col1", anchor="center")
        self.Scrolled_tree_view1.column("Col1", width="176")
        self.Scrolled_tree_view1.column("Col1", minwidth="20")
        self.Scrolled_tree_view1.column("Col1", stretch="1")
        self.Scrolled_tree_view1.column("Col1", anchor="w")

        self.Scrolled_tree_view1.heading("Col1", text="学号")
        self.Scrolled_tree_view1.heading("Col1", anchor="center")
        self.Scrolled_tree_view1.column("Col1", width="90")
        self.Scrolled_tree_view1.column("Col1", minwidth="20")
        self.Scrolled_tree_view1.column("Col1", stretch="1")
        self.Scrolled_tree_view1.column("Col1", anchor="w")

        self.Scrolled_tree_view1.heading("Col2", text="课程号")
        self.Scrolled_tree_view1.heading("Col2", anchor="center")
        self.Scrolled_tree_view1.column("Col2", width="90")
        self.Scrolled_tree_view1.column("Col2", minwidth="20")
        self.Scrolled_tree_view1.column("Col2", stretch="1")
        self.Scrolled_tree_view1.column("Col2", anchor="w")

        self.Scrolled_tree_view1.heading("Col3", text="教师")
        self.Scrolled_tree_view1.heading("Col3", anchor="center")
        self.Scrolled_tree_view1.column("Col3", width="90")
        self.Scrolled_tree_view1.column("Col3", minwidth="20")
        self.Scrolled_tree_view1.column("Col3", stretch="1")
        self.Scrolled_tree_view1.column("Col3", anchor="w")

        self.Scrolled_tree_view1.heading("Col4", text="分数")
        self.Scrolled_tree_view1.heading("Col4", anchor="center")
        self.Scrolled_tree_view1.column("Col4", width="80")
        self.Scrolled_tree_view1.column("Col4", minwidth="20")
        self.Scrolled_tree_view1.column("Col4", stretch="1")
        self.Scrolled_tree_view1.column("Col4", anchor="w")

        self.Entry7_15 = tk.Entry(self.Frame1)
        self.Entry7_15.place(relx=0.45, rely=0.875, height=24, width=69)
        self.Entry7_15.configure(background="white")
        self.Entry7_15.configure(disabledforeground="#a3a3a3")
        self.Entry7_15.configure(font="TkFixedFont")
        self.Entry7_15.configure(foreground="#000000")
        self.Entry7_15.configure(highlightbackground="#d9d9d9")
        self.Entry7_15.configure(highlightcolor="black")
        self.Entry7_15.configure(insertbackground="black")
        self.Entry7_15.configure(selectbackground="#c4c4c4")
        self.Entry7_15.configure(selectforeground="black")
        self.Entry7_15.configure(textvariable=teacher_support.grade5)

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.35, rely=0.025, relheight=0.063, relwidth=0.243)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(textvariable=teacher_support.student_course_message)
        self.Message1.configure(width=97)

        self.Message2 = tk.Message(self.Frame1)
        self.Message2.place(relx=0.05, rely=0.125, relheight=0.063, relwidth=0.343)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(textvariable=teacher_support.flush_message)
        self.Message2.configure(width=137)

        self.Scrolled_tree_view2 = ScrolledTreeView(self.Frame1)
        self.Scrolled_tree_view2.place(relx=0.775, rely=0.013, relheight=0.193, relwidth=0.2)
        self.Scrolled_tree_view2.configure(show="headings")
        self.Scrolled_tree_view2.configure(columns="Col1")
        self.Scrolled_tree_view2.heading("#0", text="Tree")
        self.Scrolled_tree_view2.heading("#0", anchor="center")
        self.Scrolled_tree_view2.column("#0", width="30")
        self.Scrolled_tree_view2.column("#0", minwidth="20")
        self.Scrolled_tree_view2.column("#0", stretch="1")
        self.Scrolled_tree_view2.column("#0", anchor="w")
        self.Scrolled_tree_view2.heading("Col1", text="课程")
        self.Scrolled_tree_view2.heading("Col1", anchor="center")
        self.Scrolled_tree_view2.column("Col1", width="31")
        self.Scrolled_tree_view2.column("Col1", minwidth="20")
        self.Scrolled_tree_view2.column("Col1", stretch="1")
        self.Scrolled_tree_view2.column("Col1", anchor="w")

        def flush_course():
            p = ["select CourseNum,CourseName from tb_course where CourseTeacherNum='{0}'".format(this_user), 0]
            ss = Auth_teacher.Teacher.select_course(*p)
            x = self.Scrolled_tree_view2.get_children()
            for item in x:
                self.Scrolled_tree_view2.delete(item)
            if ss:
                for item in ss:
                    for i in ss:
                        CLdict[i[0]] = i[1]
                        LCdict[i[1]] = i[0]
                    self.Scrolled_tree_view2.insert('', '0',
                                                    values=(item[1]))

        def flushcourse1():
            teacher_support.student_course_message.set('')
            item = self.Scrolled_tree_view2.selection()
            ss = self.Scrolled_tree_view2.item(item, "values")
            x = self.Scrolled_tree_view1.get_children()
            for item1 in x:
                self.Scrolled_tree_view1.delete(item1)
            p = ["select* from tb_stucourse where CourseNum={0}".format(LCdict[ss[0]]), 0]
            sss = Auth_teacher.Teacher.select_course(*p)
            if sss:
                for item in sss:
                    self.Scrolled_tree_view1.insert('', '0',
                                                    values=(item[0], item[1], item[2], item[3]))
                teacher_support.student_course_message.set(ss[0] + '表')
            else:
                teacher_support.student_course_message.set(ss[0] + '为空')

        def on_db_click(event):
            teacher_support.student_course_message.set('')
            item = self.Scrolled_tree_view2.selection()
            ss = self.Scrolled_tree_view2.item(item, "values")
            x = self.Scrolled_tree_view1.get_children()
            for item1 in x:
                self.Scrolled_tree_view1.delete(item1)
            p = ["select* from tb_stucourse where CourseNum='{0}'".format(LCdict[ss[0]]), 0]
            sss = Auth_teacher.Teacher.select_course(*p)
            if sss:
                for item in sss:
                    self.Scrolled_tree_view1.insert('', '0',
                                                    values=(item[0], item[1], item[2], item[3]))
                teacher_support.student_course_message.set(ss[0] + '表')
            else:
                teacher_support.student_course_message.set(ss[0] + '为空')

        self.Scrolled_tree_view2.bind("<ButtonRelease-1>", on_db_click)

        flush_course()

        def set_cell_value():
            teacher_support.flush_message.set('')
            item = self.Scrolled_tree_view1.selection()
            nn = self.Scrolled_tree_view1.item(item, "values")
            fff = int(teacher_support.grade5.get())
            e = ["select IfInputGrade from tb_control", 0]
            ee = Auth_teacher.Teacher.select_course(*e)
            if ee[0][0] == '1':
                if fff:
                    if 0 <= fff <= 100:
                        p = ["update tb_stucourse set Grade={0} where StudentNum='{1}' and CourseNum='{2}'".format
                             (fff, nn[0], nn[1]), 1]
                        Auth_teacher.Teacher.select_course(*p)
                        flushcourse1()
                    else:
                        teacher_support.flush_message.set('数值0~100')
                else:
                    teacher_support.flush_message.set('不能为空或者其它字符')
            else:
                teacher_support.flush_message.set('现在不是登记成绩时间')

        # self.Scrolled_tree_view1.bind('<ButtonRelease-1>', set_cell_value)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.68, rely=0.875, height=28, width=90)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=set_cell_value)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief='groove')
        self.Button1.configure(text='''提交并刷新''')
        self.Button1.configure(width=69)

        self.change_password_frame = tk.Frame(top)
        self.change_password_frame.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.003)
        self.change_password_frame.configure(relief='groove')
        self.change_password_frame.configure(borderwidth="2")
        self.change_password_frame.configure(relief='groove')
        self.change_password_frame.configure(background="#d9d9d9")
        self.change_password_frame.configure(highlightbackground="#d9d9d9")
        self.change_password_frame.configure(highlightcolor="black")
        self.change_password_frame.configure(width=125)

        self.Label6 = tk.Label(self.change_password_frame)
        self.Label6.place(relx=0.05, rely=0.05, height=28, width=130)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''更改密码页面  ：''')

        self.Label7 = tk.Label(self.change_password_frame)
        self.Label7.place(relx=0.213, rely=0.175, height=23, width=50)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''用户  ：''')

        self.Label8 = tk.Label(self.change_password_frame)
        self.Label8.place(relx=0.4, rely=0.175, height=23, width=87)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''user''')
        self.Label8.configure(textvariable=teacher_support.user)

        self.Label9 = tk.Label(self.change_password_frame)
        self.Label9.place(relx=0.2, rely=0.325, height=23, width=66)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''原密码   ：''')

        self.Label9_1 = tk.Label(self.change_password_frame)
        self.Label9_1.place(relx=0.2, rely=0.425, height=23, width=66)
        self.Label9_1.configure(activebackground="#f9f9f9")
        self.Label9_1.configure(activeforeground="black")
        self.Label9_1.configure(background="#d9d9d9")
        self.Label9_1.configure(disabledforeground="#a3a3a3")
        self.Label9_1.configure(foreground="#000000")
        self.Label9_1.configure(highlightbackground="#d9d9d9")
        self.Label9_1.configure(highlightcolor="black")
        self.Label9_1.configure(text='''新密码   ：''')

        self.Entry3 = tk.Entry(self.change_password_frame)
        self.Entry3.place(relx=0.4, rely=0.325, height=17, relwidth=0.36)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(show="*")
        self.Entry3.configure(textvariable=teacher_support.password)

        self.Entry3_2 = tk.Entry(self.change_password_frame)
        self.Entry3_2.place(relx=0.4, rely=0.425, height=17, relwidth=0.36)
        self.Entry3_2.configure(background="white")
        self.Entry3_2.configure(disabledforeground="#a3a3a3")
        self.Entry3_2.configure(font="TkFixedFont")
        self.Entry3_2.configure(foreground="#000000")
        self.Entry3_2.configure(highlightbackground="#d9d9d9")
        self.Entry3_2.configure(highlightcolor="black")
        self.Entry3_2.configure(insertbackground="black")
        self.Entry3_2.configure(selectbackground="#c4c4c4")
        self.Entry3_2.configure(selectforeground="black")
        self.Entry3_2.configure(show="*")
        self.Entry3_2.configure(textvariable=teacher_support.change_password)

        self.Button4 = tk.Button(self.change_password_frame)
        self.Button4.place(relx=0.475, rely=0.55, height=28, width=79)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=teacher_support.change_password_button)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(relief='groove')
        self.Button4.configure(text='''提交''')

        self.Message2 = tk.Message(self.change_password_frame)
        self.Message2.place(relx=0.4, rely=0.05, relheight=0.063, relwidth=0.443)

        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(textvariable=teacher_support.change_password_message)
        self.Message2.configure(width=177)

        self.Frame1.tkraise()

        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            command=self.Frame1.tkraise,
            compound="left",
            font="TkMenuFont",
            foreground="#000000",
            label="学生表")
        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            command=self.change_password_frame.tkraise,
            compound="left",
            font="TkMenuFont",
            foreground="#000000",
            label="修改密码")


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    # '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        # '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui('001')
