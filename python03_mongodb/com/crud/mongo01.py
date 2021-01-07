from pymongo import MongoClient
import pprint

'''
client = MongoClient('127.0.0.1', 27017)
db = client['testDB']
score = db['score']
'''

'''
client = MongoClient('localhost', 27017)
db = client.testDB
score = db.score
'''

score = MongoClient('localhost', 27017).testDB.score

result = score.find() # 조회된 document들이 담겨있는 Cursor 반환

#print(result)
for doc in result:
    pprint.pprint(doc)