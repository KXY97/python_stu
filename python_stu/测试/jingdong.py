from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui #智能等待 设置一个最大等待时间，检测到某个元素出现，就不会继续等待
dr = webdriver.Firefox()
dr.get('http://www.jd.com')
w = dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/h1/a')
a= w.get_attribute('href')
print(a)
# unit = ui.WebDriverWait(dr,10)
# #直到定位的元素出现，就不等待了
# unit.until(lambda dr:dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/h1/a'))
# print('hello')

# for i in range(1,10000,2000):
#     js = 'var q=doucument.decumentElement.scrollTop={}'.format(i)#执行Javascript语句
#     dr.execute_script(js)
#     sleep(2)
# ww = dr.switch_to.alert#切换到弹出框
# print(ww.text)
# ww.accept()#点击确定 获取弹出框上的内容
# ww.dismiss()#点击取消
# ww.send_keys('')#点击输入
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul[2]/li[1]/a[1]').click()
# sleep(1)
# dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
# sleep(1)
# dr.find_element_by_id('loginname').send_keys('123456')
# sleep(1)
# dr.find_element_by_id('nloginpwd').send_keys('123546')
# sleep(1)
# dr.find_element_by_id('loginsubmit').click()
# start = dr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')
#drag_and_drop(起始位置,结束位置)
#drag_and_drop_by_offset(起始位置，x轴坐标，y轴坐标)
# ActionChains(dr).drag_and_drop_by_offset(start,68,0).perform()
# dr.find_element_by_id('key').send_keys('python')
# sleep(1)
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
# sleep(1)
# dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()
# sleep(1)
# yy = dr.window_handles
# print(yy)
# dr.switch_to.window(yy[-2])
# dr.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/a').click()


