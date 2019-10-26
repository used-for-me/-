import pymysql
import functools


def mysql_conn(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        a = MysqlConn(*args)
        x_list = a.student_conn()
        result = func(x_list, **kwargs)
        return result

    return wrapper


class MysqlConn:
    def __init__(self, sql_language='', ss=0, user='root', password='tangtang'):
        self.__user = user
        self.__password = password
        self.__ss = ss
        self.__sql_language = sql_language

    # 设置三个参数
    def set_user(self, user):
        self.__user = user

    def set_password(self, password):
        self.__password = password

    def set_db(self, ss):
        self.__ss = ss

    def set_sql_language(self, sql_language):
        self.__sql_language = sql_language

    # 连接数据库并传入或更改数据
    def student_conn(self):
        try:
            conn = pymysql.connect(host='localhost', user=self.__user, password=self.__password,
                                   db='studentmessagemanagersystem', port=3306)
            cur = conn.cursor()
            cur.execute(self.__sql_language)
            x_list = []

            # 如果ss=0有返回值
            if self.__ss == 0:
                x_list = cur.fetchall()
            # 如果ss=1没有返回值
            if self.__ss == 1:
                conn.commit()
            cur.close()
            conn.close()
        except pymysql.err.Error as e:
            print('mysql error %d: %s' % (e.args[0], e.args[1]))
            raise
        else:
            return x_list
