#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
import requests
from 任务.config import dingdan
from 任务.data import dingdan_duqu

# class dingdan_shouye_case_shouye(unittest.TestCase):
#
#     duqu = dingdan_duqu.dingdan_shuju()
#     shuju = duqu.duqu_shuju_shouye()
#
#     def test_shouye_1(self):
#
#         abc = dingdan.DingDan.jichu_shuju_chaxun()
#
#         self.assertEqual(abc['totalSize'],0)
#         self.assertEqual(abc['status'],1)
#         self.assertEqual(abc['errMsg'],'处理成功')



class dingdan_shouye_case_chaxun(unittest.TestCase):

    duqu = dingdan_duqu.dingdan_shuju()
    shuju = duqu.duqu_shuju_chaxun()

    def test_chaxun_1(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_chaxun(int(self.shuju[0][0]),int(self.shuju[0][1]))

        self.assertEqual(abc['totalSize'],0)
        self.assertEqual(abc['status'],1)
        self.assertEqual(abc['errMsg'],'处理成功')

    def test_chaxun_2(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_chaxun(int(self.shuju[1][0]),str(self.shuju[1][1]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')

    def test_chaxun_3(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_chaxun(str(self.shuju[2][0]),int(self.shuju[2][1]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')

    def test_chaxun_4(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_chaxun(int(self.shuju[3][0]),str(self.shuju[3][1]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')



class dingdan_shouye_case_dingdan(unittest.TestCase):

    duqu = dingdan_duqu.dingdan_shuju()
    shuju = duqu.duqu_shuju_dingdan()

    def test_dingdan_1(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_dingdan(int(self.shuju[0][0]),int(self.shuju[0][1]),str(self.shuju[0][2]))

        self.assertEqual(abc['totalSize'], 0)
        self.assertEqual(abc['status'], 1)
        self.assertEqual(abc['errMsg'], None)

    def test_dingdann_2(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_dingdan(int(self.shuju[1][0]),int(self.shuju[1][1]),str(self.shuju[1][2]))

        self.assertNotEqual(abc['totalSize'], 0)
        self.assertNotEqual(abc['status'], 1)
        self.assertNotEqual(abc['errMsg'], None)

    def test_dingdann_3(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_dingdan(int(self.shuju[2][0]),int(self.shuju[2][1]),str(self.shuju[2][2]))

        self.assertNotEqual(abc['totalSize'], 0)
        self.assertNotEqual(abc['status'], 1)
        self.assertNotEqual(abc['errMsg'], None)

    def test_dingdann_4(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_dingdan(str(self.shuju[3][0]),int(self.shuju[3][1]),str(self.shuju[3][2]))

        self.assertNotEqual(abc['totalSize'], 0)
        self.assertNotEqual(abc['status'], 1)
        self.assertNotEqual(abc['errMsg'], None)



class dingdan_shouye_case_peijian(unittest.TestCase):

    duqu = dingdan_duqu.dingdan_shuju()
    shuju = duqu.duqu_shuju_peijian()

    def test_peijian_1(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_peijian(int(self.shuju[0][0]))

        self.assertEqual(abc['totalSize'],0)
        self.assertEqual(abc['status'],1)
        self.assertEqual(abc['errMsg'],'处理成功')

    def test_peijian_2(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_peijian(str(self.shuju[1][0]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')

    def test_peijian_3(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_peijian(str(self.shuju[2][0]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')

    def test_peijian_4(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_peijian(int(self.shuju[3][0]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')



class dingdan_shouye_case_yanqi(unittest.TestCase):

    duqu = dingdan_duqu.dingdan_shuju()
    shuju = duqu.duqu_shuju_yanqi()

    def test_yanqi_1(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_yanqi(str(self.shuju[0][0]),int(self.shuju[0][1]))

        self.assertEqual(abc['totalSize'],0)
        self.assertEqual(abc['status'],1)
        self.assertEqual(abc['errMsg'],'处理成功')

    def test_yanqi_2(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_yanqi(str(self.shuju[1][0]),str(self.shuju[1][1]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')

    def test_yanqi_3(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_yanqi(str(self.shuju[2][0]),int(self.shuju[2][1]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')

    def test_yanqi_4(self):

        aa = dingdan.DingDan()
        abc = aa.jichu_shuju_yanqi(str(self.shuju[3][0]),str(self.shuju[3][1]))

        self.assertNotEqual(abc['totalSize'],0)
        self.assertNotEqual(abc['status'],1)
        self.assertNotEqual(abc['errMsg'],'处理成功')



if __name__== '__main__':
    unittest.main()