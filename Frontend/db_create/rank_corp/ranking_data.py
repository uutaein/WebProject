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



#momentum_3m_profitage rank
select_rank_percent_sql ="""
    select
	    c.code,c.name, c.momentum_3m_profitage, round(((@rank-rank)/@rank)*100,2) as percent_rank 
    from
        (select
            *,
            @prev:=@curr,
            @curr:=a.momentum_3m_profitage,
            @rank:=if(@prev = @curr, @rank, @rank +1) as rank
        from
            (select code, name,momentum_3m_profitage from rank_corp)as a,
            (select @curr:=null, @prev:=null,@rank:=0)as b
    order by momentum_3m_profitage asc) as c;
    """
cursor.execute(select_rank_percent_sql)
rank_str = cursor.fetchall()


for i in range(len(rank_str)):
    code = rank_str[i][0]
    momentum_3m_profitage = rank_str[i][2]
    percent_rank = float(rank_str[i][3])
    percent_rank = round(percent_rank,2)

    
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
    


    if code in empty_list:
        continue
    if code in month3_list:
        cur_date = '2019/03'
        update_sql = "update rank_corp set momentum_3m_profitage_rank_percent=%s where code=%s and settle_date='%s'"%(percent_rank,code,cur_date)
        update_rank_sql = "update rank_corp set momentum_3m_profitage_rank=%s where code=%s and settle_date='%s'"%(percent_rank_score,code,cur_date)
    elif code in month6_list:
        cur_date = '2019/06'
        update_sql = "update rank_corp set momentum_3m_profitage_rank_percent=%s where code=%s and settle_date='%s'"%(percent_rank,code,cur_date)
        update_rank_sql = "update rank_corp set momentum_3m_profitage_rank=%s where code=%s and settle_date='%s'"%(percent_rank_score,code,cur_date)
    elif code in month9_list:
        cur_date = '2019/09'
        update_sql = "update rank_corp set momentum_3m_profitage_rank_percent=%s where code=%s and settle_date='%s'"%(percent_rank,code,cur_date)
        update_rank_sql = "update rank_corp set momentum_3m_profitage_rank=%s where code=%s and settle_date='%s'"%(percent_rank_score,code,cur_date)
    elif code in month11_list:
        cur_date = '2019/11'
        update_sql = "update rank_corp set momentum_3m_profitage_rank_percent=%s where code=%s and settle_date='%s'"%(percent_rank,code,cur_date)
        update_rank_sql = "update rank_corp set momentum_3m_profitage_rank=%s where code=%s and settle_date='%s'"%(percent_rank_score,code,cur_date)
    else:
        cur_date = '2018/12'
        update_sql = "update rank_corp set momentum_3m_profitage_rank_percent=%s where code=%s and settle_date='%s'"%(percent_rank,code,cur_date)
        update_rank_sql = "update rank_corp set momentum_3m_profitage_rank=%s where code=%s and settle_date='%s'"%(percent_rank_score,code,cur_date)

    #print(update_sql)
    #print(update_rank_sql)
    cursor.execute(update_sql)
    #con.commit()
    cursor.execute(update_rank_sql)
    con.commit()

    count = count +1
    print(count)

con.close()