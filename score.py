# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:11:39 2020

@author: lenovo
"""

import csv
#import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def rdata():#读取文件
    pr=pd.read_csv("douban_movie.csv")
    score1=0
    score2=0
    score3=0
    score4=0
    score5=0
    for score in pr['score']:
        if score=='allstar10':
            score1+=1
        elif score=='allstar20':
            score2+=1
        elif score=='allstar30':
            score3+=1
        elif score=='allstar40':
            score4+=1
        elif score=='allstar50':
            score5+=1
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False# 解决 plt 中文显示的问题
    labels=['很差','较差','还行','推荐','力荐']
    values=[score1,score2,score3,score4,score5]
    colors=['y','m','b','w','b']
    explode=[0,0,0,0,0]#每一块离开中心的距离
    plt.title("评分分布情况",fontsize=25)#标题
    plt.pie(values,labels=labels,explode=explode,colors=colors,
            startangle = 180,
            shadow=True,autopct='%1.1f%%')
    plt.axis('equal')#将饼图显示为正圆形
    plt.show()
   
    index=['1星','2星','3星','4星','5星']
    plt.title('评分分布情况')
    values=[score1,score2,score3,score4,score5]
    plt.bar(index,values)
    plt.show()
if __name__=="__main__":
    rdata()
        