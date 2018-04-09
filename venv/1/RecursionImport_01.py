# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 13:52
# @Author  : Tyx
# @Site    : 
# @File    : RecursionImport.py
# @Software: PyCharm
"""
    循环导入
"""

from RecursionImport_02 import b

def a():
    print("----aaa--");
    b();

a();