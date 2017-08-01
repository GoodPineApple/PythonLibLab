# 엑셀변환lib XlsxWriter 설치

# sudo easy_install XlsxWriter

import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()





