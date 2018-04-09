# -*- coding: utf-8 -*-
# @Time    : 2018/2/5 10:35
# @Author  : Tyx
# @Site    : 
# @File    : ProcessQueueDemo.py
# @Software: PyCharm

"""
    Process
        1.进程间的通信，使用Queue，这里使用的进程是Process
"""

from multiprocessing import Process,Queue
import os,time,random

def writeData(queue):
    """
    写入数据
    :param queue: 队列
    :return:
    """
    for i in ['A','B','C']:
        queue.put_nowait(i) # 把数据添加 到队列中去
        print("write %s"%i)
        time.sleep(random.random())

def readData(queue):
    """

    :param queue: 队列
    :return:
    """
    while True:
        if not queue.empty():
            print("read %s "%queue.get_nowait())
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':

    # 队列对象
    queue = Queue()

    # 写入进程
    writeProcess = Process(target=writeData,args=(queue,))

    # 开启写入进程
    writeProcess.start()

    # 等待写入进程完成
    writeProcess.join()

    # 读取进程
    readProcess = Process(target=readData,args=(queue,))

    # 开启读取进程
    readProcess.start()

    # 等待读取进程完成
    readProcess.join()

    print("程序结束")
