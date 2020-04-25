# matplotlibのプロットあれこれ  
　
データサイエンス界隈でpythonのよく使うライブラリと言えば、numpy,pandas,**matplotlib**です。

今回はその**matplotlib**でもとりわけよく利用するグラフをプロットする部分に着目し、どんなことができるのかをまとめました。

## よく使うモジュール

プログラムの頭に以下のような、文言を書くことが多いです。
それがどういう意味なのかを調べました、
```
import matplotlib.pyplot as plt
```

* matplotlib  
  ご存じ、今回解説するライブラリです。このライブラリを使ってグラフを作っていきます。

* pyplot  
  matplotlib内のモジュールです。  
  ざっくりいうとホントは手動で設定しなきゃいけないものを自動でやってくれる便利ツールです。  
  今回は基本的にこちらを用いたプロットの方法を解説します。

## 折れ線グラフ
線グラフを記載する場合にはplotを使用します。  
使い方としては以下の式の通りです。  
  
```Python:折れ線.py
plt.plot(X, Y, ls='-',lw='1', color='b',marker = '+',label='ice_sales')

plt.legend()
```

![Imgur](https://i.imgur.com/u2NkmnF.png)



（↑ サンプルで上記の式のグラフを出力しました。） 

それぞれの引数に関しては以下の表のとおりです。
引数|説明|補足
| :--- | :--- | :--- | :--- |
X|X軸|必須項目
Y|Y軸|入力しない場合データ数になります。
label|凡例|plt.legend()を付けないと表示されません。
color|線の色|使える色は⇒参照:https://matplotlib.org/api/colors_api.html
ls|線の種類|"例えば右記のようなパラメータが使用できます。⇒ '-' , '--', '-.' , ':' , 'steps'
lw|線の太さ|デフォルトは1.0
marker|マーカー形状|"例えば右記のパラメータが使用できます。'+' ,  ','  , '.' , "o", '1' , '2' ,'3' ,'4'


## 散布図
散布図を記載する場合にはscatterを使用します。  
使い方としては以下の式の通りです。  
  
```Python:散布図.py
plt.scatter(data_frame.high_temp, data_frame.ice_payment,s=20, marker='o', cmap='jet',c=data_frame.ice_payment)

plt.colorbar()
```

![Imgur](https://i.imgur.com/nZEiU3L.png)  

（↑ サンプルで上記の式のグラフを出力しました。） 

それぞれの引数に関しては以下の表のとおりです。
引数|説明|補足
| :--- | :--- | :--- | :--- |
X|X軸|必須項目
Y|Y軸|必須項目
c|色|X,Yの値も指定できます。
s|サイズ|デフォルト値：20
marker|マーカー形状|デフォルトはo
cmap|カラーマップ| plt.colorbar()が必要

## 円グラフ

円グラフを記載する場合にはpieを使用します。  
使い方としては以下の式の通りです。  

```Python:円.py
x = numpy.array([400, 400, 600, 800, 200])
colors = ["yellow", "red", "blue", "green", "orange"]
ex = numpy.array([0.2, 0, 0, 0, 0])
label = ["Carbonara", "Arabian", "Pescatore", "Genovese", "Peperoncino"]
plt.pie(x,labels=label,explode = ex,startangle=90,colors=colors,explode = 0.2)
```
  
![Imgur](https://i.imgur.com/5KDSTrW.png)  
（↑ サンプルで上記の式のグラフを出力しました。） 

引数|説明|補足
| :--- | :--- | :--- | :--- |
X|X軸|この値だけでも成立します。
label |ラベル|Xの値毎にラベルを張ります。
colors|色|Xの値毎に色を設定します。
explode|指定したXの値を円の中心から指定した値分離して表示|サンプルは0.2離した状態です。


## 棒グラフ
棒グラフを記載する場合にはbarを使用します。
使い方としては以下の式の通りです。

```Python:棒.py
X = numpy.array([1, 2, 3, 4, 5])
Y = numpy.array([400, 400, 600, 800, 200])
Y2 = numpy.array([400, 400, 600, 800, 200])
colors = ["yellow", "red", "blue", "green", "orange"]
label = ["Carbonara", "Arabian", "Pescatore", "Genovese", "Peperoncino"]
plt.bar(X, Y,width = 0.8 , color =colors,tick_label = label,linewidth= 1,edgecolor="#000000")
```
![Imgur](https://i.imgur.com/atAmibq.png)  
（↑ サンプルで上記の式のグラフを出力しました。） 

引数|説明|補足
| :--- | :--- | :--- | :--- |
X|X軸|必須項目
Y|Y軸|必須項目
width |棒グラフ幅|デフォルトは0.8
tick_label| X軸ラベル|設定しない場合はＸ軸が表示されます。
color|色|棒の色を設定します。
linewidth|枠線サイズ|設定することによって、枠線を付けることができます。
edgecolor|枠線色|colorと同様で配列型での指定も可能です。
bottom |棒グラフの下の値|例えば、100にするとすべてのＹ軸の始点が100になります。また、積み上げグラフ（以下参照）を作成する場合に使われます。

### 積み上げグラフ
パラメータのbottomに下の棒グラフのＹ値を入れることによって、上にグラフを積江げることが可能です。
先ほど出力した棒グラフに対して積み上げたパターンが以下です。
```Python:積み上げ棒.py
X = numpy.array([1, 2, 3, 4, 5])
Y = numpy.array([400, 400, 600, 800, 200])
Y2 = numpy.array([600, 600, 400, 200, 800])
colors = ["yellow", "red", "blue", "green", "orange"]
label = ["Carbonara", "Arabian", "Pescatore", "Genovese", "Peperoncino"]
plt.bar(X, Y,width = 0.8 , color =colors,tick_label = label,linewidth= 1,edgecolor="#000000")
plt.bar(X, Y2,bottom=Y)
```
![Imgur](https://i.imgur.com/zKRtPuo.png)  
