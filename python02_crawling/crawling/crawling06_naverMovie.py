import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

'''
    https://movie.naver.com/movie/running/current.nhn
    현재 상영중인 영화들의 제목, 평점 긁어오기

    {'title':xxxxx, 'star':xx.x}
    {'title':xxxxx, 'star':xx.x}
    ...
'''
movieCollection = MongoClient('localhost', 27017).boramDB.movieCollection

html = requests.get('https://movie.naver.com/movie/running/current.nhn')
soup = BeautifulSoup(html.text, 'html.parser')

# 각 영화들의 정보를 담고 있는 dl요소들 가지고 오기
#movies = soup.select('dl.lst_dsc')
movies = soup.find_all('dl', class_='lst_dsc')

for movie in movies: # movie == 순차적으로 접근되는 dl요소
    # 영화제목, 영화평점
    title = movie.find('a').text
    star = movie.find('span', class_='num').text
    #print({'title':title, 'star':float(star)})
    movieCollection.insert_one({'title':title, 'star':float(star)})


