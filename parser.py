# https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
import requests
from bs4 import BeautifulSoup

# HTTP GEt Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

# HTML 소스 가져오기
html = req.text

# HTTP Header 가져오기
header = req.headers

# HTTP Status 가져오기 (200 : 정상)
status = req.status_code

# HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok

# BeautifulSoup으로 html소스를 python 객체로 변환
# 첫 인자는 html소스코드, 두번째 인자는 어떤 parser를 이용할지 명시
# 이 글에서는 python 내장 html.parser를 이용
soup = BeautifulSoup(html, 'html.parser')

# soup에서 지정한 선택자를 list로 리턴
my_titles = soup.select(
    'h3 > a'
)

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

# print(html)
# print(header)
# print(status)
# print(is_ok)
