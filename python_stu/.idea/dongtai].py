#!/usr/bin/python
#-*- coding:utf-8 -*-
import json
import requests
import re
class zhilian(object):
    def qing(self):
        url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.59128518&x-zp-page-request-id=41a87bc9f17449e2bb76f56b097d3963-1550653249699-349022'
        head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        fa = requests.get(url, headers=head)
        html = fa.content.decode('utf-8')
        html=json.load(html)
        return html
    def guolv(self):
