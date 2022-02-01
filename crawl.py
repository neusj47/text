# 뉴스기사 크롤링하기 ("WONA IN IT 참고")
# 0. 크롤링할 url 생성하기
# 1. 각 뉴스의 url 속성 가져오기 (제목, 링크, 내용)
# 2. 크롤링하여 데이터 프레임 만들기

from bs4 import BeautifulSoup
import requests
import pandas as pd


# 페이지 url 형식에 맞게 바꾸어 주는 함수 만들기
  #입력된 수를 1, 11, 21, 31 ...만들어 주는 함수
def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num+1
    else:
        return num+9*(num-1)

# 크롤링할 url 생성하는 함수 만들기 (검색어, 크롤링 시작 페이지, 크롤링 종료 페이지)
def makeUrl(search,start_pg,end_pg):
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(start_page)
        print("생성url: ",url)
        return url
    else:
        urls= []
        for i in range(start_pg,end_pg+1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page)
            urls.append(url)
        print("생성url: ",urls)
        return urls

# html에서 원하는 속성 추출하는 함수 만들기 (기사, 추출하려는 속성값)
def news_attrs_crawler(articles,attrs):
    attrs_content=[]
    for i in articles:
        attrs_content.append(i.attrs[attrs])
    return attrs_content

#뉴스기사 내용 크롤링하는 함수 만들기(각 뉴스의 url)
def news_contents_crawler(news_url):
    contents=[]
    for i in news_url:
        #각 기사 html get하기
        news = requests.get(i)
        news_html = BeautifulSoup(news.text,"html.parser")
            #기사 내용 가져오기 (p태그의 내용 모두 가져오기)
        contents.append(news_html.find_all('p'))
    return contents

#html생성해서 기사크롤링하는 함수 만들기(크롤링할url): 3개의 값을 반환함(제목, 링크, 내용)
def articles_crawler(urls):
    #html 불러오기
    original_html = requests.get(urls)
    html = BeautifulSoup(original_html.text, "html.parser")
    # 검색결과
    articles = html.select("div.group_news > ul.list_news > li div.news_area > a")
    title = news_attrs_crawler(articles,'title')
    url = news_attrs_crawler(articles,'href')
    content = news_contents_crawler(url)
    return title, url, content #3개의 값을 반환



#########################################################################################################

#검색어 입력
search = "스우파"
#검색 시작할 페이지 입력
page = 1
#검색 종료할 페이지 입력
page2 = 3

# naver url 생성
urls = makeUrl(search,page,page2)

#뉴스 크롤러 실행
news_titles = []
news_url =[]
news_contents =[]
for i in range(0,len(urls)):
    title, url,content = articles_crawler(urls[i])
    news_titles.append(title)
    news_url.append(url)
    news_contents.append(content)

# 데이터 프레임 만들기
#제목, 링크, 내용 1차원 리스트로 꺼내는 함수 생성
def makeList(newlist, content):
    for i in content:
        for j in i:
            newlist.append(j)
    return newlist

#제목, 링크, 내용 담을 리스트 생성
news_titles_1, news_url_1, news_contents_1 = [],[],[]

#데이터 프레임 만들기
news_df = pd.DataFrame({'title':makeList(news_titles_1,news_titles),'link':makeList(news_url_1,news_url),'content':makeList(news_contents_1,news_contents)})
