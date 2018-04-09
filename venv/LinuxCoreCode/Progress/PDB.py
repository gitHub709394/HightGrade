# -*- coding: utf-8 -*-
# @Time    : 2018/1/28 1:11
# @Author  : Tyx
# @Site    : 
# @File    : PDB.py
# @Software: PyCharm


"""
    PDB (Python DB ) ，C/C++ 用的是GDB，是一种命令行调试工具

"""
import pdb

def testAdd(num1,num2):
    return num1+num2

if __name__ == '__main__':
    a = 10
    b = 20
    pdb.set_trace()
    result = testAdd(10,20)
    print(result)