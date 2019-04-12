from selenium import webdriver
from time import sleep
dr = webdriver.Firefox()
#处理浏览器窗口
dr.get('https://qzone.qq.com')
#获取当前窗口字符串(句柄)
print(dr.current_window_handle)
sleep(2)
#处理框架 iframe(窗口)
#dr.switch_to_frame() 框架的ID或者name或者先定位
dr.switch_to.frame('login_frame')#切换到某一个框架
dr.switch_to.default_content()#回到最开始的页面上
dr.switch_to.parent_frame()#回到父框架
dr.find_element_by_id('switcher_plogin').click()
sleep(2)
#获取所有窗口的句柄
qq=dr.window_handles
#切换句柄
dr.switch_to.window(qq[-1])
dr.find_element_by_id('u').send_keys(1872123622)
sleep(2)
dr.find_element_by_id('p').send_keys('13782826564yy')
sleep(2)
dr.find_element_by_id('login_button').click()