import requests # 웹 페이지 소스를 얻기 위한 패키지(기본 내장 패키지이다.)
from bs4 import BeautifulSoup # 웹 페이지 소스를 얻기 위한 패키지, 더 간단히 얻을 수 있다는 장점이 있다고 한다.
from datetime import datetime                                # (!pip install beautifulsoup4 으로 다운받을 수 있다.)
import pandas as pd # 데이터를 처리하기 위한 가장 기본적인 패키지
import time # 사이트를 불러올 때, 작업 지연시간을 지정해주기 위한 패키지이다. (사이트가 늦게 켜지면 에러가 발생하기 때문)
import urllib.request #
from selenium import webdriver
import json
import re     
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt
import pymysql
from sqlalchemy import create_engine
import numpy as np
import os
import openpyxl

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=os.path.abspath("C:\\Users\\enjoy\\chromedriver.exe"))
#browser  = webdriver.Chrome()
#browser.maximize_window()

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



data_list = dict()
sector_arr = []
sector_number = [100,110,200,210,220,230,240,250,260,300,310,320,330,340,400,410,500,510,520,600,610,620,630,640,700,800]
for i in sector_number:
  base_url = "http://www.wiseindex.com/Index/GetIndexComponets?ceil_yn=0&dt=20191206&sec_cd=WI"+str(i)

  response = urllib.request.urlopen(base_url)

  data = json.loads(response.read())

  
  #print(len(data["list"]))
  sector_name = data["list"][0]["IDX_NM_KOR"]
  sector_name = sector_name[5:]
  sector_arr.append(sector_name)
  arr =[]
  for i in range(0,len(data["list"])):  
    sector_corp_list = data["list"][i]["CMP_KOR"]
    arr.append(sector_corp_list)
    #print(data["list"][i]["CMP_KOR"])
  data_list[sector_name]=arr

new_dict = dict()
for i in range(0,len(sector_arr)):
  curr_sector = sector_arr[i]
  for i in range(0,len(data_list[curr_sector])):  
    #print(data_list[curr_sector][i])
    new_dict[data_list[curr_sector][i]]=curr_sector

df = pd.DataFrame(new_dict,index=[0]).T

#df.to_excel('list2.xlsx')

xlsx_data = openpyxl.load_workbook('list2.xlsx')
ws = xlsx_data.active

sector_df = []
for row in ws.rows:
  sector_df.append([row[0].value,row[1].value,row[2].value])

del sector_df[0]
print(len(sector_df))

count=0  
for i in range(len(sector_df)):
  code = sector_df[i][0]
  sector = sector_df[i][2]
  update_sql = "update rank_corp set sector='%s' where code='%s'"%(sector,code)
  print(update_sql)
  cursor.execute(update_sql)
  con.commit()
  count = count+1
  print(count)