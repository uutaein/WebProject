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
import os
import openpyxl

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



#momentum_3m_profitage rank
select_rank_percent_sql ="""
    select code,name,sector,low_val,rnum
from(
	select a.*,
		(case @vsector when a.sector then @rownum:=@rownum+1 else @rownum:=1 end) rnum, 
        (@vsector:=a.sector) vsector
from rank_corp a, (select @vsector:='', @rownum:=0 from dual) b
order by a.sector, a.low_val desc) c;
    """
cursor.execute(select_rank_percent_sql)
rank_str = cursor.fetchall()


xlsx_data = openpyxl.load_workbook('list_low_val.xlsx')
ws = xlsx_data.active

sector_df = []
for row in ws.rows:
  sector_df.append([row[0].value,row[1].value,row[2].value,row[3].value,row[4].value,row[5].value])

del sector_df[0]
print(len(sector_df))

select_sql_low_val = "select code,name,sector,low_val,low_val_rank_percent from rank_corp"
cursor.execute(select_sql_low_val)
rank_str = cursor.fetchall()

count=0  
for i in range(len(rank_str)):
  code = rank_str[i][0]
  if rank_str[i][4] is None:
    continue
  sector_low_val_rank = round(float(rank_str[i][4]),3)
  percent_rank = sector_low_val_rank * 100
  
  #print(rank_str[i])

  if percent_rank >80:
      percent_rank_score = 1
  elif percent_rank >60:
      percent_rank_score = 2
  elif percent_rank >40:
      percent_rank_score = 3
  elif percent_rank >20:
      percent_rank_score = 4
  else:
      percent_rank_score = 5

  update_sql = "update rank_corp set low_val_rank='%s' where code='%s'"%(percent_rank_score,code)
  cursor.execute(update_sql)
  con.commit()
  count = count+1
  print(count)

con.close()