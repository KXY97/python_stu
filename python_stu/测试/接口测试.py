#!/usr/bin/python
#-*- coding:utf-8 -*-

#接口，请求传参和结果对比
#http协议    requests

# import requests
# import  unittest
# import  time
# # 产生测试报告的模块
# import  HTMLTestRunner
# class Suopei(unittest.TestCase):
#     def test_1(self):
#         self.assertNotEqual(123,456)
#     def test_2(self):
#         self.assertEqual(123,123)
#     def test_3(self):
#         self.assertEqual(456,456)
#     def test_4(self):
#         self.assertNotEqual(400,401)
# if __name__ == "__main__":
# #     创建一个测试套件
#     suit = unittest.TestSuite()
# #     添加测试用例
#     for i in range(1,5):
#         suit.addTest(Suopei("test_{}".format(i)))
#         now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
#         f=open("abc.html","wb")
#         # 内容写在那个文件里，给文件个名字，测试人是谁，结果如下
#         runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="索赔测试报告",tester="阿萨德",description="结果如下")
#         runner.run(suit)
#         f.close()

# 面向对象
# 所有的用例函数，必须test开头
# class suopei(unittest.TestCase):
#     # 初始化测试环境
#     def setUp(self):
#     #  是在每次执行用例之前执行
#         print("hello")
# #setUP/tearDown：任何测试用例都要保证在相同的环境下执行
#     # 清理测试环境
#     def tearDown(self):
#     #     是在每次用例结束之后执行
#         print("world")
#
#
#
#     def test_1(self):
#         url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#         head = {
#             "Content-Type":"application/json",
#             "x-dealer-code":"2100150",
#             "x-position-code":"D_PO_1028",
#             "x-resource-code":"BASIC_DATA",
#             "x-track-code":"4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#            "x-user-code":"djy0mx",
#            "x-access-token":"0da5606a534fa727dfd7f502df38be65"
#         }
#         body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
#         res = requests.post(url,headers=head,data=body)
#         mes = res.json()
#         self.assertEqual(mes["data"]["applicationType"][0]["name"],"多装")
#
#     def tset_2(self):
#         url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#         head = {
#             "Content-Type": "application/json",
#             "x-dealer-code": "2100150",
#             "x-position-code": "D_PO_1028",
#             "x-resource-code": "BASIC_DATA",
#             "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#             "x-user-code": "djy0mx",
#             "x-access-token": "0da5606a534fa727dfd7f502df38be65"
#         }
#         b = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": qwe}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=b)
#         mes = res.json()
#         self.assertNotEqual(mes["data"]["applicationType"][0]["name"], "多装")
#
#     def test_3(self):
#         url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#         head = {
#             "Content-Type": "application/json",
#             "x-dealer-code": "2100150",
#             "x-position-code": "D_PO_1028",
#             "x-resource-code": "BASIC_DATA",
#             "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#             "x-user-code": "djy0mx",
#             "x-access-token": "0da5606a534fa727dfd7f502df38be65"
#         }
#         b = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=b)
#         mes = res.json()
#         self.assertEqual(mes["data"]["applicationType"][0]["value"], "1")
#
#     def test_4(self):
#         url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#         head = {
#             "Content-Type": "application/json",
#             "x-dealer-code": "2100150",
#             "x-position-code": "D_PO_1028",
#             "x-resource-code": "BASIC_DATA",
#             "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#             "x-user-code": "djy0mx",
#             "x-access-token": "0da5606a534fa727dfd7f502df38be65"
#         }
#         b = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": qwe}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=b)
#         mes = res.json()
#         self.assertNotEqual(mes["data"]["applicationType"][0]["value"], "1")
#
#
# if __name__=="__main__":
#     #检测类中所有以test开头的函数
#     # 比较tset后面的字符，谁在前就先执行谁
#     unittest.main()






# url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
# head = {
#     "Content-Type":"application/json",
#     "x-dealer-code":"2100150",
#     "x-position-code":"D_PO_1028",
#     "x-resource-code":"BASIC_DATA",
#     "x-track-code":"4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#    "x-user-code":"djy0mx",
#    "x-access-token":"0da5606a534fa727dfd7f502df38be65"
# }
#
# body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
# res = requests.post(url,headers=head,data=body)
# mes =res.json()
# # mes= json.loads(res.text)(需要用到JSON模块)
# assert (mes["data"]["applicationType"][0]["name"])  =="多装"
# assert (mes["data"]["applicationType"][0]["value"])  =="1"

# unittest  #单元测试框架
#主要对用例进行管理和执行
