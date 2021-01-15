import requests

from bs4 import BeautifulSoup 

name = 'harry'
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()
print(response)
print(type(response))
# <bound method Response.json of <Response [200]>>
# <class 'method'>
# json 뒤에  () 써주면 >> 어디에 속했을때 .get() 클래스 안에 있는거 호출할때 괄호!
# text는 어트리뷰트 json은 메서드 
# {'name': 'harry', 'age': 56, 'count': 22485}
# <class 'dict'>

age = response['age']
print(f'{name}의 나이는 {age}살 입니다.')
