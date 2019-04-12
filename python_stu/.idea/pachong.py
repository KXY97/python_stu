#!/usr/bin/python
#-*- coding:utf-8 -*-
# 爬虫
# 爬虫三部曲 1.分析网址发送请求 2.制定规则获取资源 3.保存
import requests
import re
class 糗事_Spider(object):
    def fasong(self,page):
        url='https://www.qiushibaike.com/textnew/{}/?s=5167695.format(page)'
        # url='https://www.qiushibaike.com/text/{}/.format(page)'
        # 伪装成浏览器
        # head={
        #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        # }
        head={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        # 发送请求
        xiangying=requests.get(url,headers=head)
        # 读取响应 1.text以字符串方式读取 2.content以字节方式读取(需要解码decode('utf-8'))
        html=xiangying.content.decode('utf-8')
        # 返回结果并赋值
        return html
    def guolv(self,abc):
        shuju=[]
        # 将正则表达式编译
        patt=re.compile(r'<div class="content">(.*?)</div>',re.S)
        # 将编译后的条件到字符串中去查找
        items=patt.findall(abc)
        for i in items:
            i=i.replace('<span>','').replace('<br/>','').replace('</span>','').replace('<span class="contentForAll">查看全文','').strip()
            shuju.append(i)
        return shuju
    def save(self,qwe):
        with open('b.txt','a',encoding='utf-8') as f:
            for i in qwe:
                f.write(i+'\n')

qiu=糗事_Spider()
html=qiu.fasong(page=1)
shuju=qiu.guolv(abc=html)
qiu.save(shuju)