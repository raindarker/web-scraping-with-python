#!/usr/bin/env python
#-*- coding: utf-8 -*-

from scrapy.selector import Selector

with open('./superHero.xml','r') as fp:
    body = fp.read()

print('body:')
print(body)
print()

print('----------Xpath selector------------')
print('xpath(/*):')
print(Selector(text = body).xpath('/*').extract())
print()

print('xpath(/html/body/superhero/class[1]):')
print(Selector(text = body).xpath('/html/body/superhero/class[1]').extract())
print()

print('xpath(/html/body/superhero/class[last()]):')
print(Selector(text = body).xpath('/html/body/superhero/class[last()]').extract())
print()

print('xpath(//name[@lang="en"):')
print(Selector(text = body).xpath('//name[@lang="en"]').extract())
print()

print('xpath(/html/body/superhero/class[last()-1]/name/text()):')
print(Selector(text = body).xpath('/html/body/superhero/class[last()-1]/name/text()').extract())
print()

print('xpath(/html/body/superhero/class[last()-1]):')
print(Selector(text = body).xpath('/html/body/superhero/class[last()-1]').extract())
print()

print('xpath(/html/body/superhero/class/sex/text()):')
print(Selector(text = body).xpath('/html/body/superhero/class/sex/text()').extract())
print()

print('xpath(//class/sex/text()):')
print(Selector(text = body).xpath('//class/sex/text()').extract())
print()

print('----------css selector------------')
print('css(class name):')
print(Selector(text = body).css('class name').extract())
print()

print('css(class name)[0]:')
print(Selector(text = body).css('class name').extract()[0])
print()

print('css([lang="en"]):')
print(Selector(text = body).css('[lang="en"]').extract())
print()

print('----------re selector------------')
print('xpath(/html/body/superhero/class[1].re):')
print(Selector(text = body).xpath('/html/body/superhero/class[1]').re('>.*?<'))
print()