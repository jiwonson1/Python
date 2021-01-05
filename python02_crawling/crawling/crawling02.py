from bs4 import BeautifulSoup


text = '''
<html>
<head>
    <title>HTML Test</title>
</head>
<body>
    <ul>
        <li>Java</li>
        <li>Oracle</li>
    </ul>
    <ol>
        <li>Hello</li>
        <li>Python</li>
    </ol>
</body>
</html>
'''

soup = BeautifulSoup(text, 'html.parser')
#print(soup)
#print(soup.text)

liResult = soup.select('ul>li')
'''
print(liResult)
print(liResult[0])
print(type(liResult[0]))
print(liResult[0].text)
'''
for el in liResult:
    print(el.text)

