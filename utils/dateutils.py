import time


class DateUtils:
    def __init__(self):
        pass

    @staticmethod
    def str_to_timestamp(date_str, date_format):
        return time.mktime(time.strptime(date_str, date_format))

    @staticmethod
    def timestamp_to_str(timestamp, date_format):
        return time.strftime(date_format, time.localtime(timestamp))

    @staticmethod
    def parse_new_date_str(date_str, date_format, offset_seconds):
        # 将指定格式的时间字符串转换成时间戳
        timestamp = time.mktime(time.strptime(date_str, date_format))
        # 将新的时间戳转换成字符串
        return time.strftime(date_format, time.localtime(timestamp + offset_seconds))

    @staticmethod
    def get_now_date_str(date_format):
        return time.strftime(date_format, time.localtime(time.time()))

    @staticmethod
    def get_now_timestamp(date_format):
        return time.time()


if __name__ == '__main__':
    time_str = DateUtils.parse_new_date_str('20061008', '%Y%m%d', 86400)
