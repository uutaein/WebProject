import pandas_datareader as wb
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import pymysql
from sqlalchemy import create_engine

pd.set_option('precision',4)
con = pymysql.connect(host='db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com', user='admin',password='adminroot',db='stockdb',charset='utf8')
engine = create_engine("mysql+pymysql://admin:"+"adminroot"+"@db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com/stockdb?charset=utf8",encoding='utf-8')
conn = engine.connect()

cursor = con.cursor()
cursor.execute("set names utf8")
con.commit()


start = datetime.datetime(2000,1,1)
end = datetime.datetime(2019,11,26)
df_null = wb.DataReader("^KS11","yahoo",start,end)
df = df_null.dropna()

#print(df)
#print(df.index.dtype)
df = df.rename(columns={'High':'high',\
                        'Low':'low',\
                        'Open':'open',\
                        'Close':'close',\
                        'Volume':'volume'
                        })
df = df.drop('Adj Close',axis=1)

df.insert(loc=0,column='date',value = df.index)

df_new = pd.DataFrame(df)
df_new = df_new.reset_index(drop=True)
#print(df_new)

create_sql = "create table ckospi_index ("\
            "date datetime,"\
            "high float,"\
            "low float,"\
            "open float,"\
            "close float,"\
            "volume float)"
print(create_sql)
cursor.execute(create_sql)
con.commit()

df_new.to_sql(name='ckospi_index', con=engine, if_exists='append',index=False)

print("파일끝")
#con.close()
