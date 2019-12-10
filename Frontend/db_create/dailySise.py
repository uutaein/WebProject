import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import time
import pandas as pd
#import json
#import pymongo
import sqlite3
import pymysql
from sqlalchemy import create_engine


TR_REQ_TIME_INTERVAL = 0.4
MARKET_KOSPI = 0
MARKET_KOSDAQ = 10

con = pymysql.connect(host='db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com', user='admin',password='adminroot',db='stockdb',charset='utf8')

#pymysql.install_as_MySQLdb()
#import MySQLdb

engine = create_engine("mysql+pymysql://admin:"+"adminroot"+"@db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com/stockdb?charset=utf8",encoding='utf-8')
conn = engine.connect()

cursor = con.cursor()
cursor.execute("set names utf8")
con.commit()

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
  # OpenAPI 메서드
  #  Tran 입력 값을 서버통신 전에 입력한다.
  #  ex) openApi.SetInputValue("종목코드", "005930")
  def set_input_value(self, id, value):
    self.dynamicCall("setInputValue(QString, QString)", id, value)

  # Tran을 서버로 송신
  def comm_rq_data(self, rqname, trcode, next, screen_no):
    self.dynamicCall("commRqData(QString, QString, int, QString",rqname, trcode, next, screen_no)
    self.tr_event_loop = QEventLoop()
    self.tr_event_loop.exec_()

  #키움서버에 TR요청시 한번에 여러개의 데이터 반환됨
  #데이터 받는 입장에서 총 몇개의 데이터 왔는지 확인위해
  # GetRepeatCnt메소드 사용
  def _get_repeat_cnt(self, trcode, rqname):
    ret = self.dynamicCall("GetRepeatCnt(QString,QString)", trcode, rqname)
    return ret

  # 서버로부터 TR처리에 대한 이벤트 발생했을때 실제 데이터 가져오기위한 메서드
  def _comm_get_data(self, code, real_type, field_name, index, item_name):
    ret = self.dynamicCall("CommGetData(QString, QString, QString, int, QString", code, real_type, field_name, index, item_name)
    return ret.strip()

  # 이벤트 발생시 처리하는 메서드
  # 고려사항
  # 1. 모든 TR요청에 대해 아래 메소드에서 모두 처리하므로 rqname인자를 통해 TR구분
  # 2. 연속조회 처리 다년의 일봉데이터 요청시 한번의 요청으로 받기 힘드므로 prevNext값의 숫자로 구분
  # 3. receive_tr_data 메서드 호출의 의미는 프로그램이 정상적인 대기상태에서 OnReceiveTrData 이벤트를 받은것을 의미
  #    따라서 이벤트 루프를 종료한다.
  def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
    # 연속으로 조회한다면
    if next == '2':
      self.remained_data = True
    else:
      self.remained_data = False
    
    # 여러 종류의 TR요청을 rqname인자로 TR구분
    # _opt10081 메서드에서 처리
    if rqname == "opt10081_req":
      self._opt10081(rqname, trcode)

    try:
      self.tr_event_loop.exit()
    except AttributeError:
      pass


  def _set_signal_slots(self):
    self.OnEventConnect.connect(self._event_connect)
    self.OnReceiveTrData.connect(self._receive_tr_data)
  
  # 데이터 얻어오기 전에 먼저 데이터의 개수를 _get_repeat_cnt 메서드를 통해 얻어옴
  def _opt10081(self, rqname, trcode):
    data_cnt = self._get_repeat_cnt(trcode, rqname)
  
    for i in range(data_cnt):
      date = self._comm_get_data(trcode, "", rqname, i,"일자")
      open = self._comm_get_data(trcode, "", rqname,i,"시가")
      high = self._comm_get_data(trcode, "", rqname,i,"고가")
      low = self._comm_get_data(trcode, "", rqname,i,"저가")
      close = self._comm_get_data(trcode, "", rqname,i,"현재가")
      volume = self._comm_get_data(trcode, "", rqname,i,"거래량")
      
      #df에 저장 
      self.ohlcv['date'].append(date)
      self.ohlcv['open'].append(int(open))
      self.ohlcv['high'].append(int(high))
      self.ohlcv['low'].append(int(low))
      self.ohlcv['close'].append(int(close))
      self.ohlcv['volume'].append(int(volume))

if __name__ == "__main__":
  app = QApplication(sys.argv)
  kiwoom = Kiwoom()
  kiwoom.comm_connect()


  kiwoom.ohlcv = {'date':[], 'open':[], 'high':[], 'low':[], 'close':[], 'volume':[]}

  code_list = kiwoom.get_code_list_by_market(MARKET_KOSPI)
  #종목 리스트 분할
  n=30  
  divide_code_list = [code_list[i*n:(i+1)*n] for i in range((len(code_list)+ n -1)//n)]
  #30개들이 리스트 53개 있음
  
  #db저장 진행상황 count
  
  print(len(divide_code_list))
  #len(divide_code_list)

  #API과다사용시 connection 끊으므로 10개씩 데이터 저장
  # range(0,10) / range(10,20) / range(20,30) / range(30,40) / range(40, 54)
  whole_count = 50
  for i in range(50,len(divide_code_list)):
    
    print(divide_code_list[i])
    #분할된 리스트 내부 종목당 count
    divide_list_count = 0

    for code in divide_code_list[i]:
      #code = "039490"
      code_name = kiwoom.get_master_code_name(code)
      
      create_sql = "create table c"+code+" ("\
            "date varchar(50),"\
            "open int,"\
            "high int,"\
            "low int,"\
            "close int,"\
            "volume int)"
      print(create_sql)
      cursor.execute(create_sql)
      con.commit()
      
      # opt10081 TR요청
      kiwoom.set_input_value("종목코드", code)
      kiwoom.set_input_value("기준일자", "20191126")
      kiwoom.set_input_value("수정주가구분",1)
      kiwoom.comm_rq_data("opt10081_req", "opt10081", 0, "0101")

      while kiwoom.remained_data == True:
        time.sleep(TR_REQ_TIME_INTERVAL)
        kiwoom.set_input_value("종목코드", code)
        kiwoom.set_input_value("기준일자", "20191126")
        kiwoom.set_input_value("수정주가구분", 1)
        kiwoom.comm_rq_data("opt10081_req", "opt10081", 2, "0101")

      df = pd.DataFrame(kiwoom.ohlcv, columns =['date','open','high','low','close','volume'])
      kiwoom.ohlcv = {'date':[], 'open':[], 'high':[], 'low':[], 'close':[], 'volume':[]}
      divide_list_count = divide_list_count + 1
      print("전체리스트: ",whole_count," 분할리스트 카운트: ",divide_list_count)

      df.to_sql(name='c'+code, con=engine, if_exists='append',index=False)
      
      time.sleep(0.8)
      
    whole_count = whole_count + 1


  print("파일 끝")

  con.close()
