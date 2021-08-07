import requests
from bs4 import BeautifulSoup

URL = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
res = requests.get(URL)

print(res.text)
