# 로깅 기본 동작 테스트 출처
# http://gyus.me/?p=418

import logging as log

# 기본설정level을 디버그로 설정.
log.basicConfig(level=log.DEBUG)

log.debug("디버그입니다.")
log.info("인포입니다.")
log.warning("warning입니다!!")
log.error("error입니다!!!!")
log.critical("심각한에러!!!!!!!!!!")

# 결과값
# DEBUG:root:디버그입니다.
# INFO:root:인포입니다.
# WARNING:root:warning입니다!!
# ERROR:root:error입니다!!!!
# CRITICAL:root:심각한에러!!!!!!!!!!