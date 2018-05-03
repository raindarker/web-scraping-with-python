#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
from qiushi.middlewares.resource import UserAgents, PROXIES

class CustomUserAgent(UserAgentMiddleware):
    def process_request(self,request,spider):
        # ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"
        ua = random.choice(UserAgents)
        request.headers.setdefault('User-Agent', ua)

class CustomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = proxy


