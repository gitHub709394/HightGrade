# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 17:49
# @Author  : Tyx
# @Site    : 
# @File    : GetAttributeDemo.py
# @Software: PyCharm


"""
    Python __getattribute__ 的使用

    __getattribute__
        1.就是属性拦截器，

"""


class Person(object):

    def __init__(self,subName):
        self.subName = subName
        self.text = "啦啦啦"

    def __getattribute__(self, obj): # 这里 obj的值，指的是这个属性名的名称，不是属性的值
        if obj == "subName":
            return "成功访问"
        else:
            return super().__getattribute__(obj)

if __name__ == '__main__':
    p = Person("python")
    print(p.subName)
    print(p.text)

