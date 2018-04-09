# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 22:14
# @Author  : Tyx
# @Site    : 
# @File    : SimpleOrDeepCopy.py
# @Software: PyCharm

"""
    深拷贝和浅拷贝
        浅拷贝:就是把引用复制出来一份，用一个变量接受
        深拷贝:就是把内容的东西都复制出来一份，是再内存中再重新复制出来一份，
"""

import copy

"""
    深浅拷贝的简单应用
"""
# a = [11,22,33];
#
#
# # 这个浅拷贝
# b = a;
# print(id(a))
# print(id(b))
#
# # 这个是深拷贝
# c = copy.deepcopy(a)
#
# print(id(c))



"""
    copy.copy的使用
        1.如果传入参数对象是可变类型，会发生深拷贝，且只深拷贝一次，也就是把最外面的包裹对象深拷贝一次
        2.如果传入参数对象是不可变类型，不会发生深拷贝
"""


"""
    copy.copy() 的简单使用
"""
# # a = [11,22,33]; # 列表的使用
# a = (11,22,33); # 元祖的使用
#
# b = a;
#
# print(id(a))
# print(id(b))
#
# c = copy.copy(a)
# print(id(c))


""" 
    列表的测试
"""
a = [11,22,33];
b = [44,55,66];


# c = [a,b];
c = (a,b); # 元祖是不可变类型，所以这里只是浅拷贝

print(id(c))
print(id(c[0]))
print(id(c[1]))

print("-------------华丽的分割线-------------------")
d = copy.copy(c); # 列表是可变类型，所以这里会发生深拷贝，但是因为copy.copy 只会发生一次，所以这里，只有最外面的对象发生了深拷贝
print(id(d))
print(id(d[0]))
print(id(d[1]))




