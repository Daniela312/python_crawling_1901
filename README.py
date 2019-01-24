# python_crawling_1901

from bs4 import BeautifulSoup
import urllib.request
import re

TOP10_FILE_NAME = 'Top10News.txt'
NewsScraping = 'NewsScraping.txt'
URL = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"

def clean_text(text):
    cleaned_text = re.sub('[\{\}\/?.,;:|\)*~!^\-_+<>@\#$%&\\\=\(\'\"]', '', text)
    cleaned_text = re.sub('[a-zA-Z]', '', cleaned_text)
    cleaned_text = re.sub('본문 내용', '', cleaned_text)
    cleaned_text = re.sub('플레이어', '', cleaned_text)
    cleaned_text = re.sub('오류를 우회하기 위한 함수 추가', '', cleaned_text)
    # cleaned_text = re.sub('▲', '', sp[1])
    # return cleaned_text
    return cleaned_text

def newsScraping(url_news, title):
    with open(NewsScraping, 'a', encoding='utf-8') as f:

        f.write(title)
        f.write("\n")

        source_code = urllib.request.urlopen(url_news)
        soup = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')

        text = ''
        for item in soup.find_all('div', id='articleBodyContents'):
            text = text + str(item).replace('<br/>', '\n')
            
        f.write(clean_text(text))
        f.write("\n\n\n")
        f.close


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
        newsScraping(link, title)

        #Write on the Text
        f.write(link)
        f.write("\n")
        f.write(title)
        f.write("\n\n")

    f.close()


def main():
    getTop10News(URL)


main()
