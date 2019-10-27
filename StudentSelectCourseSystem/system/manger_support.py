import sys
from system import Auth_manger

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

student = None
teacher = None
message1 = None
add_teacher1 = None
add_teacher2 = None
add_teacher3 = None
add_teacher4 = None
add_teacher5 = None
add_teacher6 = None
add_teacher7 = None
add_student1 = None
add_student2 = None
add_student3 = None
add_student4 = None
add_student5 = None
add_student6 = None
add_course1 = None
add_course2 = None
add_course3 = None
add_course4 = None
add_course5 = None
is_time_select_course_var = None
is_time_grade_input_var = None
user_var = None
password = None
change_password_var = None
message2 = None
message3 = None
message4 = None
message5 = None
username = None
user_birthday = None
user_sex = None
user = None


def set_tk_var(this_user):
    global student
    student = tk.StringVar()
    global teacher
    teacher = tk.StringVar()
    global message1
    message1 = tk.StringVar()
    message1.set('')
    global add_teacher1
    add_teacher1 = tk.StringVar()
    global add_teacher2
    add_teacher2 = tk.StringVar()
    global add_teacher3
    add_teacher3 = tk.StringVar()
    global add_teacher4
    add_teacher4 = tk.StringVar()
    global add_teacher5
    add_teacher5 = tk.StringVar()
    global add_teacher6
    add_teacher6 = tk.StringVar()
    global add_teacher7
    add_teacher7 = tk.StringVar()
    global add_student1
    add_student1 = tk.StringVar()
    global add_student2
    add_student2 = tk.StringVar()
    global add_student3
    add_student3 = tk.StringVar()
    global add_student4
    add_student4 = tk.StringVar()
    global add_student5
    add_student5 = tk.StringVar()
    global add_student6
    add_student6 = tk.StringVar()
    global add_course1
    add_course1 = tk.StringVar()
    global add_course2
    add_course2 = tk.StringVar()
    global add_course3
    add_course3 = tk.StringVar()
    global add_course4
    add_course4 = tk.StringVar()
    global add_course5
    add_course5 = tk.StringVar()
    global is_time_select_course_var
    is_time_select_course_var = tk.StringVar()
    p = ["select IfTakeCourse from tb_control;", 0]
    is_time_select_course_var.set(Auth_manger.Person.select_course_control(*p))
    global is_time_grade_input_var
    is_time_grade_input_var = tk.StringVar()
    pp = ["select IfInputGrade from tb_control;", 0]
    is_time_grade_input_var.set(Auth_manger.Person.select_course_control(*pp))
    global user_var
    user_var = tk.StringVar()
    user_var.set(this_user)
    global password
    password = tk.StringVar()
    global change_password_var
    change_password_var = tk.StringVar()
    # 修改密码页面message
    global message2
    message2 = tk.StringVar()
    message2.set('')
    # 课程页面message
    global message3
    message3 = tk.StringVar()
    message3.set('')
    # 学生页面message
    global message4
    message4 = tk.StringVar()
    message4.set('')
    # 教师页面message
    global message5
    message5 = tk.StringVar()
    message5.set('')
    global username
    username = tk.StringVar()
    global user_birthday
    user_birthday = tk.StringVar()
    global user_sex
    user_sex = tk.StringVar()
    global user
    user = tk.StringVar()
    user.set(this_user)
    ppp = ["select ManagerName,ManagerSex,ManagerBirthda"
           "te,ManagerRights from tb_manager where ManagerNum={0};".format(this_user), 0]
    x_list = Auth_manger.Person.who_is_me(*ppp)
    date = x_list[2].strftime('%Y-%m-%d')
    username.set(x_list[0])
    user_sex.set(x_list[1])
    user_birthday.set(date)


def add_course():
    print('manger_support.add_course')
    sys.stdout.flush()


def add_student():
    print('manger_support.add_student')
    sys.stdout.flush()


def add_teacher():
    print('manger_support.add_teacher')
    sys.stdout.flush()


def add_course_button():
    p = ["select * from tb_course where CourseNum = {0}".format(add_course1.get()), 0]
    if Auth_manger.Person.add_teacher_student_course(*p):
        message3.set('用户已存在')
    else:
        p = ["insert into tb_course values('{0}','{1}',{2},{3},'{4}');".format
             (add_course1.get(), add_course2.get(), add_course3.get(),
              add_course4.get(), add_course5.get()), 1]
        Auth_manger.Person.add_teacher_student_course(*p)
        message3.set('添加成功')
    print('manger_support.add_course_button')
    sys.stdout.flush()


def add_student_button():
    p = ["select * from tb_student where StudentNum = {0}".format(add_student1.get()), 0]
    if Auth_manger.Person.add_teacher_student_course(*p):
        message4.set('用户已存在')
    else:
        p = ["insert into tb_student values('{0}','{1}','{2}','{3}','{4}','{5}');".format
             (add_student1.get(), add_student2.get(), add_student3.get(),
              add_student4.get(), add_student5.get(), add_student6.get()), 1]
        Auth_manger.Person.add_teacher_student_course(*p)
        message4.set('添加成功')
    print('manger_support.add_student_button')
    sys.stdout.flush()


def add_teacher_button():
    p = ["select * from tb_teacher where TeacherNum = {0}".format(add_teacher1.get()), 0]
    if Auth_manger.Person.add_teacher_student_course(*p):
        message5.set('用户已存在')
    else:
        p = ["insert into tb_teacher values('{0}','{1}','{2}','{3}','{4}','{5}','{6}');".format
             (add_teacher1.get(), add_teacher2.get(), add_teacher3.get(),
              add_teacher4.get(), add_teacher5.get(), add_teacher6.get(), add_teacher7.get()), 1]
        Auth_manger.Person.add_teacher_student_course(*p)
        message5.set('添加成功')
    print('manger_support.add_teacher_button')
    sys.stdout.flush()


def change_password():
    print('manger_support.change_password')
    sys.stdout.flush()


def change_password_button():
    ppp = ["select ManagerPassword from tb_manager where ManagerNum='{0}' and ManagerPassword='{1}';".format
           (user.get(), password.get()), 0]
    if Auth_manger.Person.change_password(*ppp):
        p = ["update tb_manager set ManagerPassword='{0}' where ManagerNum='{1}';".format
             (change_password_var.get(), user.get()), 1]
        Auth_manger.Person.add_teacher_student_course(*p)
        message2.set('更改失败') if Auth_manger.Person.change_password(*ppp) else message2.set('更改成功')
    else:
        message2.set('密码错误')
    print('manger_support.change_password_button')
    sys.stdout.flush()


def control():
    print('manger_support.control')
    sys.stdout.flush()


def find_student():
    fs = ["select * from tb_student where StudentNum = {0}".format(student.get()), 0]
    fs1 = Auth_manger.Person.find_student_and_teacher(*fs)
    if fs1:
        message1.set(" 学号 专业号  姓名  性别       生日\n{0} {1}    {2}    {3}    {4}"
                     .format(fs1[0][0], fs1[0][1], fs1[0][2], fs1[0][3], fs1[0][4].strftime('%Y-%m-%d')))
    else:
        message1.set('查无此人')
    print('manger_support.find_student')
    sys.stdout.flush()


def find_teacher():
    ft = ["select * from tb_teacher where TeacherNum = {0}".format(teacher.get()), 0]
    ft1 = Auth_manger.Person.find_student_and_teacher(*ft)
    if ft1:
        message1.set("工作号 院系号  姓名  性别        生日       职称\n  {0}    {1}      {2}     {3}    {4}  {5}"
                     .format(ft1[0][0], ft1[0][1], ft1[0][2], ft1[0][3], ft1[0][4].strftime('%Y-%m-%d'), ft1[0][5]))
    else:
        message1.set('查无此人')
    print('manger_support.find_teacher')
    sys.stdout.flush()


def first_page():
    print('manger_support.first_page')
    sys.stdout.flush()


def myself():
    print('manger_support.myself')
    sys.stdout.flush()


def is_time_grade_input_func():
    # x_list 格式 p = ["update into tb_student values('12345','015','宝宝', '男','2018-12-06 15:52:57','12567');", 1]
    print('manger_support.is_time_grade_input_func')
    p = ["update tb_control set IfInputGrade={0};".format(is_time_select_course_var.get()), 1]
    Auth_manger.Person.select_course_control(*p)
    sys.stdout.flush()


def is_time_select_course_func():
    print('manger_support.is_time_select_course_func')
    p = ["update tb_control set IfTakeCourse={0};".format(is_time_select_course_var.get()), 1]
    print(p)
    Auth_manger.Person.select_course_control(*p)
    sys.stdout.flush()


def init(top, gui):
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
    from system import manger_gui

    manger_gui.vp_start_gui('001')
