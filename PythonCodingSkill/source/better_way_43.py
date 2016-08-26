# from threading import Lock
#
# lock = Lock()
# with lock:
#     print('Lock is held')
#
#
# lock.acquire()
# try:
#     print('Lock is held')
# finally:
#     lock.release()

import logging
from contextlib import contextmanager


def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


my_function()


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)
