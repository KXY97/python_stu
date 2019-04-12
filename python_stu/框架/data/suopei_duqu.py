#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
class suopei_shuju(object):

    def duqu_jichu(self):
        shuju = []
        f = xlrd.open_workbook(r'D:\python文件\框架\data\suopei.xlsx')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

if __name__== '__main__':
    ss = suopei_shuju()
    a = ss.duqu_jichu()
    print(a)