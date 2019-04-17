from utils.dbutils import DBUtils
import pandas as pd


def shibor_acquisition(pro_interface):

    connection = DBUtils()  # 获取连接
    connection.set_collection('shibor')
    last_data = connection.get_last_data()

    print(last_data)

    df = pro_interface.shibor(start_date='20060101', end_date='20061231')
    # 将数据按日期进行升序排列
    df.sort_values(by='date', inplace=True)

    connection.set_id_column('date')
    connection.df2mongo(df)
