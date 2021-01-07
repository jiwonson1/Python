from pymongo import MongoClient

score = MongoClient('localhost', 27017).testDB.score

# name이 유재식인거 하나 찾아서 midterm의 kor값을 100으로 변경
'''
    update score
       set midterm.kor = 100
     where name = '유재식'
'''
score.update_one(
    {'name':'유재식'},
    {'$set':{'midterm.kor':100}}
)


# midterm.eng값이 95보다 작은 document들을 찾아서 midterm.eng값을 100으로 변경
score.update_many(
    {'midterm.eng':{'$lt':95}},
    {'$set':{'midterm.eng':100}}
)