import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.iei.or.kr/intro/teacher.kh')
soup = BeautifulSoup(html.text, 'html.parser')

arr = soup.select('.intro_list .intro_txt')
#print(arr)
for el in arr:
    # 강사명, 제목, 내용1, 내용2
    #print(el)
    name = el.find('p', class_='intro_name').text
    title = el.find('p', class_='intro_answer').text
    content1 = el.find('pre', class_='intro_content1').text
    content2 = el.find('span').text

    print({'name':name, 'title':title, 'content1':content1, 'content2':content2})

