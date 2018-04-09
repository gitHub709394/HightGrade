# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 14:50
# @Author  : Tyx
# @Site    : 
# @File    : TcpClient.py
# @Software: PyCharm

"""
Tcp Client 客户端
"""

from socket import *

def main():

    clientTcp = socket(AF_INET,SOCK_STREAM)

    clientTcp.connect(("192.168.1.75",7787))

    clientTcp.send("今晚打老虎".encode("gb2312"))

    recvData = clientTcp.recv(1024)
    print(recvData.decode("gb2312"))

    clientTcp.close()


if __name__ == '__main__':
    main()