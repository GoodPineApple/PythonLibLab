# 출처: http://itissmart.tistory.com/49 [IT is Smart]

# read 참고
fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

# 'r'은 파일 내의 내용을 읽어온다.
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
