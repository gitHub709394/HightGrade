# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 14:28
# @Author  : Tyx
# @Site    : 
# @File    : TcpServer.py
# @Software: PyCharm

from socket import *

def main():

    tcpServer = socket(AF_INET,SOCK_STREAM)

    tcpServer.bind(("",8899))

    tcpServer.listen(5)
    print("-------1--------")
    clientSocket,clientInfo = tcpServer.accept()

    print("-------2--------")
    recvData = clientSocket.recv(1024)

    print("客户端信息:%s"%str(clientInfo))
    print("-------3--------")
    print("信息:%s"%(recvData.decode("gb2312")))

    clientSocket.close()
    tcpServer.close()

if __name__ == '__main__':
    main()