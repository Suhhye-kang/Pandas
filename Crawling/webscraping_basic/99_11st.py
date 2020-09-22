import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

  
url ="https://search.tmon.co.kr/search/?keyword=%ED%8B%B0%ED%8C%8C%EB%8B%88%EC%95%A4%EC%BD%94"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs ={"class":"item"})
print(items[0])
# for item in items:
#     name = item.find("strong", attrs={"class":"tx"}).get_text() #제품명
#     price = item.find("i", attrs={"class":"num"}).get_text() #가격
#     rate = item.find("span", attrs={"class":"grade_average_score"}).get_text() #평점
#     buy = item.find("span", attrs={"class":"buy_count"}).get_text() #구매개수
#     ship = item.find("span", attrs={"class":"text"}).get_text() #무료배송
#     link = item.find("a",attrs={"class":"anchor"})["href"] #링크  

#     print(f"제품명: {name}")
#     print(f"가격: {price}")
#     print(f"평점: {rate}점 {buy}개)")
#     print(f"무료배송: {ship}")
#     print("바로가기: {}".format(link))
#     print("-"*100) #줄긋기