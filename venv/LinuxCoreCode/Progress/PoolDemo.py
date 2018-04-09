# -*- coding: utf-8 -*-
# @Time    : 2018/2/5 9:21
# @Author  : Tyx
# @Site    : 
# @File    : PoolDemo.py
# @Software: PyCharm

"""
    进程池的使用

"""

from multiprocessing import Pool
import os

def task():
    for i in range(10,61):
        print("%d------------%s"%(i,os.getpid()))
    print("------完成")


if __name__ == '__main__':

    pool = Pool(3) # 创建一个进程池，里面放着3个进程
    for i in range(5):
        pool.apply_async(task)
    print("完成任务完成")
    pool.close()
    pool.join()