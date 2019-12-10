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
import datetime as dt
import pymysql
from sqlalchemy import create_engine
import numpy as np


#driver = webdriver.Chrome('c:/Users/enjoy/chromedriver.exe')

browser  = webdriver.Chrome()
browser.maximize_window()

con = pymysql.connect(host='db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com', user='admin',password='adminroot',db='stockdb',charset='utf8')
engine = create_engine("mysql+pymysql://admin:"+"adminroot"+"@db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com/stockdb?charset=utf8",encoding='utf-8')
conn = engine.connect()



cursor = con.cursor()
cursor.execute("set names utf8")
con.commit()


def stock_crawler(code):
    #code = 종목번호
    name = code
    base_url = 'https://finance.naver.com/item/coinfo.nhn?code='+ name + '&target=finsum_more'
    
    browser.get(base_url)
    #frmae구조 안에 필요한 데이터가 있기 때문에 해당 데이터를 수집하기 위해서는 frame구조에 들어가야한다.
    browser.switch_to_frame(browser.find_element_by_id('coinfo_cp'))
    
    #재무제표 "연간" 클릭하기
    browser.find_elements_by_xpath('//*[@class="schtab"][1]/tbody/tr/td[3]')[0].click()

    html0 = browser.page_source
    html1 = BeautifulSoup(html0,'html.parser')
    
    #기업명 뽑기
    title0 = html1.find('head').find('title').text
    print(title0.split('-')[-1])
    
    html22 = html1.find('table',{'class':'gHead01 all-width','summary':'주요재무정보를 제공합니다.'})
    
    #date scrapy
    thead0 = html22.find('thead')
    tr0 = thead0.find_all('tr')[1]
    th0 = tr0.find_all('th')
    
    date = []
    for i in range(len(th0)):
        date.append(''.join(re.findall('[0-9/]',th0[i].text)))

    #print(date)
    
    #columns scrapy
    tbody0 = html22.find('tbody')
    tr0 = tbody0.find_all('tr')
    
    col = []
    for i in range(len(tr0)):

        if '\xa0' in tr0[i].find('th').text:
            tx = re.sub('\xa0','',tr0[i].find('th').text)
        else:
            tx = tr0[i].find('th').text

        col.append(tx)
    
    
    #main text scrapy
    td = []
    for i in range(len(tr0)):
        td0 = tr0[i].find_all('td')
        td1 = []
        for j in range(len(td0)):
            if td0[j].text == '':
                td1.append(0)
            else:
                td1.append(float(td0[j].text.replace(',','')))
        td.append(td1)
    
    td2 = list(map(list,zip(*td)))
    
    pd_new =pd.DataFrame(td2,columns = col)
    
    pd_new.insert(loc=0,column='date',value = date)
    return pd_new


#crawler = stock_crawler('023530')

# mysql 'code_list' 테이블에서 종목코드(코스피) 가져오기
sql = "select * from code_list where market='0'"
cursor.execute(sql)
code_list = cursor.fetchall()


code_list_column = ['code','name','market']
df = pd.DataFrame(code_list,columns=code_list_column)


#종목코드별 재무제표 정보 저장 테이블 생성
create_sql = "create table bs_list("\
             "code varchar(50),"\
             "name varchar(50),"\
             "date varchar(50),"\
             "매출액 long,"\
             "영업이익 long,"\
             "영업이익_발표기준 long,"\
             "세전계속사업이익 long,"\
             "당기순이익 long,"\
             "당기순이익_지배 long,"\
             "당기순이익_비지배 long,"\
             "자산총계 long,"\
             "부채총계 long,"\
             "자본총계 long,"\
             "자본총계_지배 long,"\
             "자본총계_비지배 long,"\
             "자본금 long,"\
             "영업활동현금흐름 long,"\
             "투자활동현금흐름 long,"\
             "재무활동현금흐름 long,"\
             "CAPEX long,"\
             "FCF long,"\
             "이자발생부채 long,"\
             "영업이익률 float,"\
             "순이익률 float,"\
             "ROE_퍼센트 float,"\
             "ROA_퍼센트 float,"\
             "부채비율 float,"\
             "자본유보율 float,"\
             "EPS_원 long,"\
             "PER_배율 float,"\
             "BPS_원 long,"\
             "PBR_배율 float,"\
             "현금DPS_원 long,"\
             "현금배당수익률 float,"\
             "현금배당성향_퍼센트 float,"\
             "발행주식수_보통주 long)"

print(create_sql)
cursor.execute(create_sql)
con.commit()



count = 0
for i in df.index:

  code = df.get_value(i,'code')
  code_name = df.get_value(i,'name')
  crawler = stock_crawler(code)
  crawler.insert(loc=0,column='code', value=code)
  crawler.insert(loc=1,column='name',value=code_name)
  crawler = crawler.rename(columns={'영업이익(발표기준)':'영업이익_발표기준',\
                                    '당기순이익(지배)':'당기순이익_지배',\
                                    '당기순이익(비지배)':'당기순이익_비지배',\
                                    '자본총계(지배)':'자본총계_지배',\
                                    '자본총계(비지배)':'자본총계_비지배',\
                                    'ROE(%)':'ROE_퍼센트',\
                                    'ROA(%)':'ROA_퍼센트',\
                                    'EPS(원)':'EPS_원',\
                                    'PER(배)':'PER_배율',\
                                    'BPS(원)':'BPS_원',\
                                    'PBR(배)':'PBR_배율',\
                                    '현금DPS(원)':'현금DPS_원',\
                                    '현금배당성향(%)':'현금배당성향_퍼센트',\
                                    '발행주식수(보통주)':'발행주식수_보통주'})
  crawler[['매출액','영업이익','영업이익_발표기준','세전계속사업이익','당기순이익','당기순이익_지배','당기순이익_비지배',\
          '자산총계','부채총계','자본총계','자본총계_지배','자본총계_비지배','자본금','영업활동현금흐름','투자활동현금흐름','재무활동현금흐름',\
          'CAPEX','FCF','이자발생부채','EPS_원','BPS_원','현금DPS_원','발행주식수_보통주']] =\
  crawler[['매출액','영업이익','영업이익_발표기준','세전계속사업이익','당기순이익','당기순이익_지배','당기순이익_비지배',\
          '자산총계','부채총계','자본총계','자본총계_지배','자본총계_비지배','자본금','영업활동현금흐름','투자활동현금흐름','재무활동현금흐름',\
          'CAPEX','FCF','이자발생부채','EPS_원','BPS_원','현금DPS_원','발행주식수_보통주']].astype(np.long)
  time.sleep(0.5)
  count = count + 1
  print("count: ",count)
  #print(crawler)
  
  crawler.to_sql(name='bs_list',con=engine, if_exists='append',index=False)

con.close()

'''
count = 0
for i in df.index:
  if count>2:
    break
  code = df.get_value(i,'code')
  #code_name = df.get_value(i,'name')
  crawler = stock_crawler(code)
  count = count +1
  print(crawler)
    '''
print("끝")