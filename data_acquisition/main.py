import tushare as ts
from data_acquisition.macro_economy import ecomony

# 设置token
ts.set_token('0f99a58cc679fa01b44daa1e2219d032b9c7830e79a12f02acb3edab')

# 初始化pro接口
pro = ts.pro_api()
ecomony.economy_acquisition(pro_interface=pro)
