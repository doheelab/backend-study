#%%

# 출처: https://estenpark.tistory.com/353 [DATA 전문가로 가는 길]

import time

from urllib.request import urlopen
from bs4 import BeautifulSoup

stockItem = "005930"

url = "http://finance.naver.com/item/sise_day.nhn?code=" + stockItem
html = urlopen(url)
source = BeautifulSoup(html.read(), "html.parser")


maxPage = source.find_all("table", align="center")
mp = maxPage[0].find_all("td", class_="pgRR")
mpNum = int(mp[0].a.get("href")[-3:])

for page in range(1, mpNum + 1):
    print(str(page))
    url = (
        "http://finance.naver.com/item/sise_day.nhn?code="
        + stockItem
        + "&page="
        + str(page)
    )
    html = urlopen(url)
    source = BeautifulSoup(html.read(), "html.parser")
    srlists = source.find_all("tr")
    isCheckNone = None

    if (page % 1) == 0:
        time.sleep(1.50)

    for i in range(1, len(srlists) - 1):
        if srlists[i].span != isCheckNone:

            srlists[i].td.text
            print(
                srlists[i].find_all("td", align="center")[0].text,
                srlists[i].find_all("td", class_="num")[0].text,
            )


#%%

# reference: https://jeongwookie.github.io/2019/03/18/190318-naver-finance-data-crawling-using-python/

import requests
from bs4 import BeautifulSoup

# company_code를 입력받아 bs_obj를 출력
def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj


# company_code를 입력받아 now_price를 출력
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})
    now_price = blind.text
    return now_price


# 펄어비스 회사 코드는 "263750"
# 삼성전자 회사 코드는 "005930"
# 셀트리온 회사 코드는 "068270"
company_codes = ["263750", "005930", "068270"]

for item in company_codes:
    now_price = get_price(item)
    print(now_price)
