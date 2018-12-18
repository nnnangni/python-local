import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/?tabSel=exchange"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
moneys = soup.select('table tbody')

for money in moneys:
    print(money.select_one("tr:nth-of-type(1) td.tit"))
    print(money.select_one("tr:nth-of-type(1) td.sale"))

    print("-------------------")




    #asiaBody > table > tbody > tr.fst.link > td.name > a
    #asiaBody > table > tbody > tr.fst.link > td.idx

    #body > div > table > tbody > tr:nth-child(1) > td.tit
    #body > div > table > tbody > tr:nth-child(1) > td.sale
