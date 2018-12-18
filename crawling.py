import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
# res = requests.get(url).status_code
res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser') #bs를 통해 예쁘게 정제, soup 에 담음

#li는 뒷부분 지우고 뒤에 child는 of-type으로 바꿈
#마지막에 a태그는 여는태그와 닫는태그가 있음, .text는 a태그 앞의 글자만 가져옴
picks = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a')

# 리스트가 반복이되는데 for문이 가능함.
for p in picks:
    print(p.text)



