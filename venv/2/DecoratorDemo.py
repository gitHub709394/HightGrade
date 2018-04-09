# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 9:35
# @Author  : Tyx
# @Site    : 
# @File    : DecoratorDemo.py
# @Software: PyCharm


"""
    装饰器的使用
        1.装饰器的作用是通过，在不修改原来的功能的情况下，添加扩展功能

"""
# 装饰器的简单使用
# def w1(func):
#     def inner():
#         print("---权限验证---")
#         func();
#     return inner;
#
# # 这句话的意思就是等价于  f1 = w1(f1)
# @w1
# def f1():
#     print("---1---");
#
# @w1
# def f2():
#     print("---2---");
#
#
# f1();
# f2();



# 装饰器 两个装饰器

def makeBold(func):
    """ 变粗 """
    print("变粗");
    def wrapped():
        print("-----变粗-----")
        return "<b>"+func()+"</b>";
    return wrapped;

def makeItary(func):
    """ 斜体 """
    print("斜体");
    def wrapped():
        print("----斜体------")
        return "<i>"+func()+"</i>";
    return wrapped;

# @makeBold
# def f1():
#     return "中二不是病";
#
# @makeItary
# def f2():
#     return "叉烧包好吃";

@makeBold
@makeItary
def f3():
    print("f3")
    return "斜体加上粗体";

# print(f1());
# print(f2());
print(f3());
