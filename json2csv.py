from selenium import webdriver
# 引入Keys类包 发起键盘操作
from selenium.webdriver.common.keys import Keys
import time
import requests

driver = webdriver.Chrome()
# 访问百度
driver.get('http://www.baidu.com')

# 输入框输入内容
a = driver.find_element_by_id('kw').send_keys('python')
# 3s
time.sleep(3)
b = requests.get(a)
print(b)