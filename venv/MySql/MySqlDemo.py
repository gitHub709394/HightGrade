# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 9:34
# @Author  : Tyx
# @Site    : 
# @File    : MySqlDemo.py
# @Software: PyCharm

from pymysql import *

def main():

    db = connect(host="localhost",user="root",password="123456",database="pythontest",charset="utf8")

    cursor = db.cursor()

    sql = "select * from student where id = 1"
    cursor.execute(sql)

    data = cursor.fetchone() # 获取 使用 fetchone() 方法获取单条数据.

    print(data)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()