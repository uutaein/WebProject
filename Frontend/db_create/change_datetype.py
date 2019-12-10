import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import datetime
import time

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


count = 0

'''
for i in code_list:
  
  #주어진 조건에 해당되는 테이블 개수 확인
  changeType_sql = "alter table c"+i[0]+" modify date datetime"
  print(changeType_sql)
  cursor.execute(changeType_sql)
  con.commit()

change_bs_list = "매출액,영업이익,영업이익_발표기준,세전계속사업이익,당기순이익,당기순이익_지배,당기순이익_비지배,자산총계,부채총계,자본총계,자본총계_지배,자본총계_비지배,자본금,영업활동현금흐름,투자활동현금흐름,재무활동현금흐름,CAPEX,FCF,이자발생부채,EPS_원,BPS_원,현금DPS_원,발행주식수_보통주"
change_bs_list = change_bs_list.split(",")
lst_bs = list(change_bs_list)


for i in lst_bs:
  change_int_sql = "alter table bs_list modify "+i+" bigint"
  print(change_int_sql)
  cursor.execute(change_int_sql)
  con.commit()


bs_list_sql = "select * from bs_list where code=005930"
cursor.execute(bs_list_sql)
ex = cursor.fetchall()
print(ex)
'''
create_column_sql = "alter table code_list add start_date varchar(50)"
cursor.execute(create_column_sql)
con.commit()


for i in code_list:
  if count>3:
    break
  code_name = i[1]
  code = i[0]
  
  sql_test = "select * from c"+code+" where date between '2019-09-01' and '2019-11-26"
  cursor.execute(sql_test)
  sql = cursor.fetchall()
  print(type(sql))
  
  #startDate = sql[0][0]
  #str_startDate = startDate.date().isoformat()

  #cursor.execute('update code_list set start_date=%s where code=%s', (str_startDate,code))
  #con.commit()
  count = count+1
  print(count)

#alter_sql = "alter table code_list modify start_date datetime"
#cursor.execute(alter_sql)
#con.commit()
con.close()