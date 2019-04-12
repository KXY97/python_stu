from appium import webdriver
from time import sleep

def denglu(zhanghao,mima):

    desired = {
                    "device": "android",
                    "platformName": "Android",
                    "platformVersion": "5.1.1",
                    "deviceName": "127.0.0.1:62001",
                    "appPackage": "com.netease.cloudmusic",
                    "appActivity": ".activity.LoadingActivity",
                    "noReset": "True"
                    }

    dr = webdriver.Remote('http://localhost:4723/wd/hub',desired)
    sleep(15)

    dr.find_element_by_id('com.netease.cloudmusic:id/qc').click()
    sleep(2)

    dr.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('{}'.format(zhanghao))
    sleep(2)

    dr.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('{}'.format(mima))
    sleep(2)

    dr.find_element_by_id('com.netease.cloudmusic:id/qc').click()
    sleep(2)

    dr.quit()

    return dr

denglu()