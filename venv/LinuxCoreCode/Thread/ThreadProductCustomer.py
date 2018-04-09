# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 9:37
# @Author  : Tyx
# @Site    : 
# @File    : ThreadProductCustomer.py
# @Software: PyCharm


"""
    生产者消费者
"""

from threading import Thread,Lock
from queue import Queue # 这里用的Queue,是 queue.Queue


class Product(Thread):



    def __init__(self, group=None, target=None, name=None, kwargs=None, *, daemon=None,args ):
        super().__init__(None, target, name, args, kwargs, daemon=daemon)
        self.queue = args[0]
        self.mutex = args[1]

    def run(self):
        count = 0
        while True:
            try:
                if self.queue.qsize() < 1000:  # 当队列中中的数据少于 100的时候才去生产数据
                    for i in range(500):
                        count += i
                        self.mutex.acquire()
                        self.queue.put_nowait(count)
                        self.mutex.release()
                        print("生产 %s" % count)
            except Exception as ex:
                print("生产异常-----------------------------------------------")
                print(ex)
                print("arg = " + len(self.queue))
                break;





class Customer(Thread):

    def __init__(self, group=None, target=None, name=None, kwargs=None, *, daemon=None,args ):
        super().__init__(None, target, name, args, kwargs, daemon=daemon)
        self.queue = args[0]
        self.mutex = args[1]

    def run(self):
        while True:
            try:
                for i in range(3):
                    if not self.queue.empty():
                        self.mutex.acquire()
                        tmp = self.queue.get_nowait()
                        self.mutex.release()
                        print("消费 %s" %tmp)
                    else:
                        print("队列为空")
            except Exception as ex:
                print("消费异常-----------------------------------------------")
                print(ex)
                print("arg = " + len(self.queue))
                break


def main():

    # 队列当缓冲区
    queue = Queue()

    # 队列锁
    mutex = Lock()

    # 初始化
    for i in range(500):
        queue.put_nowait(i)

    for i in range(2):
        productThread = Product(args=(queue,mutex,))
        productThread.start()

    for i in range(5):
        customerThread = Customer(args=(queue,mutex,))
        customerThread.start()


if __name__ == '__main__':
    main()