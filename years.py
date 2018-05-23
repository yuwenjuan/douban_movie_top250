#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_csv('E:/Movie.csv',encoding = 'utf8')
df1=df.groupby('年份').size()
data=[]
for i in range(len(df1)):
    data.append(df1[i])
labels=df1.index
plt.figure(figsize=(10,6))
plt.bar(range(len(df1)),data,label=labels,color='b')
for a,b in zip(range(len(df1)),data):
    plt.text(a,b+0.5,'%.0f'%b,ha='center',va='bottom',fontsize=11)
plt.legend(loc='best')
plt.xlabel(u'上映年份')
plt.ylabel(u'数量')
plt.title(u'每年电影上映情况',fontsize=16)
plt.show()