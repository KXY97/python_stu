#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
import requests
from 框架.config import suopei
from 框架.data import suopei_duqu

class suopei_case(unittest.TestCase):

    shuju = suopei_duqu.suopei_shuju()
    shuju123 = shuju.duqu_jichu()
    def test_1(self):
        aa = suopei.Suopei()
        asd = aa.jichu_shuju(int(self.shuju123[0][0]),int(self.shuju123[0][1]))
        self.assertEqual(asd['data']['applicationType'][0]['name'],'多装')

    def test_2(self):
        suo = suopei.Suopei()
        asd = suo.jichu_shuju(self.shuju123[1][0], int(self.shuju123[1][1]))
        self.assertEqual("get error", asd["message"])

    def test_3(self):
        suo = suopei.Suopei()
        asd = suo.jichu_shuju(int(self.shuju123[2][0]), self.shuju123[2][1])
        self.assertEqual("get error", asd["message"])
if __name__== '__main__':
    unittest.main()