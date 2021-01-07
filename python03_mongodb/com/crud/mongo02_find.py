from pymongo import MongoClient
import pprint

score = MongoClient('localhost', 27017).testDB.score

cursor = score.find()

for doc in cursor:
    pprint.pprint(doc)

print('------------------------------------------')

print('document들의 총 갯수 :', score.count_documents({}))

print('------------------------------------------')

leeCursor = score.find({'name':'lee'}) # 조회된 document가 몇개든 간에 Cursor
for doc in leeCursor:
    pprint.pprint(doc)

print('------------------------------------------')

hong = score.find_one({'name':'hong'})
pprint.pprint(hong)
print('name이 hong인 document의 갯수 :', score.count_documents({'name':'hong'}))

print('------------------------------------------')

cursor = score.find({'kor':{'$gt':60}})
for doc in cursor:
    pprint.pprint(doc)