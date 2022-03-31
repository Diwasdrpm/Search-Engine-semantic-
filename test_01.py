import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *
workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'Number')
table.write(0, 1, 'movie_url')
table.write(0, 2, 'movie_name')
table.write(0, 3, 'movie_introduction')
line = 1
url = "https://icv2.com/articles/markets/view/50097/top-50-comics-december-2021/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)
movies_lst = []
soup = BeautifulSoup(f.content, 'lxml')
movies = soup.find('table', {'class': 'table'}).find_all(' ')
num = 0
for anchor in movies:
    urls = 'https://www.icv2.com' + anchor['href']
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