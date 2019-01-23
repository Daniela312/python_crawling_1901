# python_crawling_1901

from bs4 import BeautifulSoup
import urllib.request
import re

TOP10_FILE_NAME = 'Top10News.hwp'
URL = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"

#function of crawling
def getTop10News(URL):

    #Open Text File
    f = open(TOP10_FILE_NAME, 'a')

    #Web Crawling
    source_code = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code, 'html.parser', from_encoding='utf-8')

    table = soup.find(id="lnb.mainnews")
    lines = table.ul.find_all('li')
    for line in lines[:10]:
        a = line.find('a')
        link = a.attrs['href']
        title = a.attrs['title']

        #Write on the Text
        f.write(link)
        f.write("\n")
        f.write(title)
        f.write("\n\n")

    f.close()

    

def main():
    getTop10News(URL)


main()
