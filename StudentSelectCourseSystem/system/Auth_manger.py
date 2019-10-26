from system import mysqlconnector


class Person(object):
    def __init__(self, user, password):
        self.__user = user
        self.__password = password

    # 选课控制
    @staticmethod
    @mysqlconnector.mysql_conn
    def select_course_control(s):
        if s:
            if s[0][0] == '1':
                return '1'
            else:
                return '0'

    # 成绩录入控制
    @staticmethod
    @mysqlconnector.mysql_conn
    def grade_input_control(s):
        return s

    # 添加学生
    @staticmethod
    @mysqlconnector.mysql_conn
    def add_student(s):
        return s

    # x_list 格式 p = ["insert into tb_student values('12345','015','宝宝', '男','2018-12-06 15:52:57','12567');", 1]

    # 添加教师
    @staticmethod
    @mysqlconnector.mysql_conn
    def add_teacher(s):
        return s

    # 更改密码
    @staticmethod
    @mysqlconnector.mysql_conn
    def change_password(s):
        return s

    # 可选课程添加 【课程可选标志字段（是否已结束），可选专业，可选人数，已选人数】
    # 个人资料
    @staticmethod
    @mysqlconnector.mysql_conn
    def who_is_me(s):
        s = s[0]
        return s

    # 查找学生和查找教师
    @staticmethod
    @mysqlconnector.mysql_conn
    def find_student_and_teacher(s):
        return s

    # 添加教师、学生、课程
    @staticmethod
    @mysqlconnector.mysql_conn
    def add_teacher_student_course(s):
        return s
