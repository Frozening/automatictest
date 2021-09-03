#!/usr/bin/python
#!coding = utf8
import pytest
import json
import xlrd
import requests

def excel():
    book = xlrd.open_workbook('./data/juhe.xls') #可以把excel()写在class里，然后文件名用__init__传递
    sheet = book.sheet_by_index(0)
    item = [dict(zip(sheet.row_values(0), sheet.row_values(row))) for row in range(1, sheet.nrows)] #循环读取每行数据并转化为字典形式，并迭代更新字典列表
    return item #之所以返回list，是因为pramarmetrize()装饰器的传数据必须是list

#在readdata from excel.py中接受item