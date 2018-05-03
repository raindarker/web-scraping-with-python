#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class ShowDict(object):
	'''该类用于展示字典的使用方法 '''
	def __init__(self):
		self.spiderMan = self.createDict()
		self.insertDict(self.spiderMan)
		self.modifyDict(self.spiderMan)
		self.operationDict(self.spiderMan)
		self.deleteDict(self.spiderMan)

	def createDict(self):
		print("创建字典:")
		print("执行命令spiderMan = {'name':'Peter Parker','sex':'male','Nation':'Americ','college':'MIT'}")
		spiderMan = {'name':'Peter Parker','sex':'male','Nation':'Americ','college':'MIT'}
		self.showDict(spiderMan)
		return spiderMan

	def showDict(self,spiderMan):
		print("显示字典")
		print(("spiderMan = "), end=' ')
		print(spiderMan)
		print('\n')

	def insertDict(self,spiderMan):
		print("字典中添加键age，值为31")
		print("执行命令spiderMan['age'] = 31")
		spiderMan['age'] = 31
		self.showDict(spiderMan)

	def modifyDict(self,spiderMan):
		print("字典修改键'college'的值为'Empire State University'")
		print("执行命令spiderMan['college'] = 'Empire State University'")
		spiderMan['college'] = 'Empire State University'
		self.showDict(spiderMan)

	def operationDict(self,spiderMan):
		print("字典的其它操作方法")
		print("###########################")
		print("显示字典所有的键，keyList = spiderMan.keys()")
		keyList = list(spiderMan.keys())
		print(("keyList = "), end=' ')
		print(keyList)
		print('\n')
		print("显示字典所有键的值，valueList = spiderMan.values()")
		valueList = list(spiderMan.values())
		print(("valueList = "), end=' ')
		print(valueList)
		print('\n')
		print("显示字典所有键和值的元组，itemList = spiderMan.items()")
		itemList = list(spiderMan.items())
		print(("itemList = "), end=' ')
		print(itemList)
		print('\n')
		print("取字典中键为college的值,college = spiderman.get('college')")
		college = spiderMan.get('college')
		print(("college = %s" %college))
		print('\n')
	
	def deleteDict(self,spiderMan):
		print("删除字典中键为Nation的值")
		print("执行命令 del(spiderMan['Nation'])")
		del(self.spiderMan['Nation'])
		self.showDict(spiderMan)
		print("清空字典中所有的值")
		print("执行命令 spiderMan.clear()")
		self.spiderMan.clear()
		self.showDict(spiderMan)
		print("删除字典")
		print("执行命令 del(spiderMan)")
		del(spiderMan)
		print("显示spiderMan")
		try:
			self.showDict(spiderMan)
		except NameError:
			print("spiderMan 未被定义")


if __name__ == '__main__':
	sd = ShowDict()
