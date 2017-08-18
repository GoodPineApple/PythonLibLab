# 출처: http://itissmart.tistory.com/49 [IT is Smart]

# read 참고
fw = open('../datas/sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

# 'r'은 파일 내의 내용을 읽어온다.
# 상대경로로 대상파일을 설정
fr = open('../datas/sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
