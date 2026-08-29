"""
logger.py
Sets up logging so every conversion and every error gets written
to app.log with a timestamp, instead of just printed and lost.
"""

import logging
import os

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app.log")


def get_logger():
    logger = logging.getLogger("currency_converter")
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers if get_logger() is called more than once
    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
