# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 11:09
# @Author  : Tyx
# @Site    : 
# @File    : MySqlHelper.py
# @Software: PyCharm

from pymysql import *

class MySqlHelper(object):

    def __init__(self,host,db,userName,pwd,charset="utf8",port = 3306):
        self.host = host
        self.port = port
        self.db = db
        self.userName = userName
        self.pwd = pwd
        self.charset = charset

    def __open(self):
        """
        打开连接
        :return:
        """
        self.conn = connect(host=self.host,port=self.port,database=self.db,user=self.userName,password=self.pwd,charset=self.charset)
        self.cursor = self.conn.cursor()

    def __close(self):
        """
        关闭连接
        :return:
        """
        if self.conn != None:
            self.conn.close()
        if self.cursor != None:
            self.cursor.close()

    def find(self,sql,params=[]):
        """
        查询
        :param sql: Sql语句
        :param params: 参数化
        :return:
        """

        try:
            # 打开连接
            self.__open()

            # 执行Sql 语句
            self.cursor.execute(sql,params)

            result = self.cursor.fetchall()

            # 关闭连接
            self.__close()

            return result
        except Exception as ex:
            print(ex.message)


    def cud(self,sql,params=[]):
        """
        增加 更新 删除
        :param sql:
        :param params:
        :return:
        """
        try:
            self.__open()

            count = self.cursor.execute(sql,params)

            self.conn.commit()

            self.__close()

            return count
        except Exception as ex:
            print(ex.message)
def main():
    pass


if __name__ == '__main__':
    main()