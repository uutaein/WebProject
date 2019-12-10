# -*- coding: utf-8 -*-
import pandas as pd 
import requests
from bs4 import BeautifulSoup
import pymongo
import json
import time

conn = pymongo.MongoClient('127.0.0.1',27017)

db = conn.stockDB  #testDB 데이터베이스 생성
collection = db.stockTable #testTable 테이블 생성

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0] 


# 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌 
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format) 

#print(list(code_df))
#print(len(list(code_df)))
# 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다. 
code_df = code_df[['회사명', '종목코드']] 

# 한글로된 컬럼명을 영어로 바꿔준다. 
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'}) 


#뷰티풀 수프로 끝페이지 크롤링
def get_lastpage(item_name,code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    code = code.lstrip()
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    nyam = str(soup.select('.pgRR > a')[0])
    startpoint = nyam.find(";") + 6
    endpoint = nyam.find(">") - 1
    lastpage = int(nyam[startpoint:endpoint])
    return lastpage




# 종목 이름을 입력하면 종목에 해당하는 코드를 불러와
# 네이버 금융(http://finance.naver.com)에 넣어줌
def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    code = code.lstrip()
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
    
    print("요청 URL = {}".format(url))
    return url
    

# 신라젠의 일자데이터 url 가져오기
with open('test.json',"r") as f:
  json_data = json.load(f)

stock_sise = dict()
df = pd.DataFrame()

#print(len(json_data["data"]))
count =0
#전체 주식 코드 불러오기
for i in range(0,3):
  item_name = json_data["data"][i]["name"]
  item_code = json_data["data"][i]["code"]
  stock_sise[item_code]=''
  # 마지막 page 가져오기
  last_page = get_lastpage(item_name,code_df) + 1
  url = get_url(item_name, code_df)
  
  #stock_sise = {item_code:''}
  #df_stock_sise = pd.DataFrame(stock_sise)
  #df = pd.DataFrame()
  
  #개별 주식의 일별 시세 df에 저장
  for page in range(1,3):
    pg_url = '{url}&page={page}'.format(url=url, page=page)
    df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True,sort=True)
    
    #print(pg_url)
    time.sleep(0.01)
  
  df = df.dropna()
  df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff',\
    '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})

# 데이터의 타입을 int형으로 바꿔줌. 
# \(역슬래쉬)는 뒤에 데이터가 이어진다는 의미이다. 한줄로 쓰면 \ 필요없음.

  #df[['close', 'diff', 'open', 'high', 'low', 'volume']]\
  #  = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)
  #df['date'] = pd.to_datetime(df['date'])
  #df = df.sort_values(by=['date'], ascending=True)
  print(df)
  dict_df = df.to_dict('records')
  #stock_sise[item_code]=dict_df
  count +=1
  print(count)
  
  
#CONVERT dictionary to json
#with open('stock_sise.json','w', encoding="utf-8") as make_file:
#  json.dump(stock_sise,make_file, indent=2)

  #print(stock_sise.values())
  #df_stock_sise[item_code] = df_stock_sise[item_code].append(df)
  

#print(df.columns)
#df_to_json = df.to_json('stock.json', orient='records')
#new_data = pd.read_json('test.json',orient='records')
#item_name='삼성전자'

# 마지막 page 가져오기
#last_page = get_lastpage(item_name,code_df) + 1

#url = get_url(item_name, code_df)

# 일자 데이터를 담을 df라는 DataFrame 정의
#df = pd.DataFrame()

# 1페이지에서 20페이지의 데이터만 가져오기
#for page in range(1, last_page):
#    pg_url = '{url}&page={page}'.format(url=url, page=page)
#    df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
    
# df.dropna()를 이용해 결측값 있는 행 제거
#df = df.dropna()

# 최초 5개 데이터 확인하기
#print(df)
###############

#df.tail(5).to_json("C:\\Users\\enjoy\\WSL\\bs\\stock.json")
#df_json = df.tail(5).to_json()

#칼럼명 삽입 먼저 하고 value값 저장?
#df_json_list = json.loads(df_json).values()
#collection.insert_many(df_json_list)

