#!/usr/bin/evn python
#-*- coding: utf-8 -*-
'''
Created on 2016年8月11日

@author: hstking hstking@hotmail.com
'''

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import codecs
import time
from mylog import MyLog as mylog
from save2mysql import SavebooksData


class BookItem(object):
    categoryName = None
    middleUrl = None
    bookName = None
    wordsNum = None
    updateTime = None
    authorName = None
    

class GetBookName(object):
    def __init__(self):
        self.urlBase = 'http://all.qidian.com/Book/BookStore.aspx?&Tag=all&Action=5&OrderId=6&P=all&PageIndex=1'
        self.log = mylog()
        self.pages = self.getPages(self.urlBase)
        self.booksList = []
        self.spider(self.urlBase, self.pages)
        self.pipelines(self.booksList)
        self.log.info('begin save data to mysql\r\n')
        SavebooksData(self.booksList)
        self.log.info('save data to mysql end ...\r\n')
      
        
    def getPages(self,url):
        htmlContent = self.getResponseContent(url)
        soup = BeautifulSoup(htmlContent, 'lxml')
        tags = soup.find('a', attrs={'class':'lbf-pagination-page'})
        print(tags)
        strUrl = tags.get('href')
        print(strUrl)
        for st in strUrl.split('&'):
            if re.search('page', st):
                pages = st.split('=')[-1]
                self.log.info('获取页数为:%s' %pages)
                return int(pages)
    
    def getResponseContent(self, url):
        try:
            response = urllib.request.urlopen(url)
        except:
            self.log.error('Python 返回URL:%s  数据失败' %url)
        else:
            self.log.info('Python 返回URUL:%s  数据成功' %url)
            return response.read()
    
    
    def spider(self, url, pages):
        urlList = url.split('=')
        for i in range(1, pages + 1):
            urlList[-1] = str(i)
            newUrl = '='.join(urlList)
            htmlContent = self.getResponseContent(newUrl)
            soup = BeautifulSoup(htmlContent, 'lxml')
            tags = soup.find_all('div', attrs={'class':'sw1'}) + soup.find_all('div', attrs={'class': 'sw2'})
            for tag in tags:
                item = BookItem()
                item.categoryName = tag.find('div', attrs={'class': 'swa'}).get_text()
                item.middleUrl = tag.find('div', attrs={'class':'swb'}).span.a.get('href')         
                item.bookName = tag.find('div', attrs={'class': 'swb'}).span.a.get_text()
                item.wordsNum = tag.find('div', attrs={'class':'swc'}).get_text()
                item.updateTime = tag.find('div', attrs={'class':'swe'}).get_text()
                item.authorName = tag.find('div', attrs={'class':'swd'}).a.get_text()
                self.booksList.append(item)
                self.log.info('获取书名为<<%s>>的数据成功' %item.bookName)
       
                
    def pipelines(self,bookList):
        bookName = '起点完本小说.txt'.encode('utf-8')
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S\r\n', time.localtime())
        with codecs.open(bookName, 'w', 'utf8') as fp:
            fp.write('run time: %s' %nowTime)
            for item in self.booksList:
                fp.write('%s \t %s \t\t %s \t %s \t %s \r\n' 
                         %(item.categoryName, item.bookName, item.wordsNum, item.updateTime, item.authorName))
                self.log.info('将书名为<<%s>>的数据存入"%s"...' %(item.bookName, bookName.decode('utf-8')))

if __name__ == '__main__':
    GBN = GetBookName()

