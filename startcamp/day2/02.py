# Dictionary (딕셔너리) #궁극의 자료형 , 각각의 인덱스 존재x 키가 존재 

my_home = {
    'location': 'seoul',
    'area-code': '02'
}

# 딕셔너리 원소 접근
#1
print(my_home['location'])
# print(my_home['name']) #key 에러 
#2
print(my_home.get('location'))
print(my_home.get('name')) #에러는 안뜨고 None 이라고 출력 됨  #에러를 출력안해준다는 장점이 있다

