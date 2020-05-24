# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:51:45 2020

@author: lenovo
"""

#import numpy as np
import pandas as pd

df=pd.read_csv('top250_movie.csv',sep='#',encoding='utf8')
print(df.head())
print(df.info())
df.duplicated().value_counts()
#检查是否有重名电影
len(df.movie_name.unique())
country =df['movie_country'].str.split(' ').apply(pd.Series)
country.head()
all_country = country.apply(pd.value_counts).fillna('0')
all_country.columns = ['area1','area2','area3','area4','area5','area6']
all_country['area1'] = all_country['area1'].astype(int)
all_country['area2'] = all_country['area2'].astype(int)
all_country['area3'] = all_country['area3'].astype(int)
all_country['area4'] = all_country['area4'].astype(int)
all_country['area5'] = all_country['area5'].astype(int)
all_country['area6'] = all_country['area6'].astype(int)
#得到一个国家或地区参与制作电影数的排名情况
all_country['all_counts'] = all_country['area1']+all_country['area2']+all_country['area3']+all_country['area4']+all_country['area5']+all_country['area6']
#降序
all_country = all_country.sort_values(['all_counts'],ascending=False)
print(all_country.head())
#关于电影类型的字段分析
all_type = df['movie_type'].str.split(' ').apply(pd.Series)
all_type = all_type.apply(pd.value_counts).fillna('0')
all_type.columns = ['tpye1','type2','type3','type4','type5']
all_type['tpye1'] = all_type['tpye1'].astype(int)
all_type['type2'] = all_type['type2'].astype(int)
all_type['type3'] = all_type['type3'].astype(int)
all_type['type4'] = all_type['type4'].astype(int)
all_type['type5'] = all_type['type5'].astype(int)
print(all_type.head(10))
#计算总数
all_type['all_counts'] = all_type['tpye1']+all_type['type2']+all_type['type3']+all_type['type4']+all_type['type5']
all_type = all_type.sort_values(['all_counts'],ascending=False)
all_type.head(10)
all_type = all_type.unstack().dropna().reset_index()
all_type.head(10)
all_type.columns =['level_0','level_1','counts']
all_type_m = all_type.drop(['level_0'],axis=1).groupby('level_1').sum()
all_type_m.sort_values(['counts'],ascending=False)
#获取电影类型数量前10的类型
print(all_type_m.head(10))