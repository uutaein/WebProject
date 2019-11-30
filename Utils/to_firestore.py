# -*- coding: utf-8 -*-
import csv
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import pandas as pd

cred = credentials.Certificate("webproject.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

file_path = "StockInfo.csv"
collection_name = "StockInfo"

csv_df = pd.read_csv("StockInfo.csv")
csv_df = csv_df[['종목코드','종목명','산업분류','시장구분']]
print(csv_df.head(10))

def search_details(codename, dataframe):
    for i in range(len(dataframe)):
        if dataframe
    print(dataframe.iloc[0,1])
    print(len(dataframe))
    print(len(dataframe.columns))

search_details('X005930',csv_df)

# def batch_data(iterable, n=1):
#     l = len(iterable)
#     for ndx in range(0, l, n):
#         yield iterable[ndx:min(ndx + n, l)]


# data = []
# headers = []
# with open(file_path) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             for header in row:
#                 headers.append(header)
#             line_count += 1
#         else:
#             obj = []
#             obj2 = {}
#             for idx, item in enumerate(row):
                
#                 #obj[headers[idx]] = item
#                 obj2['value'] = item
#                 obj2['code'] = headers[idx]
#                 #obj2['name'] = 이름?
#                 #obj2['market'] = 코스피?
#                 #obj2['산업분류'] = 산업분류?
#                 obj.append(obj2)
#             data.append(obj)
#             line_count += 1
#     print(f'Processed {line_count} lines.')

# for batched_data in batch_data(data, 200):
#     batch = store.batch()
#     for data_item in batched_data:
#         doc_ref = store.collection('stockinfo').document()
#         batch.set(doc_ref, data_item)
#     batch.commit()

# print('Done')