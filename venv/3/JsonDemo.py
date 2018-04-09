# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 12:42
# @Author  : Tyx
# @Site    : 
# @File    : JsonDemo.py
# @Software: PyCharm

"""
    Json 解析

"""

import json

if __name__ == '__main__':
    # numList = [1,2,34,5]
    # # json.dumps 把对象转成Json 字符串
    # jsonStr = json.dumps(numList)
    # print(jsonStr)
    # # json.loads 把json 字符串 转成 python 对象
    # jsonObj = json.loads(jsonStr,encoding="utf-8")
    # print(jsonObj)

    jsonStr = '{"name":"SO JSON在线","url":"https://www.sojson.com","address":{"city":"北京","country":"中国"},"domain_list":[{"name":"ICP备案查询","url":"https://icp.sojson.com"},{"name":"JSON在线解析","url":"https://www.sojson.com"},{"name":"房贷计算器","url":"https://fang.sojson.com"}]}'
    jsonObj = json.loads(jsonStr,encoding="utf-8")
    print(jsonObj)


