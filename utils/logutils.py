import yaml
import logging.handlers
import logging.config
import os


class LogUtils:
    def __init__(self):
        config_path = '../config/logging.yml'

        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = yaml.load(f, Loader=yaml.FullLoader)  # 读取配置，需要指定loader
                logging.config.dictConfig(config)  # 加载配置

    @staticmethod
    def get_logger(logger_name=None):
        return logging.root if logger_name is None else logging.getLogger(logger_name)


my_logging = LogUtils()

if __name__ == '__main__':
    logger = my_logging.get_logger('data_acquisition_logger')
    logger.error('error1')
    logger.info('info1')
