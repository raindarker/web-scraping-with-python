#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016��8��13��

@author: hstking hstking@hotmail.com
'''

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import codecs
from mylog import MyLog as mylog


class MovieItem(object):
    movieName = None
    movieScore = None
    movieStarring = None

class GetMovie(object):
    '''获取电影信息 '''
    def __init__(self):
        self.urlBase = 'http://dianying.2345.com/list/----2016---1.html'
        self.log = mylog()
        self.pages = self.getPages()
        self.urls = []  #url池
        self.items = []
        self.getUrls(self.pages) #获取抓取页面的url
        self.spider(self.urls)
        self.pipelines(self.items)
        
    def getPages(self):
        '''获取总页数 '''
        self.log.info('开始获取页数')
        htmlContent = self.getResponseContent(self.urlBase)
        soup = BeautifulSoup(htmlContent, 'lxml')
        tag = soup.find('div', attrs={'class':'video_page'})
        subTags = tag.find_all('a')
        self.log.info('获取页数成功')
        return int(subTags[-2].get_text())
    
    def getResponseContent(self, url):
        '''获取页面返回的数据 '''
        # fakeHeaders= {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}  
        # request = urllib.request.Request(url, headers=fakeHeaders)
        
        # proxy = urllib.request.ProxyHandler({'http':'http://223.241.78.143:18118'})
        # opener = urllib.request.build_opener(proxy)
        # urllib.request.install_opener(opener)

        # print(request)
        try:
            # response = urllib.request.urlopen(request)
            response = urllib.request.urlopen(url)
        except:
            self.log.error('Python 返回URL:%s  数据失败' %url)
        else:
            self.log.info('Python 返回URUL:%s  数据成功' %url)
            return response.read()

    def getUrls(self, pages):
        urlHead = 'http://dianying.2345.com/list/----2016---'
        urlEnd = '.html'
        for i in range(1,pages + 1):
            url = urlHead + str(i) + urlEnd
            self.urls.append(url)
            self.log.info('添加URL:%s 到URLS列表' %url)
    
    def spider(self, urls):
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            anchorTag = soup.find('ul', attrs={'class':'globalPicTxt pic140 clearfix'})
            tags = anchorTag.find_all('li')
            for tag in tags:
                item = MovieItem()
                item.movieName = tag.find('span', attrs={'class':'sTit'}).get_text()
                item.movieScore = tag.find('span', attrs={'class':'pRightBottom'}).em.get_text().replace('分', '')
                item.movieStarring = tag.find('span', attrs={'class':'sDes'}).get_text().replace('主演：', '')
                self.items.append(item)
                self.log.info('获取电影名为：<<%s>>成功' %(item.movieName))
    
    def pipelines(self, items):
        fileName = '2016热门电影.txt'.encode('GBK')
        with codecs.open(fileName, 'w', 'utf8') as fp:
            for item in items:
                fp.write('%s \t %s \t %s \r\n' %(item.movieName, item.movieScore, item.movieStarring))
                self.log.info('电影名为：<<%s>>已成功存入文件"%s"...' %(item.movieName, fileName.decode('GBK')))
            


if __name__ == '__main__':
    GM = GetMovie()
