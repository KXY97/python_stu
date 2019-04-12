# from selenium import webdriver
# from time import sleep
# dr = webdriver.Firefox()
# dr.get('https://www.ctrip.com')
# sleep(2)
# wd = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in wd:
#     i.click()
#     sleep(2)

from selenium import webdriver
from time import sleep
dr = webdriver.Firefox()
dr.get('http://www.yrcti.edu.cn')
sleep(2)
wd = dr.find_elements_by_id('dropdown-toggle')