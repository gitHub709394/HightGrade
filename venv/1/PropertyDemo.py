# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 9:25
# @Author  : Tyx
# @Site    : 
# @File    : PropertyDemo.py
# @Software: PyCharm

"""

    Python 属性的使用，类视C# 的属性，不过写法比C#要繁琐

"""


# 使用 property 写法

# class Animal(object):
#     def __init__(self):
#         self.__name = "你好";
#
#
#     def getName(self):
#         return self.__name;
#
#     def setName(self,value):
#         self.__name = value;
#
#     # 属性的写法
#     # 第一个写get方法名，第二个写set方法名
#     # 注意不能带括号
#     name = property(getName,setName);
#
# animal = Animal();
# print(animal.name);
# animal.name = "美猴王";
#
# print(animal.name)


# 使用装配器
class Animal(object):
    def __init__(self):
        self.__name = "齐天大圣";

    @property
    def name(self):
        return self.__name;

    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self.__name = value;
        else:
            print("error：不是整形数字")


animal = Animal();
print(animal.name)
animal.name = "猴哥猴哥，你真了不得!!";
print(animal.name)