from pymongo import MongoClient

score = MongoClient('localhost', 27017).testDB.score

score.delete_one({'name':'lee'})
score.delete_many({'finalterm.eng':{'$lt':90}})
score.delete_many({})
