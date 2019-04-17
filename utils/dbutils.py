import pymongo
import pandas as pd
import json
import logging


class DBUtils:

    def __init__(self, host_name='localhost', db_port=27017, db_name='stock_data_raw'):
        self.client = pymongo.MongoClient(host=host_name, port=db_port)
        self.database = self.client[db_name]
        self.collection = None
        self.id_column_name = None

    def set_collection(self, collection_name):
        self.collection = self.database[collection_name]

    def set_id_column(self, column_name):
        self.id_column_name = column_name

    def df2mongo(self, df, collection_name=None):
        # 如果传入集合名，则重新获取集合对象
        if collection_name is not None:
            self.set_collection(collection_name)
        if self.collection is None:
            print('没有设置数据集合')
            return
        if isinstance(df, pd.DataFrame):
            bson_data = self.df2bson(df)
            result = self.collection.insert_many(bson_data)
            if result.acknowledged:
                logging.info(f'{self.collection.name}: --- 成功插入{len(result.inserted_ids)}条数据 ---')
            else:
                logging.info(f'{self.collection.name}: 数据插入失败')

    @staticmethod
    def df2bson(df):
        return json.loads(df.T.to_json()).values()

    def get_last_data(self, collection_name=None):
        if collection_name is not None:
            self.set_collection(collection_name)
        if self.collection is None:
            print('没有设置数据集合')
            return
        return self.collection.find().sort('_id', pymongo.DESCENDING).limit(1)
