#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:kong
# b=a[::-1]
# print(b)
# a=input('请输入单词，以空格分开')
# b=a.split(' ')
# print(type(b))
# print(b)
# while True:
#     for j in b:
#         w=j[::1]
#         print(w)
#     for i in b:
#         c=i[::-1]
#         print(c)
#         g=list(c)
#         print(g)
#     break
#     # if w[]
# a=input('请输入')
# b=[]
# c=[]
# for d in a:
#     if d.isupper() == True:
#         b.append(1)
#     else:
#         b.append(0)
# print(b)
# e=list(a)
# e.reverse()
# print(e)
# for g in e:
#     if g.isupper() == True:
#         c.append(1)
#     else:
#         c.append(0)
# print(c)
# print(b[0::])
# print(c[0::])
# while True:
#         if b == c:
#             print(c)
#             break
#         else:
#             for h in range(len(b)):
#                 if int(b[h]) > int(c[h]):8
#                     print(c.upper())
#                 elif int(b[h]) < int(c[h]):
#                     print(c.swapcase())
#
#
# class aaaaa():
#     def __init__(self,n=123):
#         self.name=n
#     def hahaha(self):
#         print('在{}'.format(self.name))
#     def hehehe(self):
#         print('456')
# a=aaaaa('小eq')
# b=aaaaa('小wh')
# a.hahaha()
# b.hahaha()
#
#
#
# def hanshu(s,a1,a2=0):
#     c=''
#     for i in range(len(s)):
#         if i < a1:
#             c+=s[i]
#         elif i>=a1+a2:
#             c+=s[i]
#     print(c)
# hanshu('njikmkl',3,4)
#
#
# import math
# def isPrimeNumber(num):
#     i = 2
#     x = math.sqrt(num)
#     while i < x:
#         if num%i == 0:
#             return False
#         i += 1
#     return True
# n=6
# while n < 51:
#         for j in range(3,int(n/2)):
#             if isPrimeNumber(j) and isPrimeNumber(n-j):
#                 print '%s = %s + %s' % (n, j, n-j)
#     n+=2
#
#
# def sushu(n):
#     i=2
#     while i<=n:
#         if n%i==0:
#             break
#         i+=1
#     if i==n:
#         return True
#     for k in range(6,101,2):
#         if k%2==0:
#             i=1
#             while i<=k:
#                 j=k-i
#                 if sushu(i):
#                     if sushu(j) and i<=j:
#                         print('%d+%d=%d'%(i,j,B))
#                 i+=1
#         else:
#             print('no')
#
#
# 定义一个函数，接受三个参数，分别为字符串s、数值a1、数值a2，将字符串s从下标a1开始的a2个字符删除，并把结果返回。a2默认值为0
# def hanshu(s,a1,a2=0):
#     q=list(s)
#     w=[]
#     for i in range(len(q)):
#         if i < a1:
#             w.append(q[i])
#         elif i>=a1+a2:
#             w.append(q[i])
#     w=''.join(w)
#     return(w)
#
#
# 爬虫三部曲 1.分析网址发送请求 2.制定规则获取资源 3.保存
# import requests
# import re
# class 糗事_Spider(object):
#     def fasong(self,page):
#         url='https://www.qiushibaike.com/textnew/{}/?s=5167695.format(page)'
#         # url='https://www.qiushibaike.com/text/{}/.format(page)'
#         # 伪装成浏览器
#         # head={0
#         #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
#         # }
#         head={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
#         }
#         # 发送请求
#         xiangying=requests.get(url,headers=head)
#         # 读取响应 1.text以字符串方式读取 2.content以字节方式读取(需要解码decode('utf-8'))
#         html=xiangying.content.decode('utf-8')
#         # 返回结果并赋值
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         # 将正则表达式编译
#         patt=re.compile(r'<div class="content">(.*?)</div>',re.S)
#         # 将编译后的条件到字符串中去查找
#         items=patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','').replace('<br/>','').replace('</span>','').replace('<span class="contentForAll">查看全文','').strip()
#             shuju.append(i)
#         return shuju
#     def save(self,qwe):
#         with open('b.txt','a',encoding='utf-8') as f:
#             for i in qwe:
#                 f.write(i+'\n')
#
# qiu=糗事_Spider()
# html=qiu.fasong(page=1)
# shuju=qiu.guolv(abc=html)
# qiu.save(shuju)



# from time import *
# def getLastDay():
#     y = int(input("Please input year :"))
#     m = int(input("please input month :"))
#     d = int(input("Please input day :"))
#     s=0
#     mothday=[31,28,31,30,31,30,31,31,30,31,30,31]#一年中每个月的天数
#     month=mothday[m-1]#获取输入月份的天数
#     if d > mothday[m-1]:#判断输入日期是否大于该月天数
#         d=d-mothday[m-1]
#         m+=1
#         month=mothday[m-1]#输入天数大于当月天数后月份加一，重新计算新月天数
#     if m>12:
#         m=12
#     def runnian(y,s):
#         t=0
#         if (y%400)==0:
#             print("是闰年")
#             t=1
#             s+=1
#         elif (y%100)!=0 and (y%4)==0 :
#             print("是闰年")
#             t=1
#             s+=1
#         else :
#             print("不是闰年")
#             t=0
#             s=0
#         return t,s
#     t,s=runnian(y,s)
#     if m==2:
#         month= month + t
#     for i in range(0,m-1):
#         s= s+ int(mothday[i])
#     s=s+d
#     print(s)
# getLastDay()



# import datetime
# date_A= input('请输入日期（格式：yyyy-mm-dd）：')
# dayA= datetime.datetime.strptime(date_A, '%Y-%m-%d')
# dayB=datetime.timedelta(days=1)
# dayC=dayA-dayB
# print("输入日期的前一天为："+dayC.strftime('%Y-%m-%d'))



