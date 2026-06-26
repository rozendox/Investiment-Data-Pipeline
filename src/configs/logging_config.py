"""Configuration for loggin module"""

import os
import logging
from logging.handlers import TimedRotatingFileHandler


def config_logging():
    """Configure the logging module."""
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    log_format = os.getenv('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_date_format = os.getenv('LOG_DATE_FORMAT', '%d-%m-%Y %H:%M:%S')

    log_dir = os.getenv('LOG_DIR', f'{os.getcwd()}/logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'app.log')

    file_handler = TimedRotatingFileHandler(
        log_file, when='midnight', interval=1, backupCount=7, encoding='utf-8'
    )
    file_handler.setFormatter(logging.Formatter(fmt=log_format, datefmt=log_date_format))

    logging.basicConfig(level=log_level, format=log_format,
                        datefmt=log_date_format,
                        handlers=[logging.StreamHandler(), file_handler])