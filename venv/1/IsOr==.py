# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 18:44
# @Author  : Tyx
# @Site    : 
# @File    : IsOr==.py
# @Software: PyCharm


"""
    is 与 == 的区别
        is 用来判断是否指向同一个对象
        == 用来判断对象的内容是否相等
"""

a = [11,22,33]
b = [11,22,33]

print(a == b) # True

print(a is b) # False
