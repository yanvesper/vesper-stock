import logging
from logging import handlers


class Logger:
    log_level = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }  # 日志级别的关系映射

    def __init__(self):
        fmt = '%(asctime)s - %(levelname)s: %(message)s'

        self.logger = logging.getLogger("data")
        stream_handler = logging.StreamHandler()
