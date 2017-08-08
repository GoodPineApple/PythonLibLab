# openpyxl pip통해 설치
# pip install openpyxl

from openpyxl import Workbook
from openpyxl.styles import Font, Side, Border

# Workbook 생성
wb = Workbook()

# Workbook을 생성하면 적어도 하나의 워크시트를 생성한다.
ws1 = wb.active
ws1.title = "Example1"

# 1. 시트의 행렬의 번호를 입력하여 Text 입력이 가능
ws1['A1'] = "A1_Test Text"