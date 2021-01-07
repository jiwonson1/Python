import matplotlib.pyplot as plt
from pymongo import MongoClient

# 각 장르별 웹툰 갯수 파이차트

webtoonCollection = MongoClient('localhost', 27017).boramDB.webtoonCollection

genreList = ['daily', 'comic', 'fantasy', 'action', 'drama', 'pure', 'sensibility', 'thrill', 'historical', 'sports']
webCount = [] # 각 장르별 웹툰수 담기

for genre in genreList:
    genreCount = webtoonCollection.count_documents({'genre':genre})
    webCount.append(genreCount)

#print(webCount)
#plt.bar(genreList, webCount)
plt.pie(webCount, labels=genreList, autopct="%.1f%%")
plt.show()







