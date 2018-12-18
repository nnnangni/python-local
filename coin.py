import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
res = requests.get(url).text #문서만 보기 위해서는 text 붙여야됨
# request.get("https://www.bithumb.com/") 도 가능
soup = BeautifulSoup(res,'html.parser') #지금은 html문서를 크롤링하기때문에 html.parser 옵션 지정
coins = soup.select('tbody.coin_list tr')
for coin in coins:
    print(coin.select_one("td:nth-of-type(1) a strong").text) #셀렉트로 하면 list로 반환해서 text옵션이안됨 그래서 one으로
    print(coin.select_one("td:nth-of-type(2) strong").text)
    print("-------------------")