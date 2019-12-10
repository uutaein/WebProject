import pymongo
import json
from bson.json_util import loads,dumps

conn = pymongo.MongoClient('127.0.0.1',27017)


db = conn.stockDB  #testDB 데이터베이스 생성
collection = db.stock_sise #testTable 테이블 생성
db = conn.get_database('stockDB')
collection = db.get_collection('stock_sise')
#collection.insert_one({"number":0})


with open('stock_sise_test.json','r') as data_file:
  json_data = json.load(data_file)
  #dump_json_data = json.dumps(json_data)

print(type(json_data))
#print(type(dump_json_data))

collection.delete_many({})
collection.insert_many(json_data)

#collection.find().pretty()
#칼럼명 삽입 먼저 하고 value값 저장?
#df_json_list = json.loads(df_json).values()
#collection.insert_many(df_json_list)