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

#동일업종내 PER비교

for i in code_list:
  #if count>3:
  #  break
  code_name = i[1]
  code = i[0]
  
  if code in empty_list:
      continue
  if code in month3_list:
      cur_date = '2019/03'
      select_low_val_sql = "select code,name,per_배율,date from bs_list where code='%s' and date='%s'"%(code,cur_date) 
  elif code in month6_list:
      cur_date = '2019/06'
      select_low_val_sql = "select code,name,per_배율,date from bs_list where code='%s' and date='%s'"%(code,cur_date) 
  elif code in month9_list:
      cur_date = '2019/09'
      select_low_val_sql = "select code,name,per_배율,date from bs_list where code='%s' and date='%s'"%(code,cur_date) 
  elif code in month11_list:
      cur_date = '2019/11'
      select_low_val_sql = "select code,name,per_배율,date from bs_list where code='%s' and date='%s'"%(code,cur_date) 
  else:
      cur_date = '2018/12'
      select_low_val_sql = "select code,name,per_배율,date from bs_list where code='%s' and date='%s'"%(code,cur_date) 
  #print(select_low_val_sql)
  cursor.execute(select_low_val_sql)
  select_sql = cursor.fetchall()

  """ select_sector_sql = "select code,name,sector from rank_corp where code='%s'"%(code)
  cursor.execute(select_sector_sql)
  select_sector_list = cursor.fetchall() """

  per = float(select_sql[0][2])

  update_sql = "update rank_corp set per=%s where code=%s"%(per,code)
  cursor.execute(update_sql)
  con.commit()

  count = count +1
  print(count)


con.close()