import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

headers = {'User-Agent':'Chrome/66.0.3359.181'}
URL = 'https://www.thecall.co.kr/bbs/board.php?bo_table=phone&stx=01082539451'
req = urllib.request.Request(URL, headers=headers)
html = urlopen(req)
print(html)
# response = requests.get(URL).text
# time.sleep(3)
# soup = BeautifulSoup(response, 'html.parser')
# print(soup)
# class_test = soup.find(class_='article-content')
# print(class_test)