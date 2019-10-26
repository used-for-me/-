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

global select_num
global withdrawal_num
global message1
global selected_course_message
global user
global password
global change_password
global change_password_message
global find_grade_message


def set_tk_var(that_user):
    global select_num
    select_num = tk.StringVar()
    global withdrawal_num
    withdrawal_num = tk.StringVar()
    global message1
    message1 = tk.StringVar()
    message1.set('')
    global selected_course_message
    selected_course_message = tk.StringVar()
    selected_course_message.set('')
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
    global find_grade_message
    find_grade_message = tk.StringVar()
    find_grade_message.set('')


def change_password_button():
    print('student_gui_support.change_password_button')
    ppp = ["select StudentPassword from tb_student where StudentNum='{0}' and StudentPassword='{1}';".format
           (user.get(), password.get()), 0]
    if Auth_student.Student.change_password(*ppp):
        p = ["update tb_student set StudentPassword='{0}' where StudentNum='{1}';".format
             (change_password.get(), user.get()), 1]
        Auth_student.Student.change_password(*p)
        change_password_message.set('更改失败') if Auth_student.Student.change_password(
            *ppp) else change_password_message.set(
            '更改成功')
    else:
        change_password_message.set('密码错误')
    sys.stdout.flush()


def first_page1():
    print('student_gui_support.first_page1')
    sys.stdout.flush()


def first_page2():
    print('student_gui_support.first_page2')
    sys.stdout.flush()


def first_page3():
    print('student_gui_support.first_page3')
    sys.stdout.flush()


def first_page4():
    print('student_gui_support.first_page4')
    sys.stdout.flush()


def flush_find_grade_button():
    print('student_gui_support.flush_find_grade_button')
    sys.stdout.flush()


def flush_selected_course():
    print('student_gui_support.flush_selected_course')
    sys.stdout.flush()


def select_course_button():
    print('student_gui_support.select_course_button')
    sys.stdout.flush()


def withdrawal_course_button():
    print('student_gui_support.withdrawal_course_button')
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
    from system import student_gui, Auth_student

    student_gui.vp_start_gui('11412')
