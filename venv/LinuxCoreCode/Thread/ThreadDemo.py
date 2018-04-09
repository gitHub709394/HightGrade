# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 9:36
# @Author  : Tyx
# @Site    : 
# @File    : ThreadDemo.py
# @Software: PyCharm

"""
    线程的使用
        1.Thread 会等待子线程执行完后再退出
"""
import time
from threading import Thread

def test():
    print("线程池的使用.....")
    time.sleep(1)


def main():
    for i in range(5):
        t = Thread(target=test)
        t.start()

    print("啦啦啦")

if __name__ == '__main__':
    main()