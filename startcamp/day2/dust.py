import requests
from pprint import pprint

key = 'MJjsaZ0vrFAngawH5ZY%2BnDFTdIs0CVoA%2Fi4mBvP5EyUueV56YZ2GuGyZ67X%2BtRKbZn%2BvcA0%2FamLt6X%2BExyd75w%3D%3D'
return_type = 'json'
num_of_raws = '5'
page_no = '1'
sido_name = '경기'
ver = '1.0' 
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_raws}&pageNo={page_no}&sidoName={sido_name}&ver={ver}'
# 문자열끼리는 더할 수 있음 ' '+ ' '

response = requests.get(url).json()

#sidoname의 미세먼지 농도는 pm10Value 입니다 라는 메세지를 출력하시오.

pprint(response['response']['body']['items'][0]['sidoName'])

sidoname = response['response']['body']['items'][4]['stationName']
dust =   response['response']['body']['items'][0]['pm10Value']

print(f'{sidoname}의 미세먼지 농도는 {dust}입니다.')
#리턴이 없는  response['response']['body']['items'][4]['stationName'] 이거는 {}안에 넣어도 에러가 남

response['response']['body']['items'][4]['stationName'] #None 

