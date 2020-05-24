# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:05:25 2020

@author: lenovo
"""

import urllib.request as urlrequest
from bs4 import BeautifulSoup
import csv 

top250_url ='https://movie.douban.com/top250?start={}&filter='
movie_name='名称'
movie_assess='评价人数'
movie_score='评分'
movie_url ='链接'
movie_intro='介绍'
movie_num =0

with open('top250_movie.csv','w',encoding='utf8') as outputfile:#写文件
    writer = csv.writer(outputfile)
    #写文件表头
    #writer.writerow(["movie_num","movie_name","movie_assess","movie_score","movie_url","movie_intro"])
    outputfile.write("movie_num#movie_name#movie_year#movie_country#movie_type#movie_director#movie_assess#movie_score#movie_url#movie_intro\n")
    #解析数据
    for list in range(10):
        #获取网页数据
             headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
             #User Agent是标识请求的浏览器身份的，网站常用这个参数来分辨爬虫。加上请求头伪装成网站本身获取数据
             req = urlrequest.Request(url=top250_url.format(list*25), headers=headers)  
             movies_content = urlrequest.urlopen(req).read()
             #movies_content = urlrequest.urlopen(top250_url.format(list*25)).read()
             #设置编码格式
             movies_html = movies_content.decode('utf8')
             #解析HTML
             moviessoup = BeautifulSoup(movies_html,'html.parser')
             #获取数据列表
             all_list = moviessoup.find_all(class_='item')
             #遍历列表，获取字段数据
             #print(all_list)
             for item in all_list:
                 #获取图片
                 item_data=item.find(class_='pic')
                 #获取图片链接
                 movie_url = item_data.find('a')['href']
                 #获取图片描述
                 movie_name = item_data.find('img')['alt']
                 #获取评分
                 item_info = item.find(class_='star')
                 info = item.find('div', attrs={'class': 'star'})
                #find_all 将star标签中的所有span 存入一个列表中
                 movie_assess =info.find_all('span')[3].get_text()[:-3]
                 movie_score = item_info.find('span',attrs={'class':'rating_num'}).get_text()
                 # 获取描述信息
                 try:
                     # 获取描述
                     movie_intro = item.find(class_='quote').find(class_='inq').get_text()
                 except Exception as e:
                     movie_intro='None'  
                 #序号       
                 movie_num =movie_num+1
                
                 #抓取电影上映年份、 导演、主演等信息
                 movie_actor_infos_html = item.find(class_='bd')
                 #strip() 方法用于移除字符串头尾指定的字符（默认为空格）
                 movie_actor_infos = movie_actor_infos_html.find('p').get_text().strip().split('\n')
                 actor_infos1 = movie_actor_infos[0].split('\xa0\xa0\xa0')
                 movie_director = actor_infos1[0][3:]
                 #获取导演信息
                 movie_role = movie_actor_infos[1]
                #获取演员信息
                 movie_year_area = movie_actor_infos[1].lstrip().split('\xa0/\xa0')
                 #获取制作年份
                 movie_year = movie_year_area[0]
                 #获取地区
                 movie_country = movie_year_area[1]
                 #获取电影类型
                 
                 movie_type = movie_year_area[2]
                 
                 if movie_type =='':
                    movie_type='NULL'
                 #写出具体采集信息
                 outputfile.write('{}#{}#{}#{}#{}#{}#{}#{}#{}#{}\n'.format(movie_num,movie_name,movie_year,
                 movie_country,movie_type,movie_director,movie_assess,movie_score,movie_url,movie_intro))