#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import re

mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('E:/Movie.csv',encoding = 'utf8')
num = []
for i in df[u'评分人数']:
    num.append(re.findall(r'\d+',i))
plt.figure(figsize=(8,6))
plt.plot(df[u'排名'],num,color = 'cornflowerblue',ls='-')
plt.ylabel(u'评分人数',fontsize=16)
plt.xlabel(u'排名',fontsize=16)
plt.show()