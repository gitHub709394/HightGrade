# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 10:49
# @Author  : Tyx
# @Site    : 
# @File    : DynamicLanguage.py
# @Software: PyCharm

"""
    python 动态语言
        1.静态语言:
            指的是需要经过编译，的语言，如 C,C#,Java
        2.动态语言
            程序运行过程中，添加修修补补

"""

class Person(object):
    def __init__(self,name):
        self.Name = name;
        self.age = 10;

def run():
    print("啦啦啦")

zhangSan = Person("中二");
zhangSan.age = 19;
zhangSan.address = "广东";
zhangSan.run();
print(zhangSan.address);

# # Person.num = 100; # 添加类属性
# liSi = Person("李四");
# liSi.age = 10;
# print(liSi.num)



