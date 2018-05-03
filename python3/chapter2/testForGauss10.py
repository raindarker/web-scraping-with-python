#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

def cumulative(num):
	sum = 0
	for i in range(1,num+1):
		sum += i
	return sum

def main():
	while True:
		print("===========================")
		print("输入exit退出程序:")
		str_num = input("从1累加到：")
		if str_num == 'exit':
			break
		try:
			sum = cumulative(int(str_num))
		except ValueError:
			print("除非退出输入exit，只能输入数字")
			continue
		print(("从1累加到%d的总数是%d" %(int(str_num),sum)))
	

if __name__ == '__main__':
	main()
