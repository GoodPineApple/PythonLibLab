# 출처: http://itissmart.tistory.com/49 [IT is Smart]

# sample.txt를 생성한다.
# 'w'는 해당 파일명이 존재하면 내용을 초기화 후 open, 해당 파일명이 존재하지 않으면 새로 파일을 만들어서 open.
# 'a'는 기존 내용을 그대로 유지한 채로 open
fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

