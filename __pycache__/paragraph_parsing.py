import pandas as pd
from pathlib import Path
import queue
from urllib import response
import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text

keyword = input("Enter the word you want to search on google:")
url_1= 'https://www.google.com/search?q='+keyword
htmldata = getdata(url_1)
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all("p"):
    print(data.get_text())
