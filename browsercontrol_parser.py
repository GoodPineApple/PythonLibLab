# https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
from selenium import webdriver

# driver = webdriver.Chrome('D:\taemin\dev\python\croller\chapter01\chromedriver_win32\chromedriver')
driver = webdriver.Chrome('D:/taemin/dev/python/croller/chapter01/chromedriver_win32/chromedriver')
driver = webdriver.PhantomJS('D:/taemin/dev/python/croller/chapter01/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')

driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('mypassword1234')
test = driver.find_element_by_id('label_login_chk').text()
print(test)
# PhantomJS 자체적으로 soup역할을 할 수도 있음.

# 페이지의 단일 element에 접근하는 api,
# find_element_by_name(‘HTML_name’)
# find_element_by_id(‘HTML_id’)
# find_element_by_xpath(‘/html/body/some/xpath’)
# 페이지의 여러 elements에 접근하는 api 등이 있다.
# find_element_by_css_selector(‘#css > div.selector’)
# find_element_by_class_name(‘some_class_name’)
# find_element_by_tag_name(‘h1’)

