#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re

class 爬图():

    def qingqiu(self,page):
        url='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
        head={
            'User - Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        res=requests.get(url=url,headers=head)
        html=res.content.decode('utf-8')
        return html

    def guolv(self,abc):
        shuju=[]
        ab=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
        item=ab.findall(abc)
        for j in item:
            patt=re.compile('src="(.*?)"',re.S)
            hhh=patt.findall(j)
            shuju.append(hhh[0])
        return shuju
        # print(ab)
        # pt = re.compile(r'<div class="thumb">(.*?)</a>', re.S)
        # items = pt.findall(abc)
        # for i in items:
        #     tp = re.compile(r'src="(.*?)"', re.S)
        #     ss = tp.findall(i)
        #     shuju.append(ss[0])

    def save(self,qwe):
        # 任何图片都是二进制，请求图片的网址，得到图片的源码
        for k,i in enumerate(qwe):
            res=requests.get('https:'+i)
            ht=res.content
            with open('{}.jpg'.format(k),'wb') as f:
                f.write(ht)

a=爬图()
cc=[]
for q in range(1,3):
    shuju=a.guolv(a.qingqiu(q))
    cc.extend(shuju)
a.save(cc)
