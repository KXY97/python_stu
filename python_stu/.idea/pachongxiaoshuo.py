#!/usr/bin/python
#-*- coding:utf-8 -*-
# import requests
# import re
# class xiaoshuo(object):
#     def qingqiu(self,page):
#         url='http://www.17k.com/chapter/2919690/36{}.html'.format(page)
#         head={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
#         }
#         xiangying = requests.get(url, headers=head)
#         html = xiangying.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         patt = re.compile(r'<div class="p">(.*?)<div class="author-say">', re.S)
#         items = patt.findall(abc)
#         return items
#     def save(self,qwe):
#         with open('c.txt', 'a', encoding='utf-8') as f:
#             for i in qwe:
#                 f.write(i + '\n')
# xiao=xiaoshuo()
# html=xiao.qingqiu(page=454711)
# shuju=xiao.guolv(abc=html)
# xiao.save(shuju)