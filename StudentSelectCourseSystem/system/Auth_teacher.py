from system import mysqlconnector


class Teacher:

    # 查询课程信息
    # 查询选课信息
    @staticmethod
    @mysqlconnector.mysql_conn
    def select_course(x_list):
        return x_list

    @staticmethod
    @mysqlconnector.mysql_conn
    def change_password(x_list):
        return x_list
