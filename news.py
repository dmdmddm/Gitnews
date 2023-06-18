import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

titleList = []

for j in range(1, 100, 10) : 
    # 네이버 속보 1페이지 가져오기
    res = req.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%86%8D%EB%B3%B4&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=45&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1")
    soup = bs(res.text, "lxml")

    # 속보의 이름 데이터 select
    title = soup.select("a.news_tit")

    for i in title : 
        titleList.append(i.text)

dic = {"뉴스제목" : titleList}
df = pd.DataFrame(dic)
df.to_csv("data.csv", encoding = 'euc-kr', index = False)
