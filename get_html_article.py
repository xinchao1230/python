# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 20:00:44 2017

@author: tianxinchao
"""
import os
import requests
import re
from bs4 import BeautifulSoup
         
def get_page_html():
    if not os.path.exists('E:/one_articles/'):
        os.makedirs('E:/one_articles/')
        
    for i in range(11, 100):
        page_url = 'http://wufazhuce.com/article/{}'.format(i)
        html = requests.get(page_url).content.decode('utf-8')
        
        soup = BeautifulSoup(html,"html.parser")
        article_all = soup.select('div[class="articulo-contenido"]')
        if len (article_all) > 0:
            # 抓取标题
            title_regex = re.compile('<title>(.*?)</title>')
            title = re.findall(title_regex, html)[0]

            with open('E:/one_articles/%s--[%s].txt' % (i,title), 'w') as file:
                file.write(article_all[0].get_text().strip().encode('utf-8'))
         
if __name__ == '__main__':
    get_page_html()