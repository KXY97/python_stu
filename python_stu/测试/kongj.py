import unittest
from selenium import webdriver
from time import sleep
class Lon(unittest.TestCase):

    def  setUp(self):
        self.dr=webdriver.Firefox()
        self.dr.get('https://qzone.qq.com')
    def  test_Login(self):
        self.dr.switch_to.frame('login_frame')
        self.dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="u"]').send_keys(1872123622)
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="p"]').send_keys('13782826564yy')
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
        self.assertEqual(self.dr.title,'[http://1872123622.qzone.qq.com]')
    def tearDown(self):
        self.dr.quit()
if __name__=='__main__':
    unittest.main()
