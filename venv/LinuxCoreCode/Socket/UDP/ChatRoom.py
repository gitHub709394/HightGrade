# -*- coding: utf-8 -*-
# @Time    : 2018/2/10 14:00
# @Author  : Tyx
# @Site    : 
# @File    : ChatRoom.py
# @Software: PyCharm

"""
    聊天室
"""

from socket import *


def main():
    revcSocket = socket(AF_INET, SOCK_DGRAM)
    revcSocket.bind(("", 7788))
    while True:
        content,destInfo = revcSocket.recvfrom(1024)
        print("[%s]:%s"%(destInfo,content.decode("gb2312")))


if __name__ == '__main__':
    main()