import logging
import logging.handlers

# 로거 인스턴스를 만든다
logger = logging.getLogger('mylogger')

# 포매터를 만든다
fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

# 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
fileHandler = logging.FileHandler('/myLoggerFomatterTest.log')
streamHandler = logging.StreamHandler()

# 각 핸들러에 포매터를 지정한다.
fileHandler.setFormatter(fomatter)
streamHandler.setFormatter(fomatter)

# 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# 로거 인스턴스로 로그를 찍는다.
logger.setLevel(logging.DEBUG)
logger.debug("===========================")
logger.info("TEST START")
logger.warning("스트림으로 로그가 남아요~")
logger.error("파일로도 남으니 안심이죠~!")
logger.critical("치명적인 버그는 꼭 파일로 남기기도 하고 메일로 발송하세요!")
logger.debug("===========================")
logger.info("TEST END!")

# 결과값
# [DEBUG|fomatter.py:24] 2017-08-16 13:31:00,480 > ===========================
# [INFO|fomatter.py:25] 2017-08-16 13:31:00,480 > TEST START
# [WARNING|fomatter.py:26] 2017-08-16 13:31:00,481 > 스트림으로 로그가 남아요~
# [ERROR|fomatter.py:27] 2017-08-16 13:31:00,481 > 파일로도 남으니 안심이죠~!
# [CRITICAL|fomatter.py:28] 2017-08-16 13:31:00,481 > 치명적인 버그는 꼭 파일로 남기기도 하고 메일로 발송하세요!
# [DEBUG|fomatter.py:29] 2017-08-16 13:31:00,482 > ===========================
# [INFO|fomatter.py:30] 2017-08-16 13:31:00,482 > TEST END!