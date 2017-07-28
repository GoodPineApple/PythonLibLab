# https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# “Chrome is being controlled by automated test software” notification hide.
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome('D:/taemin/dev/python/croller/chapter01/chromedriver_win32/chromedriver', chrome_options=chrome_options)
# driver = webdriver.PhantomJS('D:/taemin/dev/python/croller/chapter01/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')

driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://nid.naver.com/nidlogin.login')

# PhantomJS 자체적으로 soup역할을 할 수도 있음.
# 페이지의 단일 element에 접근하는 api,
# find_element_by_name(‘HTML_name’)
# find_element_by_id(‘HTML_id’)
# find_element_by_xpath(‘/html/body/some/xpath’)
# 페이지의 여러 elements에 접근하는 api 등이 있다.
# find_element_by_css_selector(‘#css > div.selector’)
# find_element_by_class_name(‘some_class_name’)
# find_element_by_tag_name(‘h1’)

driver.find_element_by_name('id').send_keys('taemin3000')
driver.find_element_by_name('pw').send_keys('s8549717')

# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# 내 블로그 들어가기
driver.get('http://taemin3000.blog.me/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('#title_1')
title = soup.select('title')
fraeset = soup.select('#mainFrame')

print(fraeset)
# print(title)
# print(title[0].text)
# print(soup)
# print(notices)
# print(notices[0].text)