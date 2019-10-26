import pymysql


class DenLu:
    def __init__(self, sign, user, password):
        self.__sign = sign
        self.__user = user
        self.__password = password

    def hh(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='tangtang',
                                   db='studentmessagemanagersystem', port=3306)
            cur = conn.cursor()
            p = ''
            print(self.__sign)
            if self.__sign == 'tb_student':
                p = 'select StudentNum,StudentPassword from {0} where Stu' \
                    'dentNum="{1}" and StudentPassword="{2}";'.format(self.__sign, self.__user, self.__password)
            elif self.__sign == "tb_teacher":
                p = 'select TeacherNum,TeacherPassword from {0} where Tea' \
                    'cherNum="{1}" and TeacherPassword="{2}";'.format(self.__sign, self.__user, self.__password)
            elif self.__sign == "tb_manager":
                p = 'select ManagerNum,ManagerPassword from {0} where Man' \
                    'agerNum="{1}" and ManagerPassword="{2}";'.format(self.__sign, self.__user, self.__password)
            cur.execute(p)
            nn = cur.fetchall()
            cur.close()
            conn.close()
            if nn:
                return self.__sign, self.__user
        except pymysql.err.Error as e:
            print('mysql error %d: %s' % (e.args[0], e.args[1]))
