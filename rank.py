# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:50:22 2020

@author: lenovo
"""

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
df=pd.read_csv('top250_movie.csv',sep='#',encoding='utf8')
#%matplotlib inline

#配置中文字体和修改字体大小
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 20

plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
plt.scatter(df['movie_score'],df['movie_num'])
plt.xlabel('movie_score')
plt.ylabel('movie rank')
#修改y轴为倒序
plt.gca().invert_yaxis()

#集中趋势的直方图
plt.subplot(1,2,2)
plt.hist(df['movie_score'],bins=15)
plt.savefig("评分图.png")
#电影排名和评分的相关性检测
df['movie_score'].corr(df['movie_num'])
country_rank = pd.DataFrame({'counts':all_country['all_counts']})
country_rank
country_rank.sort_values(by='counts',ascending=False).plot(kind='bar',figsize=(14,6))
plt.savefig("国家或地区直方图.png")