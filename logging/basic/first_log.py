# 로깅 기본 동작 테스트 출처
# http://gyus.me/?p=418

import logging as log

# 기본 로그 설정하지 않을 경우, 아래 코드들을 실행하면 log.info는 출력되지 않는다.
log.info("my first log info")
log.warning("my first log warn")
# 결과 : WARNING:root:my first log warn


