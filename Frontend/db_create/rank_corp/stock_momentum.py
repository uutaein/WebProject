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
  #if count >3:
  #  break
  code_name = i[1]
  code = i[0]
  
  #모멘텀 
  #최근 3개월동안의 주가수익률
  select_sql = "select date,close from c%s order by date desc limit 1,90"%(code)
  cursor.execute(select_sql)
  select_stocks_sql = cursor.fetchall()

  
  length = len(select_stocks_sql)
  cur_price = int(select_stocks_sql[0][1])
  prev_price = int(select_stocks_sql[length-1][1])

  #최근 3개월동안의 수익률(%)
  try:
    momentum_3m_profitage = round(cur_price/prev_price -1,4)
    profit_3m = round(momentum_3m_profitage,2)
  except ZeroDivisionError:
    momentum_3m_profitage = 0
    profit_3m = 0
  
  
  """ update_sql = "update rank_corp set momentum_3m_profitage=%s where code=%s"%(float(momentum_3m_profitage),code)
  cursor.execute(update_sql)
  con.commit() """

  update_sql = "update rank_corp set profit_3m=%s where code=%s"%(float(profit_3m),code)
  cursor.execute(update_sql)
  con.commit()

  count = count+1
  print(count)

con.close()