# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 11:32
# @Author  : Tyx
# @Site    : 
# @File    : FtpDemo.py
# @Software: PyCharm

from socket import *
import struct
import os

def main():

    udpSocket = socket(AF_INET,SOCK_DGRAM)
    # !H8sb5sb
    fileName = "a.png"
    sendToData = struct.pack("!H%dsb5sb"%len(fileName),1,fileName.encode("utf-8"),0,"octet".encode("utf-8"),0)

    print(sendToData)

    udpSocket.sendto(sendToData,("192.168.1.75",69))

    f = open("D:/%s"%fileName,"bw")
    flag = True
    num = 0
    while True:

        recvData,serverInfo = udpSocket.recvfrom(1024)
        # 状态码
        opCode = struct.unpack("!H",recvData[:2])
        # 数据块编号
        packCode = struct.unpack("!H",recvData[2:4])

        print("数据块编号%s"%packCode)

        if opCode[0] == 5:
            print("sorry,没有这个文件")
        elif opCode[0] == 3:

            num = num + 1

            if num == 65536:
                num = 0

            if num == packCode[0]:
                f.write(recvData[4:])
                num = packCode[0]

            # 整理 ACK 的数据包
            ackData = struct.pack("!HH",4,packCode[0])
            udpSocket.sendto(ackData,serverInfo)
        if len(recvData) < 516:
            break

    if flag == True:
        f.close()
    else:
        os.unlink("D:/%s"%fileName)
    udpSocket.close()

if __name__ == '__main__':
    main()