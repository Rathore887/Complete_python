import requests
import bs4

result=requests.get("http://www.example.com")
print(type(result))
print(result.text)

soup=bs4.BeautifulSoup(result.text,"lxml")
print(soup)  # make code more beautiful

print(soup.select('title'))
print(soup.select('title')[0].getText())
site_paragraphs=soup.select("p")
print(site_paragraphs[0].getText())
print(soup.select('p'))

