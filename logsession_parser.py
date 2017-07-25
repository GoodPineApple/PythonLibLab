import requests
from bs4 import BeautifulSoup as bs

# Session 생성, with 구문 안에 유지
# s = requests.Session()은 세션이 풀리는 경우가 있음
with requests.Session() as s:
    # HTTP GET Request: requests대신 Session을 사용한다.
    req = s.get('https://www.clien.net/service/')
    # HTML 소스 가져오기
    html = req.text
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok

    soup 

print(html)
print(header)
print(status)
print(is_ok)
