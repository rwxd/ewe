import logging
from os import getenv

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger('ewe')
logger.addHandler(stream_handler)

log_level = logging.getLevelName(getenv('LOG_LEVEL') or 'WARNING')
logger.setLevel(log_level)
