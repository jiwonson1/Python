
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

'''
database name : boramDB
collection name : webtoonCollection
'''
webtoonCollection = MongoClient('localhost', 27017).boramDB.webtoonCollection

genreList = ['daily', 'comic', 'fantasy', 'action', 'drama', 'pure', 'sensibility', 'thrill', 'historical', 'sports']

for genre in genreList:
    html = requests.get('https://comic.naver.com/webtoon/genre.nhn?genre=' + genre)
    soup = BeautifulSoup(html.text, 'html.parser')

    webtoons = soup.select('ul.img_list dl')
    for webtoon in webtoons: # webtoon == dl
        # 웹툰명, 작가명, 평점
        title = webtoon.select_one('dt a').text
        author = webtoon.select_one('dd.desc a').text
        star = float(webtoon.select_one('div.rating_type strong').text)

        #print({'title':title, 'author':author, 'star':star, 'genre':genre})
        webtoonCollection.insert_one({'title':title, 'author':author, 'star':star, 'genre':genre})








