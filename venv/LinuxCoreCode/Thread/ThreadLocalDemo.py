# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 10:36
# @Author  : Tyx
# @Site    : 
# @File    : ThreadLocalDemo.py
# @Software: PyCharm



"""
    线程中的局部变量是独自共享的，所以在修改本线程中修改局部变量是不需要加锁的
"""

from threading import Thread
import threading
import time

def test1():
    threadName = threading.current_thread().name
    num = 100
    if threadName == "Thread-1":
        num = 100
    else:
        time.sleep(1)
        num += 1
    print("%s"%threading.current_thread().name)
    print("test1 num:%s"%num)



def test2():
    num = 100
    num += 1
    print("%s" % threading.current_thread().name)
    print("test2 num:%s"%num)

def main():

    t1 = Thread(target=test1)
    t1.start()

    t2 = Thread(target=test1)
    t2.start()

if __name__ == '__main__':
    main()