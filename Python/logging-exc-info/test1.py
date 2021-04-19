import logging

logger = logging.getLogger(__name__)

try:
    x = 1/0
except Exception:
    logger.error("error 1")
try:
    x = 1/0
except Exception:
    logger.error("error 2", exc_info=True)

