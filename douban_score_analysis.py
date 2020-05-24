# -*- coding: utf-8 -*-

import pandas as pd
from collections import Counter

#读取csv文件
df=pd.read_csv('douban_movie.csv')

#统计打分数量
score_list=df['score'].values.tolist()
num_count=Counter(score_list)
#显示热评中不同分值的评论数量
print(num_count)

#分组求平均
grouped = df.groupby('score').describe().reset_index()
score=grouped['score'].values.tolist()
print(score)

#根据用户打分的分组，对每组的情感值求平均
sentiment_average=df.groupby('score')['emotion'].mean()
sentiment_emotions=sentiment_average.values
print(sentiment_emotions)
