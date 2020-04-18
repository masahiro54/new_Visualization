import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import time
import datetime
import math
Y = np.linspace(0, 100)

print(type(Y))

col_date=[]
col_pollen =[]
col_5_avg = []


conn = psycopg2.connect("dbname=trading_company host=localhost user=mkoshida password=powered3543")
cur = conn.cursor()
cur.execute("select CAST (date_code AS date),Pollen_scattering_num, col5_avg from Preprocessing_6 order by date_code;")
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
    col_date.append(rows[dcnt][0])
    col_pollen.append(rows[dcnt][1])
    col_5_avg.append(rows[dcnt][2])
    dcnt = dcnt + 1
    
#print(rows[1][1])

plt.plot(col_date, col_pollen, color=(0,0,1))
plt.plot(col_date, col_5_avg, color=(1,0,0))
plt.scatter(col_date, col_pollen, s=50, marker="x", c="red", linewidth=1)
plt.show()
