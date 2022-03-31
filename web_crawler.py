import re
from pathlib import Path
import queue
from urllib import response
from numpy import equal
import requests
from bs4 import BeautifulSoup
import mysql.connector

def getdata(url):
    r = requests.get(url)
    return r.content


def paragraph(listing_final,xyz,keyword):  
    i = 0
    for line in listing_final:
        tuples = []
        print(line)
        # print("")  
        tuples.append(keyword)
        tuples.append(i+1)
        # soup.title.get_text()
        htmldata = getdata(line)
        soup = BeautifulSoup(htmldata, 'html.parser')
        data_a = ''
        c =''
        for data_a in soup.find_all("h1"):
            b=data_a.get_text()
            c =c + (" ".join(b.split()))
        tuples.append(c)
        tuples.append(line)      
        data = ''
        y=0
        a=''
        for data in soup.find_all("p"):
            if(y>3):
                break
            x=data.get_text()
            a = a + (" ".join(x.split()))
            # print(x)
            y=y+1
        # tuples.append(a)
        xyz.append(tuples)
        i = i+1
        print("")
    print("")
    # print("")   
    # print(xyz)
    print("")
    # print("")
    print("")
    tuples_final = [tuple(x) for x in xyz]
    # for line in tuples_final:
    #     print(line)
    print(tuples_final)
    print(len(xyz))
    print("")
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="minor_2"
    )

    my_cursor=mydb.cursor()
    insert_keyword="INSERT INTO KEYWORD (WORD,RANKING,HEADING,LINKS) VALUES(%s,%s,%s,%s)"
    my_cursor.executemany(insert_keyword,tuples_final)
    my_cursor.execute("SELECT * FROM KEYWORD")
    myresult = my_cursor.fetchall()
    mydb.commit()
    

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
    print(count)
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
    
xyz = []
paragraph(listing_final,xyz,keyword)       

# for line in listing_final:
#     print(line)
#     print("")    
#     print("CONTENT:")
#     x = paragraph(line)
#     # print(x)
#     print("")
#     print("")
#     i+=1

# list final
# print(overall_final_list)

# for line in listing_final:
#     print(line)


# removing unnecessary websites
#  pushing changes to db
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="1234",
#   database="minor_2"
# )

# my_cursor=mydb.cursor()
# insert_keyword="INSERT INTO KEYWORD (WORD,RANKING,HEADING,LINKS) VALUES(%s,%s,%s,%s)"
# my_cursor.executemany(insert_keyword,overall_final_list)
# my_cursor.execute("SELECT * FROM KEYWORD")
# myresult = my_cursor.fetchall()
# for x in myresult:
#     print (x)
# mydb.commit()
