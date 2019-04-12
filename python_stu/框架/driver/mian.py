#!/usr/bin/python
#-*- coding:utf-8 -*-
from 框架 import HTMLTestRunner
from 框架.report.baogao import baogao_
def run(aa):
    baogao_(aa)
with open('回归.txt','r') as f:
    a = f.readlines()
    if len() == 1:
        run('*')
    else:
        run(a)