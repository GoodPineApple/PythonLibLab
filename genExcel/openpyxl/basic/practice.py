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

# 2-1 시트에서 셀을 변수로 만들고
c = ws1.cell('A2')

# 2-2 아래처럼 각 셀에 대해 value 입력, font 설정 등을 할 수 있다.
c.value = "A2 Zone"
c.font = Font(name='Arial', size=14)
c.border = Border(left=Side(border_style="thin", color='FF000000'),
                  right=Side(border_style="thin", color='FF000000'),
                  top=Side(border_style="thin",color='FF000000'),
                  bottom=Side(border_style="thin", color='FF000000'))

# 3. row, colum 을 지정하여 셀을 변수로 리턴할 수 있다.
d = ws1.cell(row=2,column=2)
d.value = "(2,2)text"

# 같은 workbook에 새로운 시트를 추가할 때
ws2 = wb.create_sheet()

# 번호를 지정하면 아래 번호에 sheet를 추가한다.
# ws2 = wb.create_sheet(1)

# 새로운 시트의 이름은 Sheet2라고 한다.
ws2.title = "Sheet2"

# 저장
wb.save('example.xlsx')