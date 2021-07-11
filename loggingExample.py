import logging
logging.basicConfig(filename="E:\\pythonProject\\pawanOnlineSeleniumPython\\test1.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p',
                    #level=logging.DEBUG >> 1st way
                    )

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("Debug message")
logging.info("info mesg")
logging.warning("warn msg")
logging.error("eror msg")
logging.critical("critical msg")

