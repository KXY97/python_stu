from appium import webdriver
from time import sleep


desired_caps = {'platformName':'Android',
#                'platformVersion':'5.1.1',
                'deviceName':'127.0.0.1:62001',
                'appPackage':'com.wayyue.shanzhen',
                'appActivity':'.view.main.SZMainActivity'
                }
dr = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
sleep(5)

dr.quit()