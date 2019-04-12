#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:kong
import requests
import re
class douban(object):
    def qingqiu(self,page):
        url='https://www.zhihu.com/question/20687290'.format(page)
        head={
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        fasong=requests.get(url,head)
        duqu=fasong.content.decode('utf-8')+5
        return duqu
        print(duqu)
    def guolv(self,par):
        shuju=[]
        patt=re.compile(r'itemProp="text"><p>(.*?)<div class="ft">',re.S)
        find=patt.findall(par)
        for i in find:
            shuju.append(i)
        print(shuju)
        return shuju
    def save(self,shu):
        with open('d.txt','a',encoding='utf-8') as f:
            for i in shu:
                f.write(i+'\n')
bian=douban()
bian2=bian.qingqiu(page=2)
shuju=bian.guolv(par=bian2)
bian.save(shuju)
bian.qingqiu(page=2)