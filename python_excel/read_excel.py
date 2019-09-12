# -*- coding:utf-8 -*-
# Author: xueminchao
# @Time: 2019-09-12 9:36

import xlrd

book =  xlrd.open_workbook('服务费用.xlsx')
# 查看excel 有几张表
# for sheet in book.sheets():
#     print(sheet.name)
sheet = book.sheet_by_name('阿里云服务器')
# print(sheet)

#打印行数
#print(sheet.nrows)

#打印数据
# for i in range(sheet.nrows):
#     row = sheet.row_values(i)  #将每一行内容组成列表保存到row变量中
#     #打印当前行每个单元格的值
#     for cell in row:
#         print(cell)


# 输出行号和对应行的内容
count = 0   #控制输出几行
for i in range(sheet.nrows):
    if count < 10:
        row = sheet.row_values(i)
       # print(i,row)

    count +=1


#获取指定单元格内容
print(sheet.cell(1,0).value)

#获取单元格内容的数据类型
# 说明：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print(sheet.cell(1,0).ctype)



# 参考 https://www.cnblogs.com/xiao-apple36/p/9603499.html










