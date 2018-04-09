# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 13:39
# @Author  : Tyx
# @Site    : 
# @File    : DecoratorParas.py
# @Software: PyCharm

"""
    带参数的装饰器

"""
#
# def decorator(func):
#     # print("装饰")
#     def inner(*args,**kwargs):
#         # print("123")
#         func(*args,**kwargs)
#     return inner;
#
#
#
# @decorator
# def test(a,b):
#     print("1")
#     print(a)
#     print(b)
#
# test(12,32);


"""
    有返回值的装饰器

"""

# def decorator(func):
#     def inner():
#         result = func();
#         return result;
#     return inner;
#
# @decorator
# def test():
#     return "这是什么好吃的呢？";
#
#
# print(test())



"""
    装饰器 带参数
        1.通过 在 @装饰器(参数) ，在参数里面填写参数，实现传参，可以根据这个传参进行逻辑判断
"""

def decoratorArg(args):
    def decorator(func):
        def inner():
            print("啦啦啦"+args)
            func();
        return inner;
    return decorator;

@decoratorArg("发生了什么")
def test():
    print("asdfasd");


test();