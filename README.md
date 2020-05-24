# test
本项目主要有两个部分，第一部分爬取豆瓣热门电影排行前250的信息并进行处理，第二部分爬取单个电影的热门短评与评分信息并分析处理。
运行文件顺序：download.py爬取top250电影信息并保存到top250_movie.csv，open.py电影主要信息，
rank.py电影主要信息，douban_movie_comment.py爬取某一部电影评论评分信息并保存到douban_movie.csv，
以肖申克的救赎为例，douban_sentiment_analysis.py生成每一条评论情感值并保存到sentiment.csv文件，
复制sentiment中的值到douban_movie.csv中，douban_movie.csv新插入一行“time user comment score
recommend emotion”score.py肖申克的救赎评分分布情况，douban_score_analysis.py统计1星2星。。。的数量，
相同星分一组，计算该组 情感值平均值，douban_wordcloud.py生成词云。
打开CSV文件乱码时先关闭文件，用记事本打开.CSV，另存为，编码改成ANSI
但是接下来分析还要用到.csv文件时，要再把文件编码改为UTF-8
