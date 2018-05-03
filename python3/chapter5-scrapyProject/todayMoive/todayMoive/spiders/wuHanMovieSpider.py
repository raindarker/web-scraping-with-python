# -*- coding: utf-8 -*-
import scrapy
from todayMoive.items import TodaymoiveItem

class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['theater.mtime.com']
    start_urls = (
        'http://theater.mtime.com/China_Guangdong_Province_Shenzen/',
    )

    def parse(self, response):
        subSelector = response.xpath('//li[@class="clearfix"]')
        items = []
        for sub in subSelector:
            print(sub.extract())
            item = TodaymoiveItem()
            item['moiveName'] = sub.xpath('./dl/dt/a/text()').extract()
            items.append(item)
        return items
