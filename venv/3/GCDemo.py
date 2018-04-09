# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 17:10
# @Author  : Tyx
# @Site    : 
# @File    : GCDemo.py
# @Software: PyCharm


"""
    Python 的GC 实现方式:
        1.引用计数为主
        2.隔代（零代）回收

        注意:
            GC 清理垃圾是调用 __del__方法，如果，重写了这个方法，完了之后，要调用父类的 __del__，完成垃圾回收，否则是清理不了垃圾的
"""

import gc

class ClassA:

    def __init__(self):
        print("ClassA")


class ClassB:

    def __init__(self):
        print("ClassB")



def test():
    while True:
        a = ClassA()
        b = ClassB()
        a.classB = b
        b.classA = a
        print(gc.garbage) # gc.garbage 显示 GC 的垃圾，是个空列表
        # gc.collect() # 显示 调用 GC 回收垃圾


if __name__ == '__main__':
    # gc.disable()
    test()

