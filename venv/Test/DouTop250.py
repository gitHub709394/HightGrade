# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 10:30
# @Author  : Tyx
# @Site    : 
# @File    : DouTop250.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import os

def getHtml(webUrl,pageIndex):
    """
    获取网页中的数据
    :param webUrl: 网址
    :param pageIndex: 参数
    :return:
    """

    html = requests.get(webUrl,params={"start":pageIndex,"filter":""}).content.decode("utf-8");

    soup = BeautifulSoup(html,"html.parser")

    data = soup.find("ol").find_all("li")
    return data

def getInfo(allMove):
    with open("movie.txt","a+",encoding="utf-8") as file:
        for item in allMove:
            # 排名
            nums = item.find("em")
            num = nums.get_text()

            # 名字
            names = item.find("span")
            name = names.get_text()

            # 导演
            characotrs = item.find("p")
            characotr = characotrs.get_text().replace(" ","").replace("\n","").replace("\xa0", "").replace("\xee", "").replace("\xf6", "").replace("\u0161", "").replace("\xf4", "").replace("\xfb", "").replace("\u2027", "").replace("\xe5", "")

            # 评语
            remarks = item.find_all("span",{"class":"ing"})
            if remarks:
                remark = remarks[0].get_text().replace("\u22ef", "")
            else:
                remark = "此影片没有评价"

            # 评分
            scores = item.find_all("span",{"class","rating_num"})
            score = scores[0].get_text()

            file.writelines(num.join("\n"))
            file.writelines(name.join("\n"))
            file.writelines(characotr.join("\n"))
            file.writelines(remark.join("\n"))
            file.writelines(score.join("\n"))
            file.writelines("".join("\n"))

def main():
    try:
        pageIndex = 0
        url = "https://movie.douban.com/top250"
        data = getHtml(url,pageIndex)
        while pageIndex <= 255:
            if len(data) != 0:
                getInfo(data)

            pageIndex += 25
            print(pageIndex)

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()