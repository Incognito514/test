# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import jieba
import collections
import pandas as pd
from scipy.misc import imread
def chinese_jieba(text):
    wordlist_jieba=jieba.cut(text)
    space_wordlist=" ".join(wordlist_jieba)
    return space_wordlist

#读取csv文件
df=pd.read_csv('douban_movie.csv')
comment_list=df['comment'].values.tolist()
score_list=df['score'].values.tolist()
text=""
stopwords = [line.strip() for line in open('stop.txt',encoding='UTF-8').readlines()]
for jj in range(len(comment_list)):
        text=text+chinese_jieba(comment_list[jj])
        word_counts=collections.Counter(text)
print(text)
mask_pic=imread('movie.jpg')
wordcloud=WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",#设置字体
                      mask=mask_pic,#设置背景图片
                      background_color="white",#设置背景颜色
                      max_font_size=150,# 设置字体最大值
                      max_words=2000, # 设置最大显示的字数
                       stopwords=stopwords #设置停用词，停用词则不再词云图中表示
                     ).generate(text)#根据文本生成词云
imge=wordcloud.to_image()
wordcloud.to_file('key.png')