# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 14:06
# @Author  : Tyx
# @Site    : 
# @File    : MySqlLogin.py
# @Software: PyCharm

from MySql.MySqlHelper import MySqlHelper
from hashlib import sha1

def sha1Encrypt(pwd):
    """
    sha1 加密
    :return:
    """
    s1 = sha1()
    s1.update(pwd.encode("utf-8"))
    return s1.hexdigest()

def main():
    userName = input("请输入用户名:")
    pwd = input("请输入密码:")
    pwdEncrypt = sha1Encrypt(pwd)
    print("sha1 加密之后:%s"%pwdEncrypt)
    dbHelper = MySqlHelper(host="localhost",port=3306,db="pythontest",userName="root",pwd="123456")
    sql = "select userName,pwd from student where userName = %s"
    params = [userName]
    data = dbHelper.find(sql,params)
    print(data)
    if len(data) == 0:
        print("用户名错误")
    elif data[0][1] == pwdEncrypt:
        print("登录成功")
    else:
        print("密码错误")


if __name__ == '__main__':
    main()