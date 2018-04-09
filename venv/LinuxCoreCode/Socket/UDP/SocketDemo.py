# -*- coding: utf-8 -*-
# @Time    : 2018/2/10 10:29
# @Author  : Tyx
# @Site    : 
# @File    : SocketDemo.py
# @Software: PyCharm

"""
    使用Socket 发送消息
"""

from socket import *
from threading import Thread

# def socketSend():
#     sock = socket(AF_INET, SOCK_DGRAM)
#
#     # 绑定端口
#     sock.bind(("",7788))
#
#     # 发送消息
#     sock.sendto(b"Hello_World", ("192.168.1.153", 8080))
#
#     sock.close()

def main():
        sock = socket(AF_INET, SOCK_DGRAM)

        # # 绑定端口(一般只有接收方要绑定端口，发送方动态端口即可)
        # sock.bind(("",7788))
        #000000000
        # # for i in range(10000):
        # #     # 发送消息
        # #     sock.sendto(b"Hello_World", ("192.168.1.153", 8080))
        # # buffSize:表示一次接受信息的时候能接受的最大字节数，如果超出了这个范围，那就只能在下次接受
        # recvData = sock.recvfrom(1024)
        # content,ipPort = recvData
        # print("content is %s"%content)
        # print(content.decode("gb2312"))
        for i in range(5):
            sock.sendto("你好".encode("gb2312"),("192.168.1.153",8080))

        sock.close()

if __name__ == '__main__':
    main()