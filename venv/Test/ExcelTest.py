# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 17:30
# @Author  : Tyx
# @Site    : 
# @File    : ExcelTest.py
# @Software: PyCharm

import xlwt

def setStyle(fontName,fontHeight,bold=True):

    # 创建样式
    style = xlwt.XFStyle()

    # 创建字体
    font = xlwt.Font()

    # 设置字体格式
    font.name = fontName
    font.height = fontHeight
    font.bold = bold
    font.colour_index = 0

    # 设置边距
    # borders = xlwt.Borders()
    # borders.left = 6
    # borders.right = 6
    # borders.top = 6
    # borders.bottom = 6

    # 创建对齐方式
    aligment = xlwt.Alignment()
    aligment.horz =xlwt.Alignment.HORZ_CENTER

    # 把字体和边距应用到样式中
    style.font = font
    style.alignment = aligment
    # style.borders = borders

    return style


def main():
    # 创建一个excel 工作簿
    wb = xlwt.Workbook(encoding="utf-8")

    # 创建一个sheet
    sheet1 = wb.add_sheet("sheet1")

    # # 总行数
    # rows = 10
    #
    # # 总列数
    # cols = 3
    #
    # # 创建格式 style
    # style = xlwt.XFStyle()
    #
    # # 创建font，设置字体
    # font = xlwt.Font()
    #
    # # 设置字体格式
    # font.name = "微软雅黑"
    #
    # # 将字体font，应用到格式style
    # style.font = font
    #
    # # 创建 alignment 居中
    # aligment = xlwt.Alignment()
    #
    # # 水平居中
    # aligment.horz = xlwt.Alignment.HORZ_CENTER
    #
    # # 应用到格式style
    # style.alignment = aligment
    #
    # for i in range(cols):
    #     sheet1.col(i).width = 5000
    #
    # sheet1.write(0,0,"今晚打老虎",style)
    # sheet1.write(0,1,"今晚打老虎",style)
    # sheet1.write(0,2,"今晚打老虎",style)
    #
    # # for i in range(cols):
    # #     sheet1.write(0,i,i,style)
    #
    # for i in range(1,rows):
    #     for j in range(cols):
    #         sheet1.write(i,j,i,style)
    #
    # wb.save("奥特曼.xls")
    titleStyle = setStyle("微软雅黑",250,True)
    sheet1.write(0,0,"Hello",style=titleStyle)
    sheet1.write(0,1,"World",style=titleStyle)

    contentStyle = setStyle("微软雅黑",250,False)

    for i in range(1,11):
        for j in range(0,2):
            sheet1.write(i,j,i+j,contentStyle)

    sheet1.write(12,0,"合计:")

    sheet1.write(12,1,xlwt.Formula("SUM(B2:B11)"))

    wb.save("冰淇淋.xls")

if __name__ == '__main__':
    main()