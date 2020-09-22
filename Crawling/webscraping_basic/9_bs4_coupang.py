 import re
import requests
from bs4 import BeautifulSoup

url ="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# print(res.text)
items = soup.find_all("li", attrs ={"class":re.compile("^search-product")})
#print(items[0].find("div", attrs={"class":"name"})).get_text()
for item in items:

    #광고 재품은 제외
    ad_badge=item.find("span",attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("광고 상품 제외합니다")
        continue    
    name = item.find("div", attrs={"class":"name"}).get_text() #제품명

    #애플제품 제외
    if "Apple" in name:
        print("애플상품 제외합니다")
        continue
    price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격

    #리뷰 50개이상 평점 4.5이상되는것만 조회
    rate = item.find("em", attrs={"class":"rating"}) #평점
    if rate:
        rate = rate.get_text()
    else: 
        print ("평점없는상품 제외합니다")
        continue
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()#예: (26)
        rate_cnt = rate_cnt[1:-1]
    else:
        print ("평점수 없는상품 제외합니다")
        continue
    if float(rate) >=4.5 and int(rate_cnt) > 100 :
        print(name, price, rate, rate_cnt)