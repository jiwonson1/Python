import requests
from bs4 import BeautifulSoup


html = requests.get('https://news.daum.net/digital')
soup = BeautifulSoup(html.text, 'html.parser')
#print(soup)
result = soup.select('.tit_thumb a')
#print(result)
for el in result:
    print(el.text)
