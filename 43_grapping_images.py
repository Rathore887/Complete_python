import requests
import bs4

res=requests.get("https://en.wikipedia.org/wiki/Wikipedia:Ten_things_you_may_not_know_about_images_on_Wikipedia")
soup=bs4.BeautifulSoup(res.text,'lxml')
# print(soup)
# print(soup.select('img'))
print(soup.select('img')[0])
print(soup.select('.mw-logo-icon'))