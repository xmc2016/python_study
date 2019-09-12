# -*- coding:utf-8 -*-
# Author: xueminchao
# @Time: 2019-09-12 10:48

import xlwt

book = xlwt.Workbook()

sheet = book.add_sheet("test")
# sheet.write(0,0,'name')  #行,列,内容
title = ['姓名','班级','住址','手机号']

content = [
    ['小王','一班','合阳县','1999233333'],
    ['小张','二班','韩城市','1231233213'],
    ['李华','三班','渭南市','1244444242'],
]

# 写入表头
i = 0

for j in title:
    sheet.write(0,i,j)
    i+=1


print(i)

#写入表内容
k = 1
for d in content:
    c = 0
    for x in d:
        sheet.write(k,c,x)
        c+=1
    k+=1

#保存
book.save("学生信息表.xlsx")

#https://www.cnblogs.com/xiao-apple36/p/9603499.html






