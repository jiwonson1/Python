import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.iei.or.kr/edu/curriculumList.kh?no=2')
soup = BeautifulSoup(html.text, 'html.parser')
#print(soup)

# select == 선택자를 이용해서
#result = soup.select('.content_box .sub_tit2') # select_one()

# find == 태그를 기준으로 해서
result = soup.find_all('p', class_='sub_tit2')

#print(result)
for el in result:
    print(el.text)
