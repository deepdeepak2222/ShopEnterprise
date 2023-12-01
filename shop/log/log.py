"""
Log utils
"""
import logging


def log_err(msg):
    """
    Log errors
    """
    logging.log(logging.ERROR, msg)


def log_info(msg):
    """
    Log information
    """
    logging.log(logging.INFO, msg)
