import re
from pathlib import Path
import queue
from urllib import response
import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.content


def paragraph(a):
    # if len(a) > 1:
    #     return -1
    try:
        htmldata = getdata(a)
        soup = BeautifulSoup(htmldata, 'html.parser')
        data = ''
        y=0
        for data in soup.find_all("p"):
            if(y>3):
                break
            x=data.get_text()
            x = " ".join(x.split())
            print(x)
            y=y+1

    except:
        print("No data recieved from that site......")


def find_local_anchors(soup, start_anchor):
    anchors = set()
    for link in soup.find_all('a'):
        anchor = link.attrs["href"]
        if "href" in link.attrs:
                anchors.add(anchor)
    return anchors


def crawl(base_url , start_anchor):
    search_anchors = queue.Queue()
    urls = set()
    count = 0
    while True:
        response = requests.request('GET',base_url + start_anchor)
        soup  = BeautifulSoup(response.text,"lxml")
        anchors = find_local_anchors(soup, start_anchor)
        if not start_anchor:
            for a in anchors:
                url =  a
                urls.add(url)
               

        if anchors:
            for a in anchors:
                url = a
                urls.add(url)
                count = count + 1
        
        if search_anchors.empty():
            break
        start_anchor = search_anchors.get()
    # print(count)
    return urls



keyword = input("Enter the word you want to search on google:")
url= 'https://www.google.com/search?q='+keyword
start_anchor = '/'
urls = crawl(url, start_anchor)
Link_of_urls = set()
for line in urls:
    if 'https' in line and 'google' not in line:
        Link_of_urls.add(line.split('=')[1])



list_link_of_urls = list(Link_of_urls)


# Parasing URL's and get the desired URL in working format
list_final = []
i = 0
for line in list_link_of_urls:
    list_final.append(line.split('&')[0])  
    i+=1

# for line in list_final:
#     print(line)

print("")
print("")
print("")

i=0
listing_final = []
for line in list_final:
    if '%' in line:
        list_final.remove(line)
    else:
        listing_final.append(line)    


for line in listing_final:
    print(line)
    print("")    
    print("CONTENT:")
    x = paragraph(line)
    # print(x)
    print("")
    print("")
    i+=1


print("")


# i=0
# list_fully_final = []
# for line in list_final:
#     if(len(list_final[i]) > 1):
#         list_fully_final[i].append(list_final[0][0])
#     else:
#         list_fully_final[i].append(list_final[i])
#     i=i+1



# for item in fully_final:
#     print(item)



# while(i<len(list_final)):
#     htmldata = getdata(list_final[i])
#     soup = BeautifulSoup(htmldata, 'html.parser')
#     data = ''
#     print( list_final[i] + " : paragraph for this url is listed below")

#     for data in soup.find_all("p"):
#         print(data.get_text())

#     i+=1

