#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
import xlwt
f = xlrd.open_workbook('douban.xls')
sheet = f.sheets()[0]
aa = sheet.nrows
with open(r'a.txt','w',encoding='utf-8') as c:
    while True:
        for j in range(aa):
            x = ','.join(sheet.row_values(j))
            if x[-1] == ',':
                x = x.split(',')
                x.pop(-1)
                x = ','.join(x)
                c.write(x+'\n')
            elif j == (sheet.nrows-1):
                c.write(x)