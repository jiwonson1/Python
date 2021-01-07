import matplotlib.pyplot as plt
from pymongo import MongoClient
import numpy

# 각 장르별 웹툰들의 평균 평점

webtoonCollection = MongoClient('localhost', 27017).boramDB.webtoonCollection

genreList = ['daily', 'comic', 'fantasy', 'action', 'drama', 'pure', 'sensibility', 'thrill', 'historical', 'sports']
avgStar = []

for genre in genreList:
    webCursor = webtoonCollection.find(
        {'genre':genre},
        {'star':True, '_id':False}
    )

    genreStarList = []
    for doc in webCursor:
        genreStarList.append(doc['star'])

    avgStar.append(numpy.average(genreStarList))

print(avgStar)

plt.plot(genreList, avgStar)
plt.xlabel('genre')
plt.ylabel('average star')
plt.show()