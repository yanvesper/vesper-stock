import pymongo
import pandas as pd
import json
from utils.logutils import my_logging

# 设置日志logger
logger = my_logging.get_logger('data_acquisition_logger')


class DBUtils:

    def __init__(self, host_name='localhost', db_port=27017, db_name='stock_data_raw'):
        self.client = pymongo.MongoClient(host=host_name, port=db_port)
        self.database = self.client[db_name]
        self.collection = None
        self.id_column_name = None

    def set_collection(self, collection_name):
        """设置数据集合"""
        self.collection = self.database[collection_name]

    def set_id_column(self, column_name):
        """设置作为_id的列名"""
        self.id_column_name = column_name

    def df2mongo(self, df, collection_name=None):
        """将dataframe格式的数据写入mongodb"""
        # 如果传入集合名，则重新获取集合对象
        if collection_name is not None:
            self.set_collection(collection_name)
        if self.collection is None:
            logger.debug('没有设置数据集合')
            return
        if isinstance(df, pd.DataFrame):
            bson_data = self.df2bson(df)
            result = self.collection.insert_many(bson_data)
            if result.acknowledged:
                logger.info(f'[{self.database.name}/{self.collection.name}]: --- 成功插入{len(result.inserted_ids)}条数据 ---')
            else:
                logger.info(f'[{self.database.name}/{self.collection.name}]: 数据插入失败')

    @staticmethod
    def df2bson(df):
        """将dataframe格式的数据转为bson格式"""
        return json.loads(df.T.to_json()).values()

    def get_last_data(self, collection_name=None):
        """获取指定集合中最后一条数据"""
        if collection_name is not None:
            self.set_collection(collection_name)
        if self.collection is None:
            print('没有设置数据集合')
            return
        return self.collection.find().sort('_id', pymongo.DESCENDING).limit(1)
