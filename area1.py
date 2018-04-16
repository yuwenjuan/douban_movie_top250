#-*- coding: utf-8 -*-
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('E:/Movie.csv',encoding = 'utf8')
area_split = df[u'地区'].str.split(' ').apply(pd.Series)
a = area_split.apply(pd.value_counts).fillna('0')
a.columns = ['area_1','area_2','area_3','area_4','area_5']
a['area_1'] = a['area_1'].astype(int)
a['area_2'] = a['area_2'].astype(int)
a['area_3'] = a['area_3'].astype(int)
a['area_4'] = a['area_4'].astype(int)
a['area_5'] = a['area_5'].astype(int)
a = a.apply(lambda x: x.sum(),axis = 1)#axis = 1,将一个矩阵的每一行向量相加.axis = 0,列相加
data=[]
for i in range(len(a)):
    data.append(a[i])
labels=a.index
plt.figure(figsize=(10,6))
plt.bar(range(len(a)),data,label=labels)
for a,b in zip(range(len(a)),data):
    plt.text(a,b+0.5,'%.0f'%b,ha='center',va='bottom',fontsize=11)
plt.legend(loc='upper right')
plt.title(u'电影国家/地区分布情况',fontsize=13)
plt.ylabel(u'电影数量',fontsize=13)
plt.xlabel(u'国家/地区',fontsize=13)
plt.show()