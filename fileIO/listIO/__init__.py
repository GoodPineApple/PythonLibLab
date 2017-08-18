# https://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python
import simplejson

list = [['조석', '마음의소리', '에피소드', 'null', 'null', 'http://comic.naver.com/webtoon/list.nhn?titleId=20853', '연재중', 'null','null', '9.85', 'null','http://thumb.comic.naver.net/webtoon/20853/thumbnail/thumbnail_title_20853_83x90.gif'],
                          ['자까', '대학일기', '에피소드', 'null', 'null', 'http://comic.naver.com/webtoon/list.nhn?titleId=679519', '연재중', 'null','null', '9.96', 'null','http://thumb.comic.naver.net/webtoon/679519/thumbnail/title_thumbnail_20160601180804_t83x90.jpg'],
                          ['곽백수', '트라우마', '에피소드', 'null', '바로 이 녀석, 웽 Wooeng의 소행이었다.', 'http://comic.naver.com/webtoon/list.nhn?titleId=22052', '완결', 'null','null', '9.91', 'null','http://thumb.comic.naver.net/webtoon/22052/thumbnail/thumbnail_title_22052_83x90.gif'],
                          ['비브라토', '작가 아이작의 기묘한 이야기', '미스터리', '', '악마를 만난 작가 이야기','http://webtoon.daum.net/webtoon/view/16943', '연재중', '', '20170612', 10.0, '','http://t1.daumcdn.net/cartoon/5310df4e37a2a26f6d1691f5ca54d5404894dcee'],
                          ['하이햇', '트리거', '미스터리', '', '달콤하고도 잔혹한 미궁 속에 갇힌 그들의 이야기 [로맨스 미스터리 스릴러]','http://webtoon.daum.net/webtoon/view/16909', '완결', '', '20170606', 10.0, '','http://t1.daumcdn.net/cartoon/3380a5999c0aa34f2a8b190697501dee9480f4bc']]

# read 참고
fw = open('../datas/list.txt', 'w')
simplejson.dump(list,fw)
fw.close()

# 'r'은 파일 내의 내용을 읽어온다.
# 상대경로로 대상파일을 설정
with open("../datas/list.txt") as f:
  filecontents = simplejson.load(f)
print(filecontents)