import requests
from bs4 import BeautifulSoup
url = 'https://finance.naver.com/marketindex/'

response = requests.get(url).text
print(type(response))
data =  BeautifulSoup(response, 'html.parser')
# print(data)
print(type(data)) #타입바뀌었나보자
result = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(result)
# print(result.text)  #result에서 text뒤에 안붙혔을때

# 크 롤 링 은 많이 시도해보고 좌절도 해봐야 실력이 는다 ! 

# 어플리케이션간 인터페이스 api 주로 json(자바스크립트류) 파일로 주로 씀



