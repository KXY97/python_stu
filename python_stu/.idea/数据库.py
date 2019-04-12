#!/usr/bin/python
#-*- coding:utf-8 -*-
import pymysql
import xlrd
# 连接数据库，需要给数据库设置允许外部主机连接的权限
con = pymysql.connect(host='192.168.0.89',
                      port=3306,
                      user='root',
                      password='123456',
                      charset='utf8')
# 创建游标(控制器)
abc=con.cursor()
# 执行sql语句
# # abc.execute('create database python_k;')
# abc.execute('show databases')
# abc.execute('use python_k;')
# abc.execute('create table biaoge(name char(20),age int,sex char(10));')
# abc.execute('show tables')
# abc.execute('insert into biaoge values("Lucy",20,"woman"),("Mark",25,"man");')
# for i in range(3):
#     abc.execute('insert into biaoge values("{}",{},"{}");'.format(11,12,13))
# 提交：对数据库数据进行更改的时候   是由连接数据库的变量来提交
#     con.commit()
# abc.execute('select * from biaoge;')
# 任何结果都需要有容器接收
# 接收上一个sql语句的结果
# print(abc.fetchall())
# 接收上一个sql语句的结果，默认只接收第一行，在括号里写入数字几就接收多少行
# print(abc.fetchmany(3))
# 接收上一个sql语句的结果，每次只接收一行
# print(abc.fetchone())
# 需要断开数据库
book=xlrd.open_workbook('douban.xls')
sheet=book.sheet_by_name('0')
while True:
    a=input('')
    if 'insert into' in a:
        for i in range(1,sheet.nrows):
            name = sheet.cell(i,0).value
            dao = sheet.cell(i,1).value
            jian = sheet.cell(i,2).value
            ren = sheet.cell(i,3).value
            values=(name,dao,jian,ren)
            q = 'insert into biao values("{}","{}","{}","{}")'.format(values[0],values[1],values[2],values[3])
            abc.execute(q)
        continue
    elif a!= 'exit':
        abc.execute(a)
        print(abc.fetchall())
    else:
        break
con.close()
con.commit()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print(a.fetchall())
