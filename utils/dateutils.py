import time


class DateUtils:
    def __init__(self):
        pass

    @staticmethod
    def parse_new_date_str(date_str, date_format, offset_seconds):
        # 将指定格式的时间字符串转换成时间戳
        timestamp = time.mktime(time.strptime(date_str, date_format))
        # 将新的时间戳转换成字符串
        return time.strftime(date_format, time.localtime(timestamp + offset_seconds))


if __name__ == '__main__':
    time = DateUtils.parse_new_date_str('20061008', '%Y%m%d', 86400)
    print(time)
