import tushare as ts
from data_acquistion import shibor

# 设置token
ts.set_token('0f99a58cc679fa01b44daa1e2219d032b9c7830e79a12f02acb3edab')

# 初始化pro接口
pro = ts.pro_api()
shibor.shibor_acquisition(pro_interface=pro)
