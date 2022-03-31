import requests
import bs4
import lxml
from bs4 import BeautifulSoup
from xlwt import *  
text= input("Enter the keyword you want to search")
url = 'https://www.bing.com/search?q=' + text
# request_result=requests.get( url )

# soup = bs4.BeautifulSoup(request_result.text, "html.parser")

workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'Number')
table.write(0, 1, 'movie_url')
table.write(0, 2, 'movie_name')
table.write(0, 3, 'movie_introduction')
line = 1
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)
movies_lst = []
soup = BeautifulSoup(f.content, 'lxml')
movies = soup.select_one('div', {'class': "yuRUbf"})
num = 0
for anchor in movies:
    url = 'https://www.bing.com/search?q=' + text
    movies_lst.append(urls)
    num += 1
    movie_url = urls
    movie_f = requests.get(movie_url, headers = headers)
    movie_soup = BeautifulSoup(movie_f.content, 'lxml')
    movie_content = movie_soup.find('div', {'class': 'movie_synopsis clamp clamp-6 js-clamp'})
    print(num, urls, '\n', 'Movie:' + anchor.string.strip())
    print('Movie info:' + movie_content.string.strip())
    table.write(line, 0, num)
    table.write(line, 1, urls)
    table.write(line, 2, anchor.string.strip())
    table.write(line, 3, movie_content.string.strip())
    line += 1
workbook.save('comic_top100.xls')
print(soup)