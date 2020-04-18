import numpy as np
import pandas as pd
import time
import sys
import matplotlib.pyplot as plt

col_temp=[]
col_ice_pay =[]
args = sys.argv
param = args[1]
print('パラメータ=' + param)

project_id = 'bustling-bay-273908'
query = 'select high_temp,ice_payment from test_koshida.weather_ice_pay_tab order by high_temp'
data_frame = pd.read_gbq(query, project_id)

print(data_frame.head())

#件数確認カウンタ
dcnt = 0
#折れ線
# if param == 1:
    plt.plot(data_frame.high_temp, data_frame.ice_payment, color=(0,0,1))
    # plt.show()
# elif param == 2:
    plt.scatter(data_frame.high_temp, data_frame.ice_payment, s=5, marker="o", c="red", linewidth=1)
# #近似直線の作成(直線は1次関数なので引数は1、曲線は2)
# elif param == 3:
    reg_line_temp = np.polyfit(data_frame.high_temp, data_frame.ice_payment,2)
    reg_line = np.poly1d(reg_line_temp)(data_frame.high_temp,)
    plt.plot(data_frame.high_temp,reg_line,'--',color=(0,1,0))
# elif param == 4:
    reg_line_temp = np.polyfit(data_frame.high_temp, data_frame.ice_payment,1)
    reg_line = np.poly1d(reg_line_temp)(data_frame.high_temp,)
    plt.plot(data_frame.high_temp,reg_line,'--',color=(0,1,0))
# elif param == 5:
    plt.hist(data_frame.high_temp)
plt.show()