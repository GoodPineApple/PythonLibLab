# 로깅 기본 동작 테스트 출처
# http://gyus.me/?p=418

import logging as log

# 기본설정level을 디버그로 설정.
log.basicConfig(filename="./test.log",level=log.DEBUG)

log.info("==================================")
log.info("파일에 로그정보를 남깁니다~~~")
log.info("==================================")
log.debug("디버그입니다.")
log.info("인포입니다.")
log.warning("warning입니다!!")
log.error("error입니다!!!!")
log.critical("심각한에러!!!!!!!!!!")
