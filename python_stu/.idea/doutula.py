#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
import os
class dou(object):
    def fasong(self,page):
        url = 'https://www.doutula.com/article/list/?page={}'.format(page)
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        xiang = requests.get(url, headers=head)
        html = xiang.content.decode('utf-8')
        return html

    def guolv(self,abc):
        patt = re.compile(r'</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
        items = patt.findall(abc)

        zutu=[]
        for i in items:
            pat = re.compile(r'href="(.*?)" class')
            ite = pat.findall(i)
            zutu.append(ite)
        zu=zutu[0]

        mingzi=[]
        for j in items:
            pa = re.compile(r'<div class="random_title">(.*?)<div class="date">')
            it = pa.findall(j)
            mingzi.append(it)
        ming=mingzi[0]

        dantu=[]
        for q in zutu[0]:
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
            }
            xiang = requests.get(q, headers=head)
            html = xiang.content.decode('utf-8')
            p = re.compile(r"this.src='(.*?)'")
            t = p.findall(html)
            dantu.append(t)

        for e in ming:
            os.mkdir(r'D:\python文件\.idea\表情\{}'.format(e))

        for p,r in enumerate(dantu):
            os.chdir(r'D:\python文件\.idea\表情\{}'.format(ming[p]))
            for o in r:
                res=requests.get(o)
                ht=res.content
                if '.gif' in o:
                    with open('{}.gif'.format(p),'wb') as f:
                        f.write(ht)
                        p+=1
                else:
                    with open('{}.jpg'.format(p),'wb') as f:
                        f.write(ht)
                        p+=1
a=dou()
for z in range(1,11):
    b=a.fasong(z)
    a.guolv(b)