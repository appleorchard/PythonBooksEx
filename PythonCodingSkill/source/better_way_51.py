import logging
from pprint import pprint
from sys import stdout as STDOUT

# try:
#     def determine_weight(volume, density):
#         if density <= 0:
#             raise ValueError('Density must be positive')
#
#
#     determine_weight(1, 0)
# except:
#     logging.exception('Expected')
#
# else:
#     assert False


class Error(Exception):
    """Base-class for all exceptions raised by this module."""


class InvalidDensityError(Error):
    """There was a problem with a provided density value."""


class my_module(object):
    Error = Error
    InvalidDensityError = InvalidDensityError

    @staticmethod
    def determine_weight(volume, density):
        if density <= 0:
            raise InvalidDensityError('Density must be positive')


# try:
#     weight = my_module.determine_weight(1, -1)
#     assert False
# except my_module.Error as e:
#     logging.error("Unexpected error: %s", e)

weight = 5
try:
    weight = my_module.determine_weight(1, -1)
    assert False
except my_module.InvalidDensityError:
    weight = 0
except my_module.Error as e:
    logging.error('Bug in the calling code: %s', e)

assert weight == 0

