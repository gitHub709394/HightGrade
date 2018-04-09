# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 10:32
# @Author  : Tyx
# @Site    : 
# @File    : ExtendThreadDemo.py
# @Software: PyCharm

"""
    线程的使用方式二:
        1.使用一个类，继承threading.Thread，重写run 方法

"""

from threading import Thread

class MyThread(Thread):
    """
    继承Thread 类，重写run方法
    """
    def run(self):
        for i in range(5):
            print("线程名:%s , index:%s "%(self.name,i))

def main():
    t = MyThread()
    t.start()


if __name__ == '__main__':
    main()