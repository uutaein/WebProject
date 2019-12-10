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
  #if count>3:
  #  break
  code_name = i[1]
  code = i[0]
  
  select_sql = "select date,close,volume from c%s order by date desc limit 1,20"%(code)
  cursor.execute(select_sql)
  select_sql = cursor.fetchall()

  #최근 20일 거래량 평균
  volume_sum = 0
  for i in range(len(select_sql)):
    volume = select_sql[i][2]
    volume_sum = volume_sum + volume
 
  insert_volume = round(float(volume_sum/20),2)
  #print(code)
  #print(volume_sum)

  update_sql = "update rank_corp set volume=%s where code=%s"%(float(insert_volume),code)
  print(update_sql)
  cursor.execute(update_sql)
  con.commit()

  count = count +1
  print(count)


con.close()