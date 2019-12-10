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

count=0

month3_list = ['018500','002630','000970', '008110', '092440', '018500', '001720']
month6_list = ['033250', '093240','001080','005390']
month9_list = ['003610', '008870']
month11_list = ['004310']
empty_list = ['152550', '316140', '094800', '336370', '088980', '336260','330590', '099350', '021820', '096300', '099340']

for i in code_list:
  #if count >50:
  #  break
  code_name = i[1]
  code = i[0]
  
  if code in empty_list:
    continue

  if code in month3_list:
    select_stock_list_sql = "select 발행주식수_보통주,code from bs_list where date='2019/03' and code='%s'"%(code)
  elif code in month6_list:
    select_stock_list_sql = "select 발행주식수_보통주,code from bs_list where date='2019/06' and code='%s'"%(code)
  elif code in month9_list:
    select_stock_list_sql = "select 발행주식수_보통주,code from bs_list where date='2019/09' and code='%s'"%(code)
  elif code in month11_list:
    select_stock_list_sql = "select 발행주식수_보통주,code from bs_list where date='2019/11' and code='%s'"%(code)
  else:
    select_stock_list_sql = "select 발행주식수_보통주,code from bs_list where date='2018/12' and code='%s'"%(code)
  

  
  cursor.execute(select_stock_list_sql)
  select_stocks_sql = cursor.fetchall()
  #print(select_stock_list_sql)
  #print(select_stocks_sql)

  
  stocks_in_market = str(select_stocks_sql[0][0]) # 발행주식수 보통주
  stocks_in_market = int(stocks_in_market)
  #단위:백만원

  try:
    truncate_stocks = int(stocks_in_market/1000000)
  except ZeroDivisionError:
    truncate_stocks = 0
    
  sql_sise_stocks = "select date,close from c"+code+" order by date desc limit 1,10"
  cursor.execute(sql_sise_stocks)
  sise_sql = cursor.fetchall()
  sise_stock = sise_sql[0][1]
  sise_stock = int(sise_stock)


  stock_size = truncate_stocks*sise_stock           # (발행주식수_보통주/1000000)*(11/26 시가)
  stock_capital = round(float(stock_size / 100),3)  #단위: 억원
  """ if code in empty_list:
    continue

  if code in month3_list:
    choose_date = '2019/03'
    update_sql = "update rank_corp set size='%s' where code='%s' and settle_date='2019/03'"%(stock_size,code)
  elif code in month6_list:
    choose_date = '2019/06'
    update_sql = "update rank_corp set size='%s' where code='%s' and settle_date='2019/06'"%(stock_size,code)
  elif code in month9_list:
    choose_date = '2019/09'
    update_sql = "update rank_corp set size='%s' where code='%s' and settle_date='2019/09'"%(stock_size,code)
  elif code in month11_list:
    choose_date = '2019/11'
    update_sql = "update rank_corp set size='%s' where code='%s' and settle_date='2019/11'"%(stock_size,code)
  else:
    choose_date = '2018/12'
    update_sql = "update rank_corp set size='%s' where code='%s' and settle_date='2018/12'"%(stock_size,code)

  print(update_sql)
  cursor.execute(update_sql)
  con.commit() """

  if code in empty_list:
    continue

  if code in month3_list:
    choose_date = '2019/03'
    update_sql = "update rank_corp set stock_capital=%s where code='%s' and settle_date='%s'"%(float(stock_capital),code,choose_date)
  elif code in month6_list:
    choose_date = '2019/06'
    update_sql = "update rank_corp set stock_capital=%s where code='%s' and settle_date='%s'"%(float(stock_capital),code,choose_date)
  elif code in month9_list:
    choose_date = '2019/09'
    update_sql = "update rank_corp set stock_capital=%s where code='%s' and settle_date='%s'"%(float(stock_capital),code,choose_date)
  elif code in month11_list:
    choose_date = '2019/11'
    update_sql = "update rank_corp set stock_capital=%s where code='%s' and settle_date='%s'"%(float(stock_capital),code,choose_date)
  else:
    choose_date = '2018/12'
    update_sql = "update rank_corp set stock_capital=%s where code='%s' and settle_date='%s'"%(float(stock_capital),code,choose_date)

  print(update_sql)
  cursor.execute(update_sql)
  con.commit()
  count = count+1
  print(count)

con.close()