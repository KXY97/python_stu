from appium import webdriver
from time import sleep


#表明基础信息
desired_caps = {'platformName':'Android',#所用平台
#                'platformVersion':'6.0',#平台版本
                'deviceName':'127.0.0.1:62001',
                'appPackage':'com.netease.cloudmusic',
                'appActivity':'.activity.LoadingActivity'
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)#客户端连接服务器
sleep(15)

driver.find_element_by_class_name('android.widget.ImageView').click()
sleep(3)

driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('13782826564')
sleep(3)

driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('13782826564.')
sleep(3)

driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()


driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
sleep(3)

aa =driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
sleep(3)


if aa == '恐龙让鸭梨':
    print('pass')
else:
    print('e')

driver.quit()