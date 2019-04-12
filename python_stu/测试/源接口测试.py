#接口，请求传参和结果对比
#http协议   request
#import requests
#url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#head = {
#    'Content-Type':'application/json',
#    'x-dealer-code':'2100150',
#    'x-position-code':'D_PO_1028',
#    'x-resource-code':'BASIC_DATA',
#    'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
#    'x-user-code':'djy0mx',
#    'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb',
#}
#body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
#res = requests.post(url,headers=head,data=body)
#mes = res.json()
###assert断言
###assert mes['data']['applicationType'][0]['name']=='多装'
##unittest单元测试框架
##主要是对用例进行管理和执行
##所有的用例行数，必须以test开头
#main是检测类中所有以test开头的函数
#执行顺序是比较test后面的字符，谁在前就先执行谁
#setup是在每次执行用例之前执行，初始化测试环境
#teardown是在每次执行用例之后执行，清理测试环境
#任何测试用例都要在相同的环境下执行
import requests
import unittest
class suopei(unittest.TestCase):
    def test_1(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type':'application/json',
                'x-dealer-code':'2100150',
                'x-position-code':'D_PO_1028',
                'x-resource-code':'BASIC_DATA',
                'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code':'djy0mx',
                'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb',
         }
        b = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res = requests.post(url,header=head,data=b)
        mes = res.json()
        self.assertEqual(mes['data']['applicationType'][0]['name']=='多装')
    def tset_2(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type': 'application/json',
                'x-dealer-code': '2100150',
                'x-position-code': 'D_PO_1028',
                'x-resource-code': 'BASIC_DATA',
                'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code': 'djy0mx',
                'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb',
                }
        b = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": qwert,"curPage": 1}'.encode(
            'utf-8')
        res = requests.post(url, header=head, data=d)
        mes = res.json()
        self.assertEqual(mes['data']['applicationType'][0]['name'] == '多装')
    def test_3(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {'Content-Type': 'application/json',
                'x-dealer-code': '2100150',
                'x-position-code': 'D_PO_1028',
                'x-resource-code': 'BASIC_DATA',
                'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code': 'djy0mx',
                'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb',
                }
        b = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
            'utf-8')
        res = requests.post(url, header=head, data=b)
        mes = res.json()
        self.assertEqual(mes['data']['applicationType'][0]['name'] == '多装')
if __name__=='__main__':
    unittest.main()