# -*- coding: utf-8 -*-

import pandas as pd
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np
#读取抓取的csv文件，标题在第3列，序号为2
df=pd.read_csv('douban_movie.csv',header=None,usecols=[2])

#将dataframe转换为list
contents=df.values.tolist()
#数据长度
print(len(contents))
#定义空列表存储情感分值
score=[]

for content in contents:
	#print(content)
	try:
		s=SnowNLP(content[0])
		score.append(s.sentiments)
	except:
		print("something is wrong")
		score.append(0.5)
#显示情感得分长度，与数据长度比较
plt.hist(score, bins=np.arange(0, 1, 0.01), facecolor='g')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('Analysis of Sentiments')
plt.show()
plt.savefig("emotion.png")
print(len(score))
#存储
data2 = pd.DataFrame(score)
data2.to_csv('sentiment.csv', header=False, index=False, mode='a+')
