import numpy as np
import pandas as pd
import time
import sys
import matplotlib.pyplot as plt

col_temp=[]
col_ice_pay =[]
args = sys.argv
param = args[1]
print('指定パラメータ = ' + param)
# print(type(param))
project_id = 'bustling-bay-273908'
query = 'select high_temp,ice_payment from test_koshida.weather_ice_pay_tab order by high_temp'
data_frame = pd.read_gbq(query, project_id)

# print(data_frame.head())

#件数確認カウンタ
dcnt = 0
#折れ線
if param[0] == '1':
    # print('test')
    plt.plot(data_frame.high_temp, data_frame.ice_payment, color=(0,0,1),label='ice_sales')
    # plt.show()
    if len(param) > 1:
        param = param[1:]
if param[0] == '2':
    plt.scatter(data_frame.high_temp, data_frame.ice_payment, s=5, marker="o", c="red", linewidth=1)
    if len(param) > 1:
        param = param[1:]
# #近似直線の作成(直線は1次関数なので引数は1、曲線は2)
if param[0] == '3':
    reg_line_temp = np.polyfit(data_frame.high_temp, data_frame.ice_payment,2)
    reg_line = np.poly1d(reg_line_temp)(data_frame.high_temp,)
    plt.plot(data_frame.high_temp,reg_line,'--',color=(0,1,0))
    if len(param) > 1:
        param = param[1:]
if param[0] == '4':
    reg_line_temp = np.polyfit(data_frame.high_temp, data_frame.ice_payment,1)
    reg_line = np.poly1d(reg_line_temp)(data_frame.high_temp,)
    plt.plot(data_frame.high_temp,reg_line,'--',color=(1,1,0))
    if len(param) > 1:
        param = param[1:]
if param[0] == '5':
    plt.hist(data_frame.high_temp)
plt.legend()
plt.show()
print('end')
