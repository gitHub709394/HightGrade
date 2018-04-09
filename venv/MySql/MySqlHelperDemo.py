# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 11:20
# @Author  : Tyx
# @Site    : 
# @File    : MySqlHelperDemo.py
# @Software: PyCharm

from MySql.MySqlHelper import MySqlHelper

def main():
    # userId = input("请输入Id:")
    #
    # userName = input("请输入姓名:")

    helper = MySqlHelper(host="localhost",port=3306,db="pythontest",userName="root",pwd="123456")
    # sql = "select * from student where id = %s and userName = %s"
    # params = [userId,userName]
    # dataResult = helper.find(sql,params)
    # print(dataResult)

    sql = "insert into student(userName) values(%s)"
    params = ["LiSi"]
    count = helper.cud(sql,params)
    print(count)
    if count > 0:
        print("成功")
    else:
        print("失败")
if __name__ == '__main__':
    main()