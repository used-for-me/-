from system import mysqlconnector


class Student(object):
    def __init__(self, user, password):
        self.__user = user
        self.__password = password

    @staticmethod
    @mysqlconnector.mysql_conn
    def select_course(x_list):
        return x_list

    @staticmethod
    @mysqlconnector.mysql_conn
    def selected_course(x_list):
        return x_list

    @staticmethod
    @mysqlconnector.mysql_conn
    def select_course_control(x_list):
        return x_list

    @staticmethod
    @mysqlconnector.mysql_conn
    def change_password(x_list):
        return x_list

    # 选课
    # 退选
    # 查询选课信息
    # 更改密码
    # 查询成绩
    # 统一使用一个接口，但参数不同

# 测试数据
# if __name__ == '__main__':
#     student = Student(1, 2)
#     p = ["insert into tb_student values('12345','015','宝宝', '男','2018-12-06 15:52:57','12567');", 1]
#     student.select_course(*p)
