# python_crawling_1901

from bs4 import BeautifulSoup
import urllib.request

OUTPUT_FILE_NAME = 'output.txt'
URL = "https://news.naver.com/main/ranking/read.nhn?rankingType=popular_day&oid=003&aid=0009022623&date=20190121&type=1&rankingSectionId=100&rankingSeq=1"

#function of crawling
def get_news(URL):
    source_code = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code, 'html', from_encoding='utf-8')
    text = ''

    for item in soup.find_all('div',id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    
    return text



def main():
    get_news(URL)
    f = open(OUTPUT_FILE_NAME, 'w')
    result_text = get_news(URL)
    f.write(result_text)
    f.close()


main()
