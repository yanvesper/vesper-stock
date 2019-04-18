from utils.dbutils import MongoConnection
from utils.dateutils import DateUtils
from utils.logutils import my_logging

# 设置日志logger
logger = my_logging.get_logger('data_acquisition_logger')


def shibor_acquisition(pro_interface):
    connection = MongoConnection()  # 获取连接
    connection.set_collection('shibor')

    last_data = connection.get_last_data()
    time_format = '%Y%m%d'  # 时间格式
    # 如果数据库为空，则从20061008开始获取数据，否则从最后一条数据的后一天开始
    start = DateUtils.str_to_timestamp('20061008', time_format)
    if last_data is not None:
        start = DateUtils.str_to_timestamp(last_data['_id'], time_format) + 86400
    end = DateUtils.get_now_timestamp(time_format)

    # 由于单次数据量受限为2000，在首次下载数据时需要分段操作
    # 分段采用粗略的2000天，而不是2000条数据
    while start < end:
        start_date = DateUtils.timestamp_to_str(start, time_format)
        if start + 172800000 < end:
            end_date = DateUtils.timestamp_to_str(start + 172800000, time_format)
            start += 172886400
        else:
            end_date = DateUtils.timestamp_to_str(end, time_format)
            start = end

        # 获取数据并存入数据库
        df = pro_interface.shibor(start_date=start_date, end_date=end_date)
        # 将数据按日期进行升序排列
        df.sort_values(by='date', inplace=True)
        connection.set_id_column('date')
        connection.df2mongo(df)

    logger.info(f'[stock_data_raw/shibor]: --- 更新完成，最后数据时间: {DateUtils.timestamp_to_str(end, "%Y-%m-%d")} ---')
