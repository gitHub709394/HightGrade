# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 9:40
# @Author  : Tyx
# @Site    : 
# @File    : MutexLockDemo.py
# @Software: PyCharm

"""
    互斥锁
"""
from threading import Thread,Lock

num = 0

def test1(mutex):
    global num
    for i in range(1000000):
        mutex.acquire() # 只有当
        num += 1
        mutex.release()

    print("test1 %s"%num)

def test2(mutex):
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1 # 只有当操作这个 num 的时候，才要加锁，上锁的代码要在不影响功能的大前提下，
        mutex.release()
    print("test2 %s"%num)

def main():

    mutex = Lock()

    t1 = Thread(target=test1,args=(mutex,))
    t1.start()

    t2 = Thread(target=test2,args=(mutex,))
    t2.start()

    print("最后 %s"%num)


if __name__ == '__main__':
    main()