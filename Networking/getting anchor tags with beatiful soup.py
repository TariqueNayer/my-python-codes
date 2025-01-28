import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input("Enter a website:- ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

#retrieve the anchor tag
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
