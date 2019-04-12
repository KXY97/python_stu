#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:kong
import requests
import re
class douban(object):
    def qingqiu(self,page):
        url='https://movie.douban.com/top250?start={}&filter='.format(page)
        head={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        fasong=requests.get(url=url,headers=head)
        duqu=fasong.content.decode('utf-8')
        return duqu

    def guolv(self,par):
        shuju=[]
        patt=re.compile(r'<div class="info">(.*?)</p>',re.S)
        find=patt.findall(par)
        for i in find:
            aaa=re.compile(r'<span class="title">(.*?)</span>',re.S)
            bbb=aaa.findall(i)
            shuju.append(bbb)
        return shuju

    def save(self,shu):
        with open('d.txt','a',encoding='utf-8') as f:
            for i in shu:
                print(type(i))
                f.write(i+'\n')

a=douban()
b=a.guolv(a.qingqiu(0))
print(type(b))
a.save(b)