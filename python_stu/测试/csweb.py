from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# dr = webdriver.Firefox()#定义使用浏览器
# dr.get('https://www.baidu.com')#打开网址
# sleep(2)
#dr.find_element_by_xpath()#xpath定位 路径定位 路径标记语言 xml可扩展性标记语言
#dr.find_element_by_css_selector()#通过css定位
#dr.find_elements_by_tag_name()#通过tag name定位 最不唯一 通常定位一组元素
#dr.find_element_by_partial_link_text().click()#通过标签的模糊文本定位
#dr.find_element_by_link_text('hao123').click()#通过文本定位
# dr.find_element_by_name('wd').send_keys(123)#通过name定位
# dr.find_element_by_class_name('s_ipt').send_keys(123)# 通过class_name定位
# dr.find_element_by_class_name('s_btn btn_btnhover').click()
# dr.find_element_by_id('kw').send_keys(123)通过标签的ID属性定位
# dr.find_element_by_id('su').click()通过标签的ID属性定位
# dr.set_window_size(400,400)#设置浏览器大小
# sleep(2)
# dr.maximize_window()#设置全屏
# sleep(2)
# dr.set_window_position(400,100)
# sleep(2)
# dr.minimize_window()#设置最小化
# dr.get('https://www.jingdong.com')
# sleep(2)
# dr.back()#回退
# sleep(2)
# dr.forward()#前进
# sleep(2)
# print(dr.title)#获取网址的标题
# print(dr.current_url)#获取打开网页的网址
# dr.quit()#关闭浏览器
# dr.close()#关闭浏览器断开连接
#模拟鼠标的操作
dr = webdriver.Firefox()
dr.get('https://www.jd.com')
sleep(2)
w = dr.find_element_by_id('J_cate').find_elements_by_tag_name('li')
print(w)
for i in w:
    #控制鼠标来移动到元素的位置上            执行
    ActionChains(dr).move_to_element(i).perform()
    sleep(2)