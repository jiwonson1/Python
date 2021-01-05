import requests

html = requests.get("http://www.google.com")
print(html.text)