#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
class DingDan(object):

    def jichu_shuju_shouye(self):

        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage'

        head = {
            "Content-Type": "application/json",
            "x-dealer-code": "2100005",
            "x-position-code": "D_PO_1028",
            "x-resource-code": "pol4s_partOrder_orderHomePage",
            "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            "x-user-code": "dhxc1u",
            "x-access-token": "da05ee37e5676e7b27972b2892e0fdeb"
        }

        res = requests.post(url,headers=head)

        return res.json()

    def jichu_shuju_chaxun(self,a,b):

        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList'

        head = {
            "Content-Type": "application/json",
            "x-dealer-code": "2100001",
            "x-position-code": "D_PO_1028",
            "x-resource-code": "pol4s_partOrder_orderList",
            "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            "x-user-code": "dhxc1u",
            "x-access-token": "da05ee37e5676e7b27972b2892e0fdeb"
        }

        bod = '{"pageNum": %s,"pageSize": %s,"queryTerms": {"orderType": "","orderStatus": "","orderDelayFlag": "","orderNo": "","startReportDate": "","endReportDate": ""}}' %(a,b)
        bod = bod.encode('utf-8')

        res = requests.post(url,headers=head,data=bod)

        return res.json()

    def jichu_shuju_dingdan(self,a,b,c):

        url = 'https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'

        head = {
            "Content-Type": "application/json",
            "x-dealer-code": "2100001",
            "x-position-code": "D_PO_1028",
            "x-resource-code": "pol4s_partOrderSearch_partOrderDetailSearch",
            "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            "x-user-code": "dhxc1u",
            "x-access-token": "da05ee37e5676e7b27972b2892e0fdeb"
        }

        bod = '{"pageNum":%s,"pgeSize":%s,"queryTerms":{"orderNo":"%s"}}'%(a,b,c)
        bod = bod.encode('utf-8')

        res = requests.post(url, headers=head, data=bod)

        return res.json()

    def jichu_shuju_peijian(self,a):

        url = 'https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'

        head = {
                "Content-Type":"application/json",
                "x-dealer-code":"2100001",
                "x-position-code":"D_PO_1028",
                "x-resource-code":"pol4s_partOrder_orderPartDetail",
                "x-track-code":"4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                "x-user-code":"dhxc1u",
                "x-access-token":"da05ee37e5676e7b27972b2892e0fdeb"
                }

        bod = '{"partOrderItemId": %s}' %(a)
        bod = bod.encode('utf-8')

        res = requests.post(url, headers=head, data=bod)

        return res.json()

    def jichu_shuju_yanqi(self,a,b):

        url = 'https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'

        head = {
                "Content-Type":"application/json",
                "x-dealer-code":"2100001",
                "x-position-code":"D_PO_1028",
                "x-resource-code":"pol4s_partOrder_orderPartDetail",
                "x-track-code":"4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                "x-user-code":"dhxc1u",
                "x-access-token":"da05ee37e5676e7b27972b2892e0fdeb"
                }

        bod = '{"queryTerms":{"orderNo": %s},"partCode": %s}' %(a,b)
        bod = bod.encode('utf-8')

        res = requests.post(url,headers=head,data=bod)

        return res.json()

if __name__=='__main__':
    pp = DingDan()
    sy = pp.jichu_shuju_shouye()
    cx = pp.jichu_shuju_chaxun(1,10)
    dd = pp.jichu_shuju_dingdan(1,10,'V2100880181219390')
    pj = pp.jichu_shuju_peijian(3108)
    yq = pp.jichu_shuju_yanqi('E2100305040604900',5483887)

    print(sy)
    print(cx)
    print(dd)
    print(pj)
    print(yq)