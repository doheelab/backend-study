import requests
from bs4 import BeautifulSoup

search = "삼성전자"
raw = requests.get(
    f"https://search.naver.com/search.naver?where=news&query={search}",
    headers={"User-Agent": "Mozilla/5.0"},
)
html = BeautifulSoup(raw.text, "html.parser")

articles = html.select("ul.list_news > li")

# 리스트를 사용한 반복문으로 모든 기사에 대해서 제목/언론사 출
for ar in articles:
    title = ar.select_one("a.news_tit").text
    source = ar.select_one("a.info").text
    source = source.split(" ")[0]
    print(title, source)
