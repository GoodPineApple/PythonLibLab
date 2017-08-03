# 다양한 workbook 관련 정보들을 확인할 수 있음.
# http://xlsxwriter.readthedocs.io/workbook.html
import xlsxwriter
# xml파일 workbook 생성
workbook = xlsxwriter.Workbook('filename.xlsx')

# sheet 추가
worksheet0 = workbook.add_worksheet()
worksheet1 = workbook.add_worksheet()            # Sheet2
worksheet2 = workbook.add_worksheet('Foglio2')  # Foglio2
worksheet3 = workbook.add_worksheet('Data')     # Data
worksheet4 = workbook.add_worksheet()           # Sheet5

# sheet에 정보 추가
worksheet0.write(0, 0, 'Hello Excel')            # Sheet1

# xml 파일 저장 종료
workbook.close()