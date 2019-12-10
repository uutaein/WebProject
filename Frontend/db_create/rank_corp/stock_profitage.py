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


count=0
for i in code_list:
    #if count<770:
    #    continue
    code_name = i[1]
    code = i[0]
    
    if code in empty_list:
        continue
    if code in month3_list:
        cur_date = '2019/03'
        select_profitage_sql = "select code,name,자본총계_지배,당기순이익_지배,ROE_퍼센트,date from bs_list where date='%s' and code=%s"%(cur_date,code)
    elif code in month6_list:
        cur_date = '2019/06'
        select_profitage_sql = "select code,name,자본총계_지배,당기순이익_지배,ROE_퍼센트,date from bs_list where date='%s' and code=%s"%(cur_date,code)
    elif code in month9_list:
        cur_date = '2019/09'
        select_profitage_sql = "select code,name,자본총계_지배,당기순이익_지배,ROE_퍼센트,date from bs_list where date='%s' and code=%s"%(cur_date,code)
    elif code in month11_list:
        cur_date = '2019/11'
        select_profitage_sql = "select code,name,자본총계_지배,당기순이익_지배,ROE_퍼센트,date from bs_list where date='%s' and code=%s"%(cur_date,code)
    else:
        cur_date = '2018/12'
        select_profitage_sql = "select code,name,자본총계_지배,당기순이익_지배,ROE_퍼센트,date from bs_list where date='%s' and code=%s"%(cur_date,code)

    
    cursor.execute(select_profitage_sql)
    stocks_profitage_sql = cursor.fetchall()
    #print(stocks_profitage_sql)

    capital = int(stocks_profitage_sql[0][2])           #자본총계_지배
    net_income = int(stocks_profitage_sql[0][3])        #당기순이익
    roe_percent = stocks_profitage_sql[0][4]            #ROE_퍼센트
    try:
        roi_percent = round((net_income / capital)*100,4)   #ROI_퍼센트
        profitage = round(roe_percent/roi_percent,4)        #수익성( ROE/ROI )
    except ZeroDivisionError:
        roi_percent = 0
        profitage = 0

    #print(type(roe_percent))
    """ if code in empty_list:
        continue
    if code in month3_list:
        cur_date = '2019/03'
        update_roi_sql = "update bs_list set ROI_퍼센트=%s where code=%s and date='%s'"%(roi_percent,code,cur_date)
        update_sql = "update rank_corp set profitage=%s where code=%s and settle_date='%s'"%(profitage,code,cur_date)
    elif code in month6_list:
        cur_date = '2019/06'
        update_roi_sql = "update bs_list set ROI_퍼센트=%s where code=%s and date='%s'"%(roi_percent,code,cur_date)
        update_sql = "update rank_corp set profitage=%s where code=%s and settle_date='%s'"%(profitage,code,cur_date)
    elif code in month9_list:
        cur_date = '2019/09'
        update_roi_sql = "update bs_list set ROI_퍼센트=%s where code=%s and date='%s'"%(roi_percent,code,cur_date)
        update_sql = "update rank_corp set profitage=%s where code=%s and settle_date='%s'"%(profitage,code,cur_date)
    elif code in month11_list:
        cur_date = '2019/11'
        update_roi_sql = "update bs_list set ROI_퍼센트=%s where code=%s and date='%s'"%(roi_percent,code,cur_date)
        update_sql = "update rank_corp set profitage=%s where code=%s and settle_date='%s'"%(profitage,code,cur_date)
    else:
        cur_date = '2018/12'
        update_roi_sql = "update bs_list set ROI_퍼센트=%s where code=%s and date='%s'"%(roi_percent,code,cur_date)
        update_sql = "update rank_corp set profitage=%s where code=%s and settle_date='%s'"%(profitage,code,cur_date) 

    print(update_sql)
    print(update_roi_sql)
    cursor.execute(update_roi_sql)
    cursor.execute(update_sql)
    con.commit()"""

    if code in empty_list:
        continue
    if code in month3_list:
        cur_date = '2019/03'
        update_sql = "update rank_corp set roe=%s where code=%s and settle_date='%s'"%(roe_percent,code,cur_date)
    elif code in month6_list:
        cur_date = '2019/06'
        update_sql = "update rank_corp set roe=%s where code=%s and settle_date='%s'"%(roe_percent,code,cur_date)
    elif code in month9_list:
        cur_date = '2019/09'
        update_sql = "update rank_corp set roe=%s where code=%s and settle_date='%s'"%(roe_percent,code,cur_date)
    elif code in month11_list:
        cur_date = '2019/11'
        update_sql = "update rank_corp set roe=%s where code=%s and settle_date='%s'"%(roe_percent,code,cur_date)
    else:
        cur_date = '2018/12'
        update_sql = "update rank_corp set roe=%s where code=%s and settle_date='%s'"%(roe_percent,code,cur_date)

    cursor.execute(update_sql)
    con.commit()

    count = count +1
    print(count) 

con.close()