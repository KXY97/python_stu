#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
class dingdan_shuju(object):

    def duqu_shuju_shouye(self):

        shuju = []
        f = xlrd.open_workbook('d:\python文件\任务\data\chaxun.xlsx')
        sheet = f.sheets()[0]
        num = sheet.nrows

        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))

        return shuju

    def duqu_shuju_chaxun(self):

        shuju = []
        f = xlrd.open_workbook('d:\python文件\任务\data\chaxun.xlsx')
        sheet = f.sheets()[1]
        num = sheet.nrows

        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))

        return shuju

    def duqu_shuju_dingdan(self):

        shuju = []
        f = xlrd.open_workbook('d:\python文件\任务\data\chaxun.xlsx')
        sheet = f.sheets()[2]
        num = sheet.nrows

        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))

        return shuju

    def duqu_shuju_peijian(self):

        shuju = []
        f = xlrd.open_workbook('d:\python文件\任务\data\chaxun.xlsx')
        sheet = f.sheets()[3]
        num = sheet.nrows

        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))

        return shuju

    def duqu_shuju_yanqi(self):

        shuju = []
        f = xlrd.open_workbook('d:\python文件\任务\data\chaxun.xlsx')
        sheet = f.sheets()[4]
        num = sheet.nrows

        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))

        return shuju

if __name__== '__main__':
    ss = dingdan_shuju()
    q = ss.duqu_shuju_shouye()
    a = ss.duqu_shuju_chaxun()
    b = ss.duqu_shuju_dingdan()
    c = ss.duqu_shuju_peijian()
    d = ss.duqu_shuju_yanqi()
    print(q)
    print(a)
    print(b)
    print(c)
    print(d)