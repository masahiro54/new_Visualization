import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import time
import datetime
import math
from bigquery.errors import BigQueryTimeoutException

col_temp=[]
col_ice_pay =[]

conn = psycopg2.connect("dbname=trading_company host=localhost user=mkoshida password=powered3543")
cur = conn.cursor()
cur.execute("select high_temp,ice_payment from weather_ice_pay_veiw order by high_temp;")
#フェッチ開始前の時間取得
start = time.time()
#fetchallでデータを取得
rows = cur.fetchall()
#件数確認カウンタ
dcnt = 0

#print(rows[0][0])
#print(rows[0][1])
#データをフェッチ
for r in rows:
    col_temp.append(rows[dcnt][0])
    col_ice_pay.append(rows[dcnt][1])
    dcnt = dcnt + 1
    
#print(rows[1][1])

plt.plot(col_temp, col_ice_pay, color=(0,0,1))
plt.scatter(col_temp, col_ice_pay, s=5, marker="o", c="red", linewidth=1)
#近似直線の作成(直線は1次関数なので引数は1、曲線は2)
reg_line_temp = np.polyfit(col_temp, col_ice_pay,2)
reg_line = np.poly1d(reg_line_temp)(col_temp)
plt.plot(col_temp,reg_line,'--',color=(0,1,0))

#plt.hist(col_temp)
plt.show()
