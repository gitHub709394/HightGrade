# -*- coding: utf-8 -*-
# @Time    : 2018/2/6 9:59
# @Author  : Tyx
# @Site    : 
# @File    : PoolCopyFile.py
# @Software: PyCharm

"""
    进程池 复制文件

"""

from multiprocessing import Pool,Manager
import os

def CopyFile(sourceFileAbs,targetFileAbs,queue):
    """
    复制文件
    :return:
    """
    with open(sourceFileAbs,"rb") as fRead:
        with open(targetFileAbs,"wb") as fWrite:
            for line in fRead:
                fWrite.write(line)
    if not queue.full():
        queue.put(targetFileAbs)

    print("%s 复制完成"%targetFileAbs)

def main():

    # 源目标目录
    sourcePath = input("请输入源文件绝对路径:")

    if not (os.path.isdir(sourcePath) and os.path.isabs(sourcePath)):
        return "输入的源文件路径不是有效路径，或者不是绝对路径"

    # 获取源文件下的所有文件
    sourceFiles = os.listdir(sourcePath)

    # 目标目录  (现在是在当前目录下)
    tuplePath = os.path.split(sourcePath)
    targetPath = os.path.join(tuplePath[0],tuplePath[1]+"-复件")
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)

    queue = Manager().Queue()
    pool = Pool(5)

    # 复制文件
    for tmpFile in sourceFiles:
        pool.apply_async(CopyFile,(os.path.join(sourcePath,tmpFile),os.path.join(targetPath,tmpFile),queue,))


    # 总大小
    allLength = len(sourceFiles)

    # 现总大小
    nowLength = 0
    while nowLength < allLength:
        if not queue.empty():
            queue.get()
            nowLength += 1
            copyRate = nowLength/allLength
            print("\rCopy 的进度是%.2f%%"%(copyRate*100),end="")
    print("Copy 完成")

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()