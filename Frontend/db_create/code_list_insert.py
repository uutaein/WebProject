import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import dart_fss as dart
import urllib.parse

api_key ='584626469376cfe0ab051018212582a3c59699f5'
dart.dart_set_api_key(api_key=api_key)

MARKET_CODE_DICT = {
    'kospi': 'stockMkt',
    'kosdaq': 'kosdaqMkt',
    'konex': 'konexMkt'
}
DOWNLOAD_URL = 'kind.krx.co.kr/corpgeneral/corpList.do'

con = pymysql.connect(host='db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com', user='admin',password='adminroot',db='stockdb',charset='utf8')
engine = create_engine("mysql+pymysql://admin:"+"adminroot"+"@db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com/stockdb?charset=utf8",encoding='utf-8')
conn = engine.connect()


MARKET_KOSPI = 0
MARKET_KOSDAQ = 10


cursor = con.cursor()
cursor.execute("set names utf8")
con.commit()


def download_stock_codes(market=None,delisted=False):
  params = {'method': 'download'}

  if market.lower() in MARKET_CODE_DICT:
    params['marketType'] = MARKET_CODE_DICT[market]
  if not delisted:
    params['searchType'] = 13

  params_string = urllib.parse.urlencode(params)
  request_url = urllib.parse.urlunsplit(['http',DOWNLOAD_URL,'',params_string,''])

  df = pd.read_html(request_url, header=0)[0]
  df.종목코드 = df.종목코드.map('{:06d}'.format)

  return df

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)

    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
      code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
      return code_name

    def get_code_list(self):
      self.kospi_codes = self.kiwoom.get_code_list_by_market(MARKET_KOSPI)
      self.kosdaq_codes = self.kiwoom.get_code_list_by_market(MARKET_KOSDAQ)

if __name__ == "__main__":
  '''
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()

    code_list = kiwoom.get_code_list_by_market(MARKET_KOSPI)
    for code in code_list:
      code_name = kiwoom.get_master_code_name(code)
      print("code: ",code," code_name: ",code_name)
  '''
  kospi_stocks = download_stock_codes('kospi')
  kosdaq_stocks = download_stock_codes('kosdaq')
  
  df_kospi = pd.DataFrame(kospi_stocks[['종목코드','회사명']])
  df_kosdaq = pd.DataFrame(kosdaq_stocks[['종목코드','회사명']])
  
  # 0:코스피_상장법인 1:코스닥_상장법인
  df_kospi['market'] = 0
  df_kosdaq['market'] = 1
  df_all = pd.concat([df_kospi,df_kosdaq])
  
  df_all.rename(columns={'종목코드':'code','회사명':'name'},inplace=True)

  create_sql = "create table code_list ("\
               "code varchar(50),"\
               "name varchar(100),"\
               "market int)"

  print(create_sql)
  cursor.execute(create_sql)
  con.commit()

  df_all.to_sql(name='code_list', con=engine, if_exists='append',index=False)
  
  
      