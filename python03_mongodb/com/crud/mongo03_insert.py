from pymongo import MongoClient

score = MongoClient('localhost', 27017).testDB.score

# db.score.insertOne({}); => MongoDB 명령어
'''
score.insert_one({
    'name':'조세오',
    'kor':50,
    'math':90,
    'eng':70
})
'''

# db.score.insertMany([{}, {}])
score.insert_many([
    {
        'name':'강호둥',
        'midterm':{'kor':100, 'eng':70, 'math':80},
        'finalterm':{'kor':90, 'eng':80, 'math':80}
    },
    {
        'name':'유재식',
        'midterm':{'kor':70, 'eng':90, 'math':100},
        'finalterm':{'kor':100, 'eng':70, 'math':80}
    }
])




