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

#성장성 지수
#최근 결산연도의 매출액, 영업이익 증가율을 사용한다.
#매출액증가율 = 매출액(최근) / 매출액(작년) -1
#영업이익증가율 = 영업이익(최근) / 영업이익(작년) -1
#스코어 산정지수 : 매출액증가율/2 + 영업이익증가율/2
for i in code_list:
  #if count>3:
  #  break
  code_name = i[1]
  code = i[0]

  if code in month3_list:
    sql_stocks = "select 발행주식수_보통주,code from bs_list where date='2018/' and code="+code

  sql_stocks = "select 발행주식수_보통주,code from bs_list where date='2018/12' and code="+code

  if code in empty_list:
    continue
  if code in month3_list:
    curr_date = '2019/03'
    prev_date = '2018/03'
    select_sql = "select code,매출액,영업이익,date from bs_list where date between '%s' and '%s' and code=%s"%(prev_date,curr_date, code)
  elif code in month6_list:
    curr_date = '2019/06'
    prev_date = '2018/06'
    select_sql = "select code,매출액,영업이익,date from bs_list where date between '%s' and '%s' and code=%s"%(prev_date,curr_date, code)
  elif code in month9_list:
    curr_date = '2019/09'
    prev_date = '2018/09'
    select_sql = "select code,매출액,영업이익,date from bs_list where date between '%s' and '%s' and code=%s"%(prev_date,curr_date, code)
  elif code in month11_list:
    curr_date = '2019/11'
    prev_date = '2018/11'
    select_sql = "select code,매출액,영업이익,date from bs_list where date between '%s' and '%s' and code=%s"%(prev_date,curr_date, code)
  else:
    curr_date = '2018/12'
    prev_date = '2017/12'
    select_sql = "select code,매출액,영업이익,date from bs_list where date between '%s' and '%s' and code=%s"%(prev_date,curr_date, code)

  cursor.execute(select_sql)
  select_stocks_sql = cursor.fetchall()
  
  try:
    #매출액증가율 = 매출액(최근) / 매출액(작년) -1
    sales_growth = (float(select_stocks_sql[1][1]) / float(select_stocks_sql[0][1]))-1
    sales_growth = round(sales_growth,4)

    #영업이익증가율 = 영업이익(최근) / 영업이익(작년) -1
    sales_profit_growth = (float(select_stocks_sql[1][2]) / float(select_stocks_sql[0][2]))-1
    sales_profit_growth = round(sales_profit_growth,2)
    
    growth_ratio = round(sales_growth/2 + sales_profit_growth/2,4)
  except ZeroDivisionError:
    growth_ratio = 0

  
  
  """ if code in empty_list:
    continue

  if code in month3_list:
    choose_date = '2019/03'
    update_sql = "update rank_corp set growth='%s' where code='%s' and settle_date='2019/03'"%(float(growth_ratio),code)
  elif code in month6_list:
    choose_date = '2019/06'
    update_sql = "update rank_corp set growth='%s' where code='%s' and settle_date='2019/06'"%(float(growth_ratio),code)
  elif code in month9_list:
    choose_date = '2019/09'
    update_sql = "update rank_corp set growth='%s' where code='%s' and settle_date='2019/09'"%(float(growth_ratio),code)
  elif code in month11_list:
    choose_date = '2019/11'
    update_sql = "update rank_corp set growth='%s' where code='%s' and settle_date='2019/11'"%(float(growth_ratio),code)
  else:
    choose_date = '2018/12'
    update_sql = "update rank_corp set growth='%s' where code='%s' and settle_date='2018/12'"%(float(growth_ratio),code)

  print(update_sql)
  cursor.execute(update_sql)
  con.commit() """

  if code in empty_list:
    continue

  if code in month3_list:
    choose_date = '2019/03'
    update_sql = "update rank_corp set net_profit=%s where code='%s' and settle_date='%s'"%(float(sales_profit_growth),code,choose_date)
  elif code in month6_list:
    choose_date = '2019/06'
    update_sql = "update rank_corp set net_profit=%s where code='%s' and settle_date='%s'"%(float(sales_profit_growth),code,choose_date)
  elif code in month9_list:
    choose_date = '2019/09'
    update_sql = "update rank_corp set net_profit=%s where code='%s' and settle_date='%s'"%(float(sales_profit_growth),code,choose_date)
  elif code in month11_list:
    choose_date = '2019/11'
    update_sql = "update rank_corp set net_profit=%s where code='%s' and settle_date='%s'"%(float(sales_profit_growth),code,choose_date)
  else:
    choose_date = '2018/12'
    update_sql = "update rank_corp set net_profit=%s where code='%s' and settle_date='%s'"%(float(sales_profit_growth),code,choose_date)

  print(update_sql)
  cursor.execute(update_sql)
  con.commit()

  count = count+1
  print(count) 

con.close()