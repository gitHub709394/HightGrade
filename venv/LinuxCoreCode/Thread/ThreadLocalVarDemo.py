# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 14:28
# @Author  : Tyx
# @Site    : 
# @File    : ThreadLocalVarDemo.py
# @Software: PyCharm

"""
    ThreadLocal 使用这个可以，达到每个线程的变量是属于本线程的
"""
import threading

def task1(name,threadLocal):
    threadLocal.student = name
    print(threadLocal.student+" "+threading.current_thread().name)



def main():

    threadLocal = threading.local()

    task1Thread = threading.Thread(target=task1,name="Thread-A",args=("任务1",threadLocal,))
    task2Thread = threading.Thread(target=task1,name="Thread-B",args=("任务2",threadLocal,))
    task1Thread.start()
    task2Thread.start()



if __name__ == '__main__':
    main()