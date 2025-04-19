#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔
from common.OprateFile import filePath
import xlrd



class oprateExcel:

	def getExcelDatas(self,fileName):
		book = xlrd.open_workbook(filePath(fileName=fileName))
		sheet = book.sheet_by_index(0)
		datas=list()
		title=sheet.row_values(0)
		for row in range(1, sheet.nrows):
			row_value=sheet.row_values(row)
			datas.append(dict(zip(title,row_value)))
		return datas

	def isRun(self,fileName):
		run_list=list()
		datas=self.getExcelDatas(fileName)
		for item in datas:
			if item['是否执行']=='y':
				run_list.append(item)
		return run_list


