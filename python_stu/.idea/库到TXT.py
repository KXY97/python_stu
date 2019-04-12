#!/usr/bin/python
#-*- coding:utf-8 -*-
import pymysql
con = pymysql.connect(host='192.168.0.60',
                      port=3306,
                      user='root',
                      password='123456',
                      charset='utf8')
abc=con.cursor()
abc.execute('use python_k;')
abc.execute('select * from biao;')
a=abc.fetchall()
con.close()
with open(r'a.txt','w',encoding='utf-8') as f:
    for i in a:
        for j in i:
            if j == i[-1]:
                f.write(j)
            else:
                f.write(j+',')
        f.write('\n')
# 库-TXT

