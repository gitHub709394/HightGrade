# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 12:21
# @Author  : Tyx
# @Site    : 
# @File    : RequestTest.py
# @Software: PyCharm

import requests

URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API

def main():
    try:
        r =  requests.get(URL,params={'ip':'8.8.8.8'},timeout=1)
        print(r.status_code)
        r.raise_for_status() # 响应状态码不是200，就主动抛出异常
    except Exception as ex:
        print(ex)
    else:
        result = r.json()
        print(result)
        print(result["data"]["country"])
        print(result["data"])
        print(type(result["data"]))
        # print(type(result),result,sep="\n")

if __name__ == '__main__':
    main()