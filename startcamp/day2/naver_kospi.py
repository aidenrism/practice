import requests
from bs4 import BeautifulSoup

# 1. url 
# 2. url 로 요청을 보낸다.
# 3. 받은 응답을 예쁘게 꾸며준다.
# 4. 꾸민 응답중에서 원하는 데이터를 선택한다.

#1
url = 'https://finance.naver.com/sise/'

#2
response = requests.get(url).text
print(type(response))
# <class 'requests.models.Response'>
#<class 'str'>   text뒤에 붙여서 

#3
data = BeautifulSoup(response, 'html.parser')
print(type(data)) #<class 'bs4.BeautifulSoup'>

#4
# result = data.select_one('#KOSPI_now')

# print(result)
#<span class="num" id="KOSPI_now">3,149.41</span>
result = data.select_one('#KOSPI_now').text
print(result) #3,149.41


