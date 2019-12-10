import sys
#from PyQt5.QtWidgets import *
#from PyQt5.QAxContainer import *
#from PyQt5.QtCore import *
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import datetime
import time
import numpy as np

con = pymysql.connect(host='db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com', user='admin',password='adminroot',db='stockdb',charset='utf8')
engine = create_engine("mysql+pymysql://admin:"+"adminroot"+"@db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com/stockdb?charset=utf8",encoding='utf-8')
conn = engine.connect()
cursor = con.cursor()
cursor.execute("set names utf8")
con.commit()


sql = "select code,name from code_list where market=0"
cursor.execute(sql)
data = cursor.fetchall()
code_list = list(data)

month3_list = ['018500','002630','000970', '008110', '092440', '018500', '001720']
month6_list = ['033250', '093240','001080','005390']
month9_list = ['003610', '008870']
month11_list = ['004310']
empty_list = ['152550', '316140', '094800', '336370', '088980', '336260','330590', '099350', '021820', '096300', '099340']

count =0
 #성장성 insert db
for i in code_list:
	#if count>10:
	#	break
	code_name = i[1]
	code = i[0]
	
	#사이즈(시가총액 = 발행주식수 x 주가)
	if code in empty_list:
		continue
	if code in month3_list:
		insert_stock_list_sql = "insert into rank_corp (code,name,settle_date) values('%s','%s','2019/03')"%(code,code_name)
	if code in month6_list:
		insert_stock_list_sql = "insert into rank_corp (code,name,settle_date) values('%s','%s','2019/06')"%(code,code_name)
	if code in month9_list:
		insert_stock_list_sql = "insert into rank_corp (code,name,settle_date) values('%s','%s','2019/09')"%(code,code_name)
	if code in month11_list:
		insert_stock_list_sql = "insert into rank_corp (code,name,settle_date) values('%s','%s','2019/11')"%(code,code_name)
	else:
		insert_stock_list_sql = "insert into rank_corp (code,name,settle_date) values('%s','%s','2018/12')"%(code,code_name)

	print(insert_stock_list_sql)
	cursor.execute(insert_stock_list_sql)
	con.commit()
	
	count = count +1
	print(count)


con.close()
	
	
