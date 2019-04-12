#!/usr/bin/python
#-*- coding:utf-8 -*-
from 框架 import HTMLTestRunner
import unittest
from 框架.test.tes_suopei import suopei_case

def baogao_():
    suit = unittest.TestSuite
    dis = unittest.defaultTestLoader.discover(‪r'd:\python文件\框架\tes_suopei')

    for i in dis:
        suit.addTest(i)
    f = open('a.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='索赔测试报告', description='结果如下', tester='孔香尹')
    runner.run(suit)
    f.close()

if __name__== '__main__':
    baogao_()