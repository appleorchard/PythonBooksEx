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

print('--------------------------------')

with open('tmp/my_output.txt', 'w') as f:
    f.write("This is some data! ")


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

print('--------------------------------')
with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not pprint')

logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')
