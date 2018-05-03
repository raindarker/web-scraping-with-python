# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WuhanspiderSpider(scrapy.Spider):
    name = 'wuHanSpider'
    allowed_domains = ['tianqi.com']
    citys = ['shenzhen']
    start_urls = []
    for city in citys:
        start_urls.append('https://www.tianqi.com/'+city+'/')

    def parse(self, response):
        subSelector = response.xpath('//div[@class="day7"]')
        items = []
        for sub in subSelector:
            items = []
            for i in range(7):
                item = WeatherItem()
                cityDate = sub.xpath('./ul[@class="week"]/li/b//text()').extract()[i]
                item['cityDate'] = cityDate
                week = sub.xpath('./ul[@class="week"]/li/span//text()').extract()[i]
                item['week'] = week
                img = sub.xpath('./ul[@class="week"]/li/img/@src').extract()[i]
                item['img'] = img
                weather = sub.xpath('./ul[@class="txt txt2"]/li//text()').extract()[i]
                item['weather'] = weather
                wind = sub.xpath('./ul[@class="txt"]/li//text()').extract()[i]
                item['wind'] = wind
                items.append(item)
            return items
