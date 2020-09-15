import requests
url = "https://www.melon.com/chart/month/index.htm?classCd=GN0000"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
res=requests.get(url, headers=headers)
res.raise_for_status()
with open("melon.html", "w", encoding="utf8") as f:
    f.write(res.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "lxml")

musics = soup.find_all("div", attrs = {"class": "ellipsis rank01"})
for music in musics:
    print(music.get_text())


singers = soup.find_all("div", attrs = {"class": "ellipsis rank02"})
for singer in singers:
    name = artist.a.get_text()
    print(name)
