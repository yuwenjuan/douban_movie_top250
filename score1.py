#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']#解决中文乱码问题

df = pd.read_csv('E:/Movie.csv',encoding = 'utf8')
data = df[u'评分']#获取评分那一列的数据
bins = [8.0,8.5,9.0,9.5,10]  #分区(0,8],(8,8.5]....
sub_reg = pd.cut(data,bins=bins)
sub_cnt = sub_reg.value_counts()  #统计区间个数
print(len(sub_cnt))
data=[]
for i in range(len(sub_cnt)):
    data.append(sub_cnt[i])
for a,b in zip(range(len(sub_cnt)),data):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)
labels=sub_cnt.index
plt.xlabel(u'评分区间')
plt.ylabel(u'数量')
plt.title(u'电影评分分布情况',fontsize=16)
plt.bar(range(len(sub_cnt)),data,tick_label=labels,color='rgby')
plt.show()