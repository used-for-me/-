import sys

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

global grade5
global student_course_message
global flush_message
global user
global password
global change_password
global change_password_message


def set_tk_var(that_user):
    global grade5
    grade5 = tk.StringVar()
    global student_course_message
    student_course_message = tk.StringVar()
    student_course_message.set('')
    global flush_message
    flush_message = tk.StringVar()
    flush_message.set('')
    global user
    user = tk.StringVar()
    user.set(that_user)
    global password
    password = tk.StringVar()
    global change_password
    change_password = tk.StringVar()
    global change_password_message
    change_password_message = tk.StringVar()
    change_password_message.set('')


def hhh():
    print('teacher_support.hhh')
    sys.stdout.flush()


def kk():
    print('teacher_support.kk')
    sys.stdout.flush()


def llll():
    print('teacher_support.llll')
    sys.stdout.flush()


def change_password_button():
    print('teacher_support.change_password_button')
    ppp = ["select TeacherPassword from tb_teacher where TeacherNum='{0}' and TeacherPassword='{1}';".format
           (user.get(), password.get()), 0]
    if Auth_teacher.Teacher.change_password(*ppp):
        p = ["update tb_teacher set TeacherPassword='{0}' where TeacherNum='{1}';".format
             (change_password.get(), user.get()), 1]
        Auth_teacher.Teacher.change_password(*p)
        change_password_message.set('更改失败') if Auth_teacher.Teacher.change_password(
            *ppp) else change_password_message.set(
            '更改成功')
    else:
        change_password_message.set('密码错误')
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    from system import teacher_gui, Auth_teacher

    teacher_gui.vp_start_gui('001')
