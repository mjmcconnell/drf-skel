# local imports
import logging
import sys

# third-party imports
import json_logging


json_logging.ENABLE_JSON_LOGGING = True
json_logging.init()

logger = logging.getLogger("drf")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))
