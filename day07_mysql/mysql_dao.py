"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: mysql_createDatabase.py
@time: 2017/11/13 11:34
@describe:
"""
from abc import ABCMeta, abstractmethod
import pymysql


# 连接层
class DBUtil(object):
    __mysql_host = '127.0.0.1'
    __mysql_port = 3306
    __mysql_user = 'root'
    __mysql_password = '123456'
    __database = 'bbs1'
    __db = pymysql.connect(host=__mysql_host, port=__mysql_port, user=__mysql_user, password=__mysql_password,
                           db=__database)

    def get_connect(self):
        return self.__db


# vo层
class Login(object):
    def __init__(self):
        self.username = ''
        self.password = ''

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


# vo层
class Student(object):
    def __init__(self):
        self.id = 0
        self.name = 0
        self.grade = 0
        self.classid = 0
        self.sex = 0
        self.isMonitor = False
    def __init__(self,name:str,grade:int,classid:int,sex:str,isMonitor:str):
        self.name = name
        self.grade = grade
        self.classid = classid
        self.sex = sex
        self.isMonitor = isMonitor


# DAO接口层
class Interface(object):
    __metaclass__ = ABCMeta  # 指定这是一个抽象类

    @abstractmethod
    def insert(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def queryById(self, id):
        pass

    @abstractmethod
    def queryAll(self):
        pass


class StudentDaoImpl(Interface):  # 必须实现interface中的所有函数，否则会编译错误
    __db = DBUtil().get_connect()
    __mysql_cursor = __db.cursor()  # 创建一个游标对象 cursor

    def queryById(self, id):
        pass

    def insert(self, obj:Student):
        sql = "INSERT INTO " + "student" + " VALUES ("+"null,'"+str(obj.name)+"',"+str(obj.grade)+","+str(obj.classid)+",'"+str(obj.sex)+"','"+str(obj.isMonitor)+"'"+")"
        print(sql)
        try:
            # 执行sql语句
            self.__mysql_cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
        except:
            # 如果发生错误则回滚
            self.__db.rollback()

    def queryAll(self):
        # SQL 查询语句
        sql = "SELECT * FROM student"
        query_list = []
        try:
            # 执行SQL语句
            self.__mysql_cursor.execute(sql)
            # 获取所有记录列表
            results = self.__mysql_cursor.fetchall()
            for row in results:
                query_dic = {'id' : row[0],'name' : row[1], 'grade' : row[2],'classid' : row[3],'sex' : row[4],'isMonitor' : row[5]}
                query_list.append(query_dic)
        except:
            print("Error: unable to fetch data")
        return query_list

    def queryMaxId(self):
        # SQL 查询语句
        sql = "SELECT max(id) FROM student"
        # 执行SQL语句
        self.__mysql_cursor.execute(sql)
        # 获取所有记录列表
        results = self.__mysql_cursor.fetchall()
        return results[0][0]

    def delete(self, sid):
        # SQL 删除语句
        sql = "DELETE FROM student WHERE id = "+str(sid)
        print(sql)
        try:
            # 执行SQL语句
            self.__mysql_cursor.execute(sql)
            # 提交修改
            self.__db.commit()
        except:
            # 发生错误时回滚
            self.__db.rollback()

    def update(self, obj):
        pass


class LoginDaoImpl(Interface):  # 必须实现interface中的所有函数，否则会编译错误
    __db = DBUtil().get_connect()
    __mysql_cursor = __db.cursor()  # 创建一个游标对象 cursor

    def queryById(self, username):
        sql = "select * from login where username = '" + username + "'"
        try:
            # 执行SQL语句
            self.__mysql_cursor.execute(sql)
            # 获取所有记录列表
            results = self.__mysql_cursor.fetchall()
            for row in results:
                username = row[0]
                password = row[1]
                print(username, password)
        except:
            # 如果发生错误则回滚
            self.__db.rollback()

    def login(self, username, password):
        sql = "select * from login where username = '" + username + "' And password = '" + password + "'"
        print(sql)
        try:
            # 执行SQL语句
            self.__mysql_cursor.execute(sql)
            # 获取所有记录列表
            results = self.__mysql_cursor.fetchall()
            print(results)
            if len(results) is 1:
                return True
            else:
                return False
        except:
            # 如果发生错误则回滚
            self.__db.rollback()

    def insert(self, obj: Login):
        print(obj.username)
        sql = "INSERT INTO " + "login" + " VALUES (" + "'" + obj.username + "','" + obj.password + "'" + ")"
        print(sql)
        try:
            # 执行sql语句
            self.__mysql_cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
        except:
            # 如果发生错误则回滚
            self.__db.rollback()

    def queryAll(self):
        pass

    def delete(self, id):
        pass

    def update(self, obj):
        pass


class DaoFactory(object):
    def getStudentDaoImpl(self):
        return StudentDaoImpl()

    def getLoginDaoImpl(self):
        return LoginDaoImpl()


if __name__ == '__main__':
    daoFactory = DaoFactory()
    studentDaoImpl = daoFactory.getStudentDaoImpl()
    loginDaoImpl = daoFactory.getLoginDaoImpl()
    print(studentDaoImpl.queryMaxId())
